# How to use the workflow api

Within this short documentation, we want to show how to use the workflow api.

## requiremnts

- Django==2.2.3
- Python==3.7
- djangorestframework==3.8

## Overview
It uses django rest framework to build api. Here lets run the app.

Build the api:
```
python manage.py migrate
python manage.py makemigrations workflowapp

```
start the Server:
```
python manage.py runserver 0:8000
```
This will start the server at : http://127.0.0.1:8000/

## The example above would generate the following URL patterns:

Access the admin: http://localhost:8000/admin/
user: admin password: admin

- URL pattern: ^workflow/$ Name: [ workflow-list](http://localhost:8000/workflow/)
- URL pattern: ^workflow/{pk}/$ Name: [ workflow-detail](http://localhost:8000/workflow/1)
- URL pattern: ^comment/$ Name: [comment-list](http://localhost:8000/comment/)
- URL pattern: ^comment/{pk}/$ Name: [comment-detail](http://localhost:8000/comment/1)

The figure below shows the overview of the used agile board within this project.
You can find it under **Issues --> Boards**. There you can change between different
boards. In our chase we use one board for every sprint. In addition we compare a
sprint to the gitlab feature **MILESTONE**, so each **User Story** and **Task** challenged
within one **sprint** is labeled with a **MILESTONE**. This **MILESTONE** is dated with the
end of the **sprint** and is achieved with the end of the related **sprint**.


## Testing the api

api is tested using Insomnia for CRUD function. It is tested on workflow  and comment api end points.

### GET

![retrieve from workflow api](/workflowapi/pictures/GET.JPG)
![retrieve from comment api](/workflowapi/pictures/GET_comment.JPG)
To dive deaper into the usage of such an agile board, we now explain the usage of
every list in the board. On the left side, you first see the **Story** list. This list
contains every **user story** tackled within this sprint. It contains all realted taskst
to achieve the **user story**. These are so called related issues in gitlab.

### POST

![retrieve from workflow api](/workflowapi/pictures/POST.JPG)
![retrieve from comment api](/workflowapi/pictures/POST_comment.JPG)
Here we focus on discussions related to the user story.
### UPDATE

![retrieve from workflow api](/workflowapi/pictures/PUT_workflow.JPG)
![retrieve from comment api](/workflowapi/pictures/PUT_comment.JPG)
The second board list is the **to Do** list. This list contains all tasks, needed
to complete to achieve the **user story**. This means that every task related to
the user story is in this list. It should be as small featured as possible and we
additionally estimate a time it takes to complete this task (Remember this is done
within the sprint planning and as a team). After listing every task we need to tackle
and the sprint itself begins, we can start working on the tasks.
### DELETE

![retrieve from workflow api](/workflowapi/pictures/DELETE_workflow.JPG)
![retrieve from comment api](/workflowapi/pictures/DELETE_comment.JPG)
