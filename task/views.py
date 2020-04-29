from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from task.serializers import TaskSerializer
from task.services import TaskServices

task_service = TaskServices()


class CreateTask(APIView):
    """
    API to create tasks
    """

    def post(self, request):
        try:
            ''' request user'''
            user = request.user
            ''' checking whether the user is signed in or not '''
            if user.is_authenticated:
                '''task serializer'''
                return task_service.create(data=request.data, user=user)
            else:
                return Response(
                    {
                        'success': False,
                        'error': 'Unauthorized user(user must login)',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'error': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )


class ViewTask(APIView):
    """
    API to view task details
    """

    def get(self, request, pk):
        try:
            ''' request user '''
            user = request.user
            ''' checking whether the user is signed in or not '''
            if user.is_authenticated:
                '''task serializer'''
                return task_service.view(user=user, pk=pk)
            else:
                return Response(
                    {
                        'success': False,
                        'error': 'Unauthorized user(user must login)',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'error': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )


class TaskList(APIView):
    def get(self, request):
        try:
            ''' request user '''
            user = request.user
            ''' checking whether the user is signed in or not '''
            if user.is_authenticated:
                '''task serializer'''
                return task_service.list(user=user)
            else:
                return Response(
                    {
                        'success': False,
                        'error': 'Unauthorized user(user must login)',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'error': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )


class UpdateTask(APIView):
    def patch(self, request, pk):
        try:
            ''' request user '''
            user = request.user
            ''' checking whether the user is signed in or not '''
            if user.is_authenticated:
                '''task serializer'''
                return task_service.update(pk=pk, data=request.data, user=user)
            else:
                return Response(
                    {
                        'success': False,
                        'error': 'Unauthorized user(user must login)',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'error': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )


class DeleteTask(APIView):
    def delete(self, request, pk):
        try:
            ''' request user '''
            user = request.user
            ''' checking whether the user is signed in or not '''
            if user.is_authenticated:
                '''task delete service'''
                return task_service.delete(pk=pk, user=user)
            else:
                return Response(
                    {
                        'success': False,
                        'error': 'Unauthorized user(user must login)',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'error': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )
