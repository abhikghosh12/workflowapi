import os
import datetime
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workflowapi.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from workflowapp.models import workflow, comment, step
from workflowapp.serializers import workflowSerializer, commentSerializer, stepSerializer
from data import *

# Create data updates  here.
"""
Here JSON data are provided for workflow and comment (see folder data). This test checks the model and serializers.
This example JSON create to create a workflow

json_workflow1 =            {
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

Here JSON data are provided for workflow and comment. This test checks the model and serializers.
This example JSON  to create a comment of workflow


json_comment1 =     {
                        "name": "Concerned  person",
                        "text": "On the step 'Hit Nail' be careful to not hit your hand!"
                    }
"""
def add_workflow():
    with open('data/workflow.json') as f:
        json_workflow = json.loads(f.read())
    workflow_serializer = workflowSerializer(data=json_workflow)
    workflow_serializer.is_valid(raise_exception=True)
    workflow = workflow_serializer.save()
    workflow_serializer = workflowSerializer(instance=workflow)
    print(workflow_serializer.data)

def add_comment():
    with open('data/comment.json') as f:
        json_comment = json.loads(f.read())
    comment_serializer = commentSerializer(data=json_comment)
    comment_serializer.is_valid(raise_exception=True)
    comment = comment_serializer.save()
    comment_serializer = commentSerializer(instance=comment)
    print(comment_serializer.data)


if __name__ == "__main__":

    print("##########################################")
    print("Update of data into database in progress!")
    add_workflow()
    print("##########################################")
    add_comment()
    print("Done!!!")
    print("##########################################")
