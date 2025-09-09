# ⚽ Adinais Football Shop
Welcome to my first individual assignment, my very own football shop for Adinais Football Brand! This project is supposedly a fully functional web application built with Django for the Platform-Based Programming course. For now it has barely anything ☺️

**Live Application Link**: [CLICK LINK](https://rafasyah-miyauchi-adinaisfootball.pbp.cs.ui.ac.id/)

## So, How Was This Made?

Here's a quick rundown of the steps I took to get this thing up and running:

1. **Getting Started**: First things first, I set up a new Django project and an app called main to hold all the important stuff.

2. **The Database Blueprint (models.py)**: Then, I defined the Product model in models.py. This is basically the blueprint for every item in the shop, telling Django what info to store, like the name, price, description, etc.

3. **The Logic (views.py)**: The views.py file is where the main logic happens. 

4. **The Fun Part (main.html)**: This is the actual webpage! For now it is the bare minimum but later it will look better!

5. **Making it Work (urls.py)**: To make sure the pages actually show up, I set up the routing in urls.py. This connects the URLs you type in the browser to the right view function.

6. **Going Live (PWS Deployment)**: Finally, I deployed the whole thing to PWS so anyone can check it out online.

##  MVT Architecture Diagram

The Model-View-Template (MVT) pattern in Django handles web requests in a structured way.

![Image by fahadul Shadhin](1_XohhamnRotq53fQaY5HQfA.png)
    [SOURCE](https://python.plainenglish.io/the-mvt-design-pattern-of-django-8fd47c61f582)


1. You type in the URL, where your browser then sends a an HHTP request to the server.

2. The `urls.py` in the project folder catches it.

3. The app's `urls.py` takes over. It will then matches the URL to the show_main function in `views.py`.

4. The views.py function does the work. It basically processes the request. It can interact with the `models.py` to get data from the database. It then bundles this data into a `context` dictionary.

5. The template file (main.html) makes it pretty. This works because the view calls the `render()` function, which combines the specified HTML template with the `context` data. The template placeholders `{{ }}` are filled with the data.


6. Finally, Django sends the final, rendered HTML back to the user's browser, which displays the web page.

## Assignment Questions

### What is the role of `settings.py`?
The `settings.py` file is the central configuration hub for a Django project. It contains all the settings that define how the project runs. It includes:
* `INSTALLED_APPS`: A list of all applications that are active in the project.
* `DATABASES`: Configuration for connecting to databases (like SQLite for development or PostgreSQL for production).
* `SECRET_KEY`: A unique key for cryptographic signing.
* `DEBUG`: A boolean that toggles debug mode, showing detailed error pages when set to `True`.
* `ALLOWED_HOSTS`: A list of domains that are allowed to serve the Django application.

### How does database migration work in Django?
Database migration is Django's system for updating the database schema to match the application's models. To my knowledge, it's basically a two step process where,
1.  **`python manage.py makemigrations`**: This command basically inspects your `models.py` files for any changes (like adding a field or a new model) and creates a new "migration file." This file is essentially a Python script containing instructions on how to apply those changes to the database.
2.  **`python manage.py migrate`**: Finally this command finds all unapplied migration files and executes them in order. It translates the Python instructions into SQL commands and runs them against the database, thus updating the database schema.

### Why was Django chosen as a starting point?
I think Django is chosen as a starting point for the convenient aspect of database development due to its philosophy and its ease of use. Two in paticular are ORM (Object-Relational-Mapping) which essentially simplifies database interactions, and a Model-View-Template (MVT) architecture which organizes the application into thre distinch layers. 

### Feedback for Tutorial 1
I have personally no issue with Tutorial 1, but one aspect that makes it less effective was the fact that it was held online making communication and problem solvig requires us to share our screen which is a bit of an inconveniences especially during debugging stage