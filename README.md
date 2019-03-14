# Instructions

NOTE: Before running this application you should run the code at https://github.com/emmet-gingles/Jupyter-OscarWinners to create the MySQL data.

1. Install Python from https://python.org/downloads/
2. Install Django: <br/>
	pip install django
3.	Create project: <br/>
	django-admin startproject myProject
4. Create app: <br/>
	cd myProject
	python manage.py startapp Oscars
5. Update MyProject/settings.py by adding 'Oscars' to the INSTALLED_APPS. <br/>
   Also change DATABASES to your MySQL connection.
6. Copy the files from this repository into your project.
7. Run Django server: <br/>
	python manage.py runserver
