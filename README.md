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

## Assignment 2 Questions:

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

## Assignment 3 Questions:

### Purpose of Data Delivery during Platform Implementatition
We need data delivery because modern applications are rarely built as a single piece. A universal format like JSON or XML acts as a common language. It allows the backend (our Django app) to "serialize" its data, sending it in a way that any frontend, be it a web browser, a mobile app, or even another server, can easily understand and work with.

### XML or JSON? Why is JSON more popular?
I personally prefer JSON for the same reason why it may be more popular than XML. First it's more readable, cleaner syntax and python dictionaries, it's more intuitive to me. It's more popular also because of the fact that it is lightweight.

### Purpose of is_valid() method and why do we need it?
The is_valid() method acts as a crucial security and data checkpoint. For example, when a form is submitted, the data is just raw text that we can't trust. is_valid() runs a series of checks on this data against the rules defined in our model and form. 

### Purpose of csrf_token?
It's basically a security feature that protects against Cross-Site Request Forgery (CSRF) attacks. A CSRF attack tricks a logged-in user into unknowingly submitting a malicious request on a website they trust. The csrf_token prevents this by placing a unique, secret token in every form. When the form is submitted, the server checks if the submitted token matches the one it issued. The attacker's fake form won't have this correct token, so Django will reject the malicious request, protecting the user.

### The Process to Assignment 3
Well, mostly I followed the breakdown from the Tutorial 2, but I went from models.py to check what are the data structure, then for this assignment 3, I start from the forms.py making sure to match it with the models.py. The important steps, which is the first point of this assignment is on views.py where I make 4 functions correlating with xml and json. In urls.py I then mapped each view to a specific URL, making the application's features accessible to users. Finally, I built the HTML templates to create the user interface, using Django's template language to dynamically display the data from the views.

### Feedback to TAs for Tutorial 2
I have no feedback for the tutorial 2, other than cross checking the information within the website to ensure that there are no error cause by syntax in the tamplate.

## Postman API Test Results

Here are the results of testing the data delivery endpoints.

### 1. Get All Products (JSON)
![All Products in JSON](images/jsonlocalhost.jpg)

### 2. Get All Products (XML)
![All Products in XML](images/xmllocalhost.jpg)

### 3. Get Product by ID (JSON)
![Product by ID in JSON](images/jsonid.jpg)

### 4. Get Product by ID (XML)
![Product by ID in XML](images/xmlid.jpg)

## Assignment 4 Questions:

### What is Django's AuthenticationForm? Explain its advantages and Disadvantages
It's a built in class from Django to handles anything about user login. It is a way to validates a user's credentials such as their username and password (what this website use) with the databases. The main advantage of AuthenticationForm is how it has a built-in security where it may handle most security checks automatically and error handling without us writing boilerplate code for a login form. The main disadvantage of AuthenticationForm is it's the bare minimum meaning it has limited customization and genereic appearance. For example, if we want to login with an email address, we must override its method. 

### What is the difference between authentication and authorization? How does Django implement the two concepts?
Authentication is the process of verifying who a user is. Whereas, Authorization is the process of verifying what an authenticated user is allowed to do. Within Django, it has a built in framework called django.contrib.auth to handle both aspect. Authentication is managed via the User model, middleware, and helper functions like authenticate() (to check credentials) and login() (to create a session for the user). While authorizaiton is handled by a built-in permission and groups system and decorator.

### What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?
To start, a cookie is a small data stored on the user's browser whereas a session is a mechanism to store user-specific data on the server. The main benefits is state management like personalized content and user logins sectios. Another is Security (sessions) where you can store sensitive infromation in a server-side session. The drawbacks are first the limited Size (Cookies), where it is limited to a small size (around 4KB), so they cannot be used to store large amounts of data. Whereas server Load (Sessions) where each active session consumes server memory and/or storage. For example, on a website with millions of active users, this can become a significant performance and scalability bottleneck.

### In web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?
No, the usage of cookies is not secure by default. There are a couple, but from what I learned in the slides, the two are regardingt Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF). XSS is a vulnerability that allows someone to inject JavaScript code that will be executed by the client. The potential problem with this vulnerability is that an attacker could steal cookies from users who are already logged into a website. Whereas CSRF could happen when an attacker tricks a logged-in user into clicking a link that performs an unwanted action on a website they are authenticated with. The browser will automatically include the authentication cookie with the request, making the malicious request seem legitimate to the server.

For CSRF, Django has a built-in CSRF protection framework. It works by adding a hidden csrfmiddlewaretoken field to POST forms. This token is unique to each user session. On submission, Django verifies this token, ensuring the request originated from the site itself and not from a malicious third-party source.

For XSS, Django’s Built in Security Features Cross Site Scripting (XSS) Protection. Using Django templates protects us against the majority of XSS attacks. Additionally, we can also use is_valid() in Django templates, forms.py and views.py

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
There are three documents that I am mostly working on, the first and foremost is my views.py, where I implemented register, login_user and logout for the authentication. After I do that, I worked on mapping each authentication view to a specific URL path to make it accessible from the browser. A few adjustment to the templates (html documents) to facilitate the authentication process such as the login.html and register.html. In addition to that I also added decorate @login_required(login_url='/login') to the show_main view to redirect any unauthenticated users to the login page. To finalize I update the model and view logic where in models.py I added ForeignKey relationship to the Product model, whilst editing the create_product in views.py in order to automatically assin the currently logged-in user to any new product being created. I tested all the changes in my local house by creating an account and trying the filter, session and cookies feature

## Assignment 5 Questions:

### **CSS Selector Priority**

I learned that when multiple CSS rules apply to one element, the browser decides which one wins based on specificity. The order from strongest to weakest is: `!important`, inline styles (the `style="..."` attribute), ID selectors (`#my-id`), class selectors (`.my-class`), and finally, element selectors (`div`). If two selectors are equally specific, the one that comes last in the stylesheet gets applied.

### **Responsive Design**

I believe responsive design is essential because it makes my website look good and work well on any device, from a phone to a desktop. This is great for user experience, helps with Google search rankings, and makes it easier for me to maintain the code since I only have one version to manage.

* **Good Example (FIFA.com):** I looked at the FIFA website. On my computer, it's a big, wide layout. On my phone, everything neatly stacks into a single column, and the menu changes to a mobile-friendly version. It's super easy to use anywhere.

* **Bad Example (1996 Space Jam Website):** For a non-responsive example, I checked out the original Space Jam movie site. On a phone, it's basically unusable. The whole page just shrinks down, and I have to zoom and scroll around to read anything, which shows exactly why we need responsive design today.

### **The Box Model**

I understand the CSS Box Model as a set of layers for every HTML element.

* **Padding:** This is the space *inside* an element's border, pushing the content away from the edge.

* **Border:** This is the line that goes *around* the padding and content.

* **Margin:** This is the space *outside* the border, used to push elements away from each other.

### **Flexbox vs. Grid**

For this project, I used both Flexbox and Grid to create the layout.

* **Flexbox:** I found Flexbox is perfect for arranging items in a single line (a row or a column). I used it a lot for centering content inside containers and for aligning the buttons in my forms and navbar.

* **Grid:** Grid was my choice for the overall page structure, specifically for the product list. It let me create a two-dimensional grid of cards that stays perfectly aligned in rows and columns, which is harder to do with Flexbox.

### **How I Made This**

Here's a quick rundown of the steps I took to build and design this assignment:

1. **Getting Started:** First things first, I set up a new base template (`base.html`) and plugged in **Tailwind CSS** using the CDN. This gave me all the style utilities I needed. I also wired up the basic views and URLs for the new "Edit Product" feature.

2. **What I think when I create the Vibe:** I didn't want a generic site, so I created a custom "futuristic sports" theme. I picked the `Orbitron` font, created a custom color palette with neon lime and dark grays, and used a "glassmorphism" effect to give the cards a cool, frosted look.

3. **Building the Navbar:** I built a fully responsive navigation bar from scratch. It looks great on desktop, and on mobile, it collapses into a hamburger menu that I made interactive with a bit of JavaScript.

4. **Making Cards Interactive:** I redesigned the product cards and added a "Quick View" feature. When a user clicks the button on a card, a modal pops up showing the product details. I research a bit in youtube and finds out that it used a bit of JavaScript and `data-*` attributes to pull the product info into the modal instantly without reloading the page.

5. **Fixing Bugs:** I ran into a bug where my forms weren't getting styled. I fixed this by adding a small script to the `login`, `register`, `create`, and `edit` pages that applies the correct Tailwind classes to the form fields after the page loads.

## Assignment 6 Questions:

### 1. What is the difference between synchronous request and asynchronous request?

From what I've learned in this assignment, the main difference is how they handle waiting for a response. A **synchronous** request is "blocking"—when I send a request, my browser freezes and waits for the server to send back a full new page. I can't click or interact with anything until that entire process is finished. It’s like making a phone call and having to wait on hold, unable to do anything else.

An **asynchronous** request, which is what I implemented with AJAX, is "non-blocking." I can send a request to the server in the background, and the user can continue to interact with the page. When the server sends back a small piece of data (like JSON), a little bit of JavaScript updates only the necessary part of the page. This is more like sending a text message—I can send it and then go about my day, and my phone will just notify me when a reply arrives.

### 2. How does AJAX work in Django (request-response flow)?

I implemented a clear request-response flow in my project to make AJAX work with Django. Here’s how I understood and built it:

1.  **Event Trigger on the Frontend:** It all starts with a user action, like clicking the "Add New Product" button. This triggers a JavaScript event listener that I wrote.
2.  **JavaScript `fetch()` Request:** The JavaScript function then uses the `fetch()` API to send a request to a specific URL on my Django server (e.g., `/create-product-ajax/`). For creating or updating, this is a `POST` request containing the form data.
3.  **Django URL Routing:** My `urls.py` file matches this URL to a specific view I created for handling AJAX requests, like my `add_product_ajax` view.
4.  **Django View Processing:** This view is different from a normal one. Instead of rendering a whole HTML page, it processes the incoming data, interacts with the database (like creating a new `Product` object), and then prepares a response.
5.  **Return `JsonResponse`:** The view returns a `JsonResponse`, which sends the data (e.g., `{'status': 'success', 'message': 'Product added!'}`) back to the browser in a simple, machine-readable format.
6.  **JavaScript DOM Manipulation:** My frontend JavaScript receives this JSON. Based on the response, it dynamically updates the page without a reload. For example, it might show a success toast, close the modal, and then call another function to refresh the product grid with the new item.

### 3. What are the advantages of using AJAX compared to regular rendering in Django?

After refactoring my project, I found several big advantages of using AJAX:

* **Vastly Improved User Experience (UX):** This is the biggest one. The website feels so much faster and more responsive. There are no more jarring full-page reloads when I add or delete a product. The user gets instant feedback through modals and toasts, which makes the app feel more modern and interactive.
* **Reduced Bandwidth and Server Load:** With regular rendering, Django had to rebuild and send the entire HTML page for every small change. With AJAX, the server only sends a tiny bit of JSON data. This is much more efficient and saves bandwidth, which I imagine would be very important for a real-world application with many users.
* **Better Separation of Concerns:** Using AJAX encouraged me to think of my Django backend more like an API. The backend's job is to handle data and business logic, while the frontend's job is to handle the presentation and user interaction. This separation made my code feel cleaner and more organized.

### 4. How do you ensure security when using AJAX for Login and Register features in Django?

Security was a major consideration, and I made sure to rely on Django's built-in features even when using AJAX.

First and foremost, my `login_ajax` and `register_ajax` views still use Django’s `AuthenticationForm` and `UserCreationForm`. These forms are crucial because they handle essential security tasks like protecting against invalid login attempts and, most importantly, correctly hashing passwords before storing them in the database. I'm not handling raw passwords in my views.

For Cross-Site Request Forgery (CSRF), which is common with form submissions, a fully secure implementation would involve sending the CSRF token with the AJAX `fetch` request. [cite_start]For this assignment, I followed the tutorial's approach of using the `@csrf_exempt` decorator[cite: 1077], which is simpler for development but something I'd replace by passing the token in the request headers in a production environment.

Finally, in a real production site, I would ensure all authentication traffic is sent over **HTTPS** to encrypt the data and prevent credentials from being stolen in transit.

### 5. How does AJAX affect user experience (UX) on websites?

AJAX completely transforms the user experience from something static into something dynamic and fluid.

The most immediate effect I noticed is the **feeling of speed and responsiveness**. Because the page doesn't have to reload, actions feel instantaneous. When I add a product, the grid just updates. This is a much better experience than waiting for a blank white screen while the server renders a whole new page.

Another key effect is **continuity**. The user never loses their context. For example, if they have scrolled down the product list, they can open a modal to edit a product and then close it, and they'll still be in the same scroll position. In a non-AJAX app, they would be sent to a new "edit" page and then redirected back, losing their place.

Finally, AJAX allows for richer, more interactive features that are standard on modern websites. The modal forms and toast notifications in my project are direct examples of this. They provide feedback and allow for user input without interrupting their main workflow, which is a huge improvement to the overall usability of the site.