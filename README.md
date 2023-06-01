#Django REST API Projects#
This repository contains two Django REST API projects. One is for managing companies, learning hubs and courses, and the other for managing an e-commerce cart with users, merchants, and products.

Project 1: Companies, Learning Hubs and Courses API
This API allows you to manage Companies, their associated Learning Hubs, and the courses offered at these hubs.

Installation and Setup
Clone the repository.
Navigate to the root directory of this project.
Run pip install -r requirements.txt to install the required dependencies.
Run python manage.py makemigrations and python manage.py migrate to create the database schema.
Run python manage.py runserver to start the server. The API will be available at http://localhost:8000/.
Endpoints
The API has the following endpoints:

/api/companies/: Get a list of all companies, their associated learning hubs and courses.
/api/companies/<int:id>/: Get a specific company by its ID along with its associated learning hubs and courses.
Testing
Run python manage.py test to execute the test cases.

Project 2: E-commerce Cart API
This API allows users to add products to their cart and calculate the total cost including the delivery fee.

Installation and Setup
Follow the same installation and setup steps as for Project 1.

Endpoints
The API has the following endpoints:

/api/cart/: Get a list of all carts with associated user, items, and total cost.
/api/cart/<int:id>/: Get a specific cart by its ID along with associated user, items, and total cost.
Testing
Run python manage.py test to execute the test cases.
