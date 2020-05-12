# serializers.py
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import workflow, comment, step


class stepSerializer(serializers.ModelSerializer):
    class Meta:
        model = step
        fields = ['name', 'description']

class workflowSerializer(WritableNestedModelSerializer):
    steps = stepSerializer(many=True)
    class Meta:
        model = workflow
        fields = ['name', 'description', 'steps']

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ['name', 'text']
