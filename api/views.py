from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TaskRequestSerializer, TaskResponseSerializer
from api.utils import get_sorted_tasks


class TaskView(APIView):

    def post(self, request):
        request_serializer = TaskRequestSerializer(data=request.data)
        if request_serializer.is_valid():
            build = request_serializer.validated_data['build']

            tasks = get_sorted_tasks(build)

            response_serializer = TaskResponseSerializer(tasks)
            return Response(tasks, status=status.HTTP_200_OK)

        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
