# How to use the workflow API

Within this short documentation, we want to show how to use the workflow api.
This readme describes every step required to get going with your own object detection classifier:
1. [Requirements](#Requirements)
2. [Build the API](#Build_the_API)
3. [Unit tests](#Unit_tests)
4. [ Update databases ](#Update_databases)
5. [ API Endpoints ](#API_Endpoints )
6. [ Testing the API (Integration tests) ](#Testing_the_API )
7. [ Known problems with solutions ](#Known_problems_with_solutions )

## Requirements

- Django==2.2.3
- Python==3.7.7
- djangorestframework==3.10.2
- drf-nested-routers

### Install

```    
pip install -r requirements.txt
```    
## Overview
It uses django rest framework to build API. Here lets Build, run and test the app. It creats a nested serializer and uses HTTP REST methods to do all CRUD functions.

The figure shows the Overview of the project. This has app folder called workflowapp and project folder workflowapi.

![retrieve from workflow api](/workflowapi/pictures/overview.JPG)

## Build the API

This will built the django API with sqlite3 databases.

```
python manage.py migrate
python manage.py makemigrations workflowapp

```
## Unit tests

This unit test `test_comment.py` and `test_workflow.py` checks:

* Create a workflow with API.
* GET a workflow with API.
* Update a workflow with API.
* Delete a workflow with API.
* Get workflow list.
* Create a comment with API.
* GET a comment with API.
* Update a comment with API.
* Delete a comment with API.
* Get comment list.

```   
    python manage.py test
```   

###  Update databases :

This Update `update_db.py` checks the model and serializers. This populates the databases with initial data. Here JSON data are provided for workflow and comment.

```
python update.py

```
Note: If error comes refer Known problems with solutions [ Known problems with solutions ](#Known_problems_with_solutions)

###  Start the Server:

This will start the localserver at : http://localhost:8000/

```
python manage.py runserver
```

###  Create superuser:

- Access the admin: http://localhost:8000/admin/
- user: admin
- password: admin

 or

 Create a new superuser
```
python manage.py createsuperuser
```

## API Endpoints

#### workflow

* **/workflow/**: [ workflow-list](http://localhost:8000/workflow/)(Todo create and list endpoint)
* **/workflow/{pk}/**: [ workflow-detail](http://localhost:8000/workflow/1)(Todo retrieve, update and destroy endpoint)

#### comment

* **/comment/**: [comment-list](http://localhost:8000/comment/)(Todo create and list endpoint)
* **/comment/{pk}/**: [comment-detail](http://localhost:8000/comment/)(Todo retrieve, update and destroy endpoint)


## Testing the API (Integration tests)

API is tested using [Insomnia](https://insomnia.rest/) for CRUD function. It is tested on workflow  and comment api end points.

### Make a GET Request

Let's make another post request, to create some data. Make a New Request and select the proper type & format. Then, complete the request URL/endpoint and body (make sure all required fields are included). Once you've done that, click on the HEADER tab. I want to make a header called basic Authorization e.g. (**user**: admin **password**: admin)
.
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


## Known problems with solutions

sqlite3.OperationalError: no such table: workflowapp_workflow

```
python manage.py migrate --run-syncdb
```
