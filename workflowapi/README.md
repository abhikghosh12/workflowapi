# How to use the workflow api

Within this short documentation, we want to show how to use the workflow api.

## Requiremnts

- Django==2.2.3
- Python==3.7
- djangorestframework==3.8
- drf-nested-routers

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
This will start the localserver at : http://localhost:8000/

## The example above would generate the following URL patterns:

- Access the admin: http://localhost:8000/admin/
- user: admin
- password: admin

- **URL pattern**: ^workflow/$ , **Name**: [ workflow-list](http://localhost:8000/workflow/)
- **URL pattern**: ^workflow/{pk}/$ , **Name**: [ workflow-detail](http://localhost:8000/workflow/1)
- **URL pattern**: ^comment/$ **Name**: [comment-list](http://localhost:8000/comment/)
- **URL pattern**: ^comment/{pk}/$ **Name**: [comment-detail](http://localhost:8000/comment/1)

## Testing the api

api is tested using [Insomnia](https://insomnia.rest/) for CRUD function. It is tested on workflow  and comment api end points.

### Make a GET Request

Let's make another post request, to create some data. Only now, we must use our JWT to access the endpoint. Make a New Request and select the proper type & format. Then, complete the request URL/endpoint and body (make sure all required fields are included). Once you've done that, click on the HEADER tab. I want to make a header called Authorization (**user**: admin **password**: admin) and paste in the JWT I received from my Login request. Once I've done that, I'll hit SEND.

#### Make a GET Request to workflow API endpoint  

The figure below shows the GET Request at [API endpoint](http://localhost:8000/workflow/1)
GET request for List of workflow at [API endpoint](http://localhost:8000/workflow/)

![retrieve from workflow api](/workflowapi/pictures/GET.JPG)

#### Make a GET Request to comment API endpoint

The figure below shows the GET Request at [API endpoint](http://localhost:8000/comment/1)
GET request for List of workflow at [API endpoint](http://localhost:8000/comment/)

![retrieve from comment api](/workflowapi/pictures/GET_comment.JPG)

### Make a POST Request

#### Make a POST Request to workflow API endpoint
![retrieve from workflow api](/workflowapi/pictures/POST.JPG)

#### Make a POST Request to workflow API endpoint
![retrieve from comment api](/workflowapi/pictures/POST_comment.JPG)
Here we focus on discussions related to the user story.

### Make a PUT Request

#### Make a PUT Request to workflow API endpoint
![retrieve from workflow api](/workflowapi/pictures/PUT_workflow.JPG)

#### Make a PUT Request to workflow API endpoint
![retrieve from comment api](/workflowapi/pictures/PUT_comment.JPG)


### Make a DELETE Request

#### Make a DELETE Request to workflow API endpoint
![retrieve from workflow api](/workflowapi/pictures/DELETE_workflow.JPG)

#### Make a DELETE Request to workflow API endpoint
![retrieve from comment api](/workflowapi/pictures/DELETE_comment.JPG)
