# InventoryManagement
An application for a company system, where employees can login and view inventory. They can also update, delete, and create new items within the inventory after logging in.

## Getting Started
In order to get started you'll need a version of Python3 running on your machine. Once that is installed, cd into the root directory and install pipenv using the code below.

```
python -m pip install pipenv

```

After that, create your virtual environment using the command below, then activate your virtual environment by calling pipenv shell, as shown below.

```
pipenv install

pipenv shell

```
Install the required version of django according to the requirements.txt file, within your virtual environment.

## Running the application
In order to run the application, cd to the directory trydjango, which contains manage.py. From there you can run the following code to start the project.
Once you run the code below, copy the provided link to your browser, which should be your localhost. This application makes use of the Django's built in User and Admin to provide users.
With this I've created users/employees that can be used to login to the application. For this app, you can login with username: jdoe, password: seven.

```
python manage.py runserver

```
## Notes
This application allows for all CRUD operations for the given users and takes advantage of the django admin to add and delete users from the application.

## Contributors
- Shahran Islam
