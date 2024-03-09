from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer


class TaskListApi(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        output = [{'user': output.user_id, 'title': output.title, 'description': output.description,
                   'created_at': output.created_at, 'is_completed': output.is_completed} for output in Task.objects.filter(user=request.user)]
        return Response(output)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


class TaskApi(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request, pk):
        output = [{'user': output.user_id, 'title': output.title, 'description': output.description,
                   'created_at': output.created_at, 'is_completed': output.is_completed} for output in Task.objects.filter(pk=pk, user=request.user)]
        return Response(output)

    def delete(self, request, pk):
        Task.objects.get(user=request.user, pk=pk).delete()
        return Response(f'deleted task number {pk}')

    def patch(self, request, pk):
        task = Task.objects.get(user=request.user, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('wrong parameters')


'''
class TaskAPIView(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()
'''
# variants of same api
'''
class TaskAPIView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()

    @action(detail=False, methods=['get'])
    def tasks(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def create_task(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(serializer.data)
'''