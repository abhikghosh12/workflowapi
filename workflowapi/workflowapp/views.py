from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import workflowSerializer, commentSerializer, stepSerializer
from .models import workflow, comment, step
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status , generics , mixins


# Create your views here.

class workflowViewSet(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    """
    API endpoint for workflow that allows users to be viewed or edited.
    """
    queryset = workflow.objects.all()
    serializer_class = workflowSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class commentViewSet(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    """
    API endpoint for comment that allows users to be viewed or edited.
    """
    queryset = comment.objects.all()
    serializer_class = commentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class stepViewSet(mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    """
    API endpoint for steps that allows users to be viewed or edited.
    """
    queryset = step.objects.all()
    serializer_class = stepSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class workflowListView(generics.ListCreateAPIView):
    """
    API endpoint for workflow list that allows users to be viewed or edited.
    """
    queryset = workflow.objects.all()
    serializer_class = workflowSerializer

    def list(self, request):

        queryset = self.get_queryset()
        serializer = workflowSerializer(queryset, many=True)
        return Response(serializer.data)

class commentListView(generics.ListCreateAPIView):
    """
    API endpoint for comment list that allows users to be viewed or edited.
    """
    queryset = comment.objects.all()
    serializer_class = commentSerializer
