# ToDoDjango


BackEnd Assignment
Clarusway
Subject: Django CRUD Operations Assignment
Learning Goal
Practice Django to implement CRUD (Create, Read, Update, Delete) operations.
Introduction
In this assignment, you will create a "TODO" Django app.
The root url will be a Todo form. Users can submit a new todo using this form.
After submission, the user will be linked to "list" page. Or they can go to the list page with a direct
link.
In list page, users will see the "Title", "Description", "Priority", and "isCompleted" of the TODO. Here
there will be "Add New", "Update", and "Delete" buttons.
"Add New" will go to the "TODO" form.
"Update" will go to the related TODO filled form, which can be updated.
"Delete" will erase the related TODO, and continue to show the list page.
Model
In this project, you need to create a TODO model with fields:
title
description
priority
isCompleted
updated_date
created_date
You can use choices option with priority.
Form
In this project, you need to create a forms.py file including TODO form using TODO model.
Views
In this project, you need to create four views:
todo_list # To read all TODO objects on the template.
todo_add # Including TODO form, to create TODO object.
todo_update # Including TODO form, to update TODO object.
todo_delete # To delete a TODO object.