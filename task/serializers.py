from datetime import datetime

from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    status = serializers.CharField(required=True, allow_null=False)
    created_at = serializers.DateTimeField(required=False, format="%d-%m-%Y %H:%M")
    updated_at = serializers.DateTimeField(required=False, format="%d-%m-%Y %H:%M")
    is_deleted = serializers.BooleanField(required=False)

    def validate_status(self, status):
        '''
        :param status: task status
        :return: status(if the status is valid)
        '''
        task_status = ('TODO', 'WIP', 'DONE')
        ''' checking whether status is an element of task_status tuple '''
        if status.upper() in task_status:
            return status
        raise serializers.ValidationError('Invalid status(Status must be in ["TODO", "WIP, "DONE"])', )

    def create(self, validated_data):
        '''
        :param validated_data: serializer validated data
        :return: newly created task instance
        '''
        task = Task.objects.create(created_by=self.context.get('user'), **validated_data)
        return task

    def update(self, instance, validated_data):
        '''
        :param instance: task instance
        :param validated_data: serializer validated data
        :return: modified task instance
        '''
        instance.title = validated_data.get('title', instance.title)
        instance.status = validated_data.get('status', instance.status)
        instance.updated_at = datetime.now()
        instance.save()
        return instance
