# SEI Project Four, Design Feed.

# Table of contents

* Project Overview
* Brief 
* Technologies Used
* Approach Taken
* Wins
* Challenges 
* Bugs
* Key Learnings
* Future Content 

# Project Overview 

The app has been deployed with Netlify and Heroku is available [here.](https://design-feed.netlify.app/)

Design Feed is an online social network that allows users to share their work, including images, measurements and technical drawings for feedback from other users.
This was my first experience creating a full stack app and creating a backend using Python3 and Django. This project was a solo project and I had 7 days to complete it.

![Screenshot 2021-10-08 at 14 40 04](https://user-images.githubusercontent.com/83759837/136567337-30493adf-9c32-4873-84ed-179e93ff9ef4.png)
![Screenshot 2021-10-08 at 14 41 01](https://user-images.githubusercontent.com/83759837/136567462-6eb2e8ba-7af3-4043-b824-8477c3bc5095.png)

# Brief

* Build a full-stack application by making your own backend and your own frontend.
* Use a Python Django API using Django REST Framework to serve your data from a Postgres database.
* Consume your API with a separate front-end built with React.
* Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models.
* Be deployed online so it’s publicly accessible.

# Technologies Used

__Frontend__

* React.js
* CSS3/ SASS
* Axios
* Nodemon
* React router dom
* React loader spinner
* React masonry component
* React moving text
* React star rating component 
* Material UI
* Chakra

__Backend__

* Python3
* Django
* Django REST Framework
* PostgreSQL

__Development Tools__

* Insomnia
* TablePlus
* Git & GitHub
* npm
* pip & pipenv
* Firefox dev tools
* Trello Board (planning and timeline)
* Excalidraw (planning)
* Slack

__Deployment__

* Heroku 
* Netlify 

# Appraoch Taken 

__Planning:__

Starting off in Excalidraw where I drew out a detailed layout plan of how I visualise my App to look and function. I find this a really useful start to a project as it helps me hugely further down the line if I am ever stuck on what I need to do. I then created a relationship diagram (ERD) which helped to inform me of all my models and data relationships.

Starting off in Excalidraw where I drew out a detailed layout plan of how I visualise my App to look and function. I find this a really useful start to a project as it helps me hugely further down the line if I am ever stuck on what I need to do. I then created an entity relationship diagram (ERD) which helped to inform me of all my models and data relationships.

![Untitled-2021-08-18-1303(7)](https://user-images.githubusercontent.com/83759837/136569133-6c739c7b-61bf-4763-b86f-bb7ebef2ac93.png)
![Screenshot 2021-10-08 at 14 52 24](https://user-images.githubusercontent.com/83759837/136569040-1e0f1c91-b5f6-4950-a68d-588cb2b23c0d.png)

__Backend:__

* This was not only my first experience creating a backend using Python3 and Django, it was also my first time creating a backend functionality solo. Taking this into consideration I gave myself 2-3 days to complete this. I used Django and Django REST Framework to create a PostgreSQL database with RESTful features. I started off by building my design model including a comment and user models. I worked in TablePlus to visualise my PostgreSQL database and Insomnia to test all my backend requests, ensuring all my model relationships were working and returning the correct JSON responses.  

```python
class Design(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    description = models.TextField()
    colour = models.CharField(max_length=50)
    size = models.PositiveBigIntegerField()
    print = models.BooleanField()
    image = models.CharField(max_length=300)
    design_drawing = models.CharField(max_length=300, blank=True)
    season = models.CharField(max_length=50)
    center_back_length = models.PositiveBigIntegerField(blank=True, null=True)
    center_front_length = models.PositiveBigIntegerField(blank=True, null=True)
    sleeve_length = models.PositiveBigIntegerField(blank=True, null=True)
    hem_length = models.PositiveBigIntegerField(blank=True, null=True)
    chest = models.PositiveBigIntegerField(blank=True, null=True)
    waist = models.PositiveBigIntegerField(blank=True, null=True)
    inside_leg_length = models.PositiveBigIntegerField(blank=True, null=True)
    outside_leg_length = models.PositiveBigIntegerField(blank=True, null=True)
    saved_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='saved_designs',
        blank='True'
    )

    added_by = models.ForeignKey(
        'jwt_auth.User',
        related_name='added_designs',
        on_delete=models.DO_NOTHING,
        blank=True
    )


    def __str__(self):
        return f'{self.name}'
```
