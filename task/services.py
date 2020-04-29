from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer


class TaskServices:
    @transaction.atomic
    def create(self, data, user):
        ''' checking the validity of serializer '''
        serializer = TaskSerializer(data=data, context={'user': user})
        ''' checking whether the API payload is valid or not '''
        if serializer.is_valid():
            ''' creating new task'''
            task = serializer.save()
            if task:
                ''' success response '''
                return Response(
                    {
                        'success': True,
                        'message': 'Task successfully created',
                        'data': serializer.data,
                    },
                    status=status.HTTP_201_CREATED
                )
        ''' serializer error response '''
        return Response(
            {
                'success': False,
                'error': 'Failed to create new task',
                'message': serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def view(self, user, pk):
        ''' checing whether the task id exists or not'''
        if Task.objects.filter(id=pk).exists():
            ''' task instance '''
            task = Task.objects.get(id=pk)
            ''' checking whether the task belongs to the requested user '''
            if task.created_by == user:
                serializer = TaskSerializer(task)
                ''' success response '''
                return Response(
                    {
                        'success': True,
                        'message': 'Task details successfully fetched',
                        'data': serializer.data,
                    },
                    status=status.HTTP_200_OK
                )
            ''' unauthorized access response '''
            return Response(
                {
                    'success': False,
                    'error': 'Task does not belong to {}'.format(user.email),
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        ''' invalid task id response '''
        return Response(
            {
                'success': False,
                'error': 'Invalid Task id',
            },
            status=status.HTTP_404_NOT_FOUND
        )

    def list(self, user):
        ''' Filtering tasks based on request user id '''
        tasks = Task.objects.filter(created_by=user, is_deleted=False)
        ''' task serializer '''
        serializer = TaskSerializer(tasks, many=True)
        ''' success response '''
        return Response(
            {
                'success': True,
                'message': 'Task list successfully fetched',
                'data': serializer.data,
            },
            status=status.HTTP_200_OK
        )

    @transaction.atomic
    def update(self, pk, data, user):
        ''' checking whether the tasks id exists or not '''
        if Task.objects.filter(id=pk).exists():
            ''' getting task object '''
            task = Task.objects.get(id=pk)
            ''' checking whether the task belongs to the requested user '''
            if task.created_by == user:
                serializer = TaskSerializer(data=data, instance=task)
                ''' checking whether the serializer is valid or not '''
                if serializer.is_valid():
                    ''' updating task details '''
                    serializer.update(instance=task, validated_data=serializer.validated_data)
                    ''' success response '''
                    return Response(
                        {
                            'success': True,
                            'message': f'Task: {pk}, successfully updated',
                            'data': serializer.data,
                        },
                        status=status.HTTP_200_OK
                    )
                return Response(
                    {
                        'success': False,
                        'error': f'Failed to update task: {pk}',
                        'message': serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            ''' unauthorized access response '''
            return Response(
                {
                    'success': False,
                    'error': 'Task: {} does not belong to {}'.format(pk, user.email),
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        ''' invalid task id response '''
        return Response(
            {
                'success': False,
                'error': f'No task found with id: {pk}',
            },
            status=status.HTTP_404_NOT_FOUND
        )

    @transaction.atomic
    def delete(self, pk, user):
        ''' Checking whether the task id exists or not '''
        if Task.objects.filter(id=pk).exists():
            ''' getting the task object '''
            task = Task.objects.get(id=pk)
            ''' checking whether the task belongs to the requested user '''
            if task.created_by == user:
                ''' deleting the task '''
                task.is_deleted = True
                task.save()
                ''' success response '''
                return Response(
                    {
                        'success': True,
                        'message': f'Task: {pk} successfully deleted',
                    },
                    status=status.HTTP_200_OK
                )
            ''' unauthorized access response '''
            return Response(
                {
                    'success': False,
                    'error': 'Task: {} does not belong to {}'.format(pk, user.email),
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        ''' invalid task id response '''
        return Response(
            {
                'success': False,
                'error': f'No task found with id: {pk}',
            },
            status=status.HTTP_404_NOT_FOUND
        )
