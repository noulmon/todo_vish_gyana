# DJANGO TODO APP: VISH GYANA TECHNOLOGY SOLUTIONS PVT. LTD.

### Introduction:
_**Django TODO APP**_ is a 'TASK MANAGEMENT'  application 
where the users register with the application using the email address and password.
The signed in user can create, view, update and delete the 'Todo Tasks'.
User can also get the list of all tasks created by them(only).


### Follow the steps to _run the application_:

1. Install all the required packages(python modules):

    ```pip install -r requirements.txt```

2. Migrate all the models to the database(Assuming that you've already setup the Database- PostgreSQL preferred)
 
    ```python manage.py migrate```
    
3. When the migrations are successfully completed, we can run the server:

    ```python manage.py runserver```
    
    If the steps are followed correctly, the server will be up and running.
 
 4. To gather all static files:
   
    ```python manage.py collectstatic```

 4. To login to admin panel, we have to create a superuser using email and password:
 
    ```python manage.py createsuperuser```
    
    User can log into the **Admin Panel** using the following url(assuming that you are on local server):
    
        http://127.0.0.1:8000/

## AWS:
 Elastic Beanstalk Instance: `http://todo-vish-gyana2-dev.ap-south-1.elasticbeanstalk.com/`

## API Documentation:
   - API Documentation are in: ``\docs\api_docs\todo_app_api_docs.json``
   - Browsable Documentation: `https://documenter.getpostman.com/view/6826654/SzmY819S` 

## API Endpoints:
#### User APIs:
1. For user to register in the application`(POST)`: ```/user/register/```
2. For user to sign in to the application`(POST)`: ```/user/login/```

#### Task APIs:
(**_`Note: Please add the 'user token' as the 'Authorization Header' for all below APIs`_**)
1. To create/add tasks`(POST)`: ```/task/create/```

2. To view task details`(GET)`: ```task/view/<int:pk>/```

3. To get the task list`(GET)`: ```task/list/```

4. To update task details`(PATCH)`: ```task/update/<int:pk>/```

5. To delete a task`(DELETE)`: ```task/delete/<int:pk>/```
