from rest_framework import serializers


class TaskRequestSerializer(serializers.Serializer):
    build = serializers.CharField()


class TaskResponseSerializer(serializers.Serializer):
    tasks = serializers.ListField()
