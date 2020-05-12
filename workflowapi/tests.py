import os
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workflowapi.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.test import TestCase
from workflowapp.models import workflow, comment, step
from workflowapp.serializers import workflowSerializer, commentSerializer, stepSerializer

# Create your tests here.
"""
Here JSON data are provided for workflow and comment. This test checks the model and serializers.
This example JSON create to create a workflow
"""


json_workflow =            {
                                "name": "How to nail something",
                                "description": "Basic instructions to nail something",
                                "steps": [
                                  {
                                     "name": "Place nail",
                                     "description": "Hold nail on top the thing to be nailed"
                                  },
                                  {
                                    "name": "Hit nail",
                                    "description": "Hit the nail repeatedly with a hammer"
                                  }
                                ]
                            }

"""
Here JSON data are provided for workflow and comment. This test checks the model and serializers.
This example JSON  to create a comment of workflow
"""

json_comment =     {
                        "name": "Concerned  person",
                        "text": "On the step 'Hit Nail' be careful to not hit your hand!"
                    }


workflow_serializer = workflowSerializer(data=json_workflow)
workflow_serializer.is_valid(raise_exception=True)
workflow = workflow_serializer.save()
workflow_serializer = workflowSerializer(instance=workflow)
print(workflow_serializer.data)

print('###################################################################################################')

comment_serializer = commentSerializer(data=json_comment)
comment_serializer.is_valid(raise_exception=True)
comment = comment_serializer.save()
comment_serializer = commentSerializer(instance=comment)
print(comment_serializer.data)
