# SEI Project Four, Design Feed.

# Table of contents

* [Project Overview](#project-overview)
* [Brief](#brief) 
* [Technologies Used](#technologies-used)
* [Approach Taken](#approach-taken)
* [Wins](#wins)
* [Challenges](#challenges)
* [Bugs](#bugs)
* [Key Learnings](#key-learnings)
* [Future Content](#future-content-what-would-i-like-to-add-if-i-had-more-time) 

# Project Overview 

The app has been deployed with Netlify and Heroku is available [here.](https://design-feed.netlify.app/)

Design Feed is an online social network that allows users to share their work, including images, measurements and technical drawings for feedback from other users.
This was my first experience creating a full stack app and creating a backend using Python3 and Django. This project was a solo project and I had 7 days to complete it.

![Screenshot 2021-10-08 at 14 40 04](https://user-images.githubusercontent.com/83759837/136567337-30493adf-9c32-4873-84ed-179e93ff9ef4.png)
![Screenshot 2021-10-08 at 14 41 01](https://user-images.githubusercontent.com/83759837/136567462-6eb2e8ba-7af3-4043-b824-8477c3bc5095.png)

Please feel free to sign up and login with your own credentials or you can use the following: 

Username: zoe_daniels
Password: password

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
__Frontend:__

* Once the backend was complete I moved over to the frontend to map out the framework for the App and all its routes, using React-router-dom. I used Axios for all the data requests from the backend, creating an API request library that was imported into each page.

* My frontend structure was broken up into three sections. I spent about two days, starting from the top to bottom adding everything onto the page, including titles, text, buttons, inputs, images etc. Once all the structure and data had been added I went back and styled each page one by one which took about a day and a half. Working closely and comparing each page to my Excalidraw sketches, ensuring nothing had been missed out. I prefer to start the CSS as soon as possible to be able to visualise and see the App come to life, making it easier for me to think and create extra features or develop the current ones.

* I started off using Chakra for my framework but ended up using Material UI for my forms and styling the rest myself, as this is something I thoroughly enjoy. Styling each page one by one starting from the top enabled me to organise my SASS much better than in previous projects. This made things much easier when I came back to edit something as I was able to quickly find the right section. I chose to style my App in a way that looked clean and fresh due to my content being very busy already. Because my App was based around designers being able to view one another’s work I wanted the surrounding features to not be too distracting. My inspirations for colour palettes, fonts, forms, layout  and buttons came from Pinterest as I feel they have perfectly captivated this.

![Screenshot 2021-10-08 at 15 04 59](https://user-images.githubusercontent.com/83759837/136571015-623b7b24-a819-4e90-b5ed-6c9910123d72.png)

* Having a login popup window was a goal I really wanted to complete in this project. I researched and experimented with a couple of npm packages but I decided to hard code it myself by creating a separate login function and importing it into the relevant pages, using props and triggers. I found this a little challenging at first as I managed to get my close button to work but if the user had logged in successfully the popup was not closing. I resolved this by creating a constant for the trigger and the button and setting this to false once the user had successfully logged in.

```javascript
function LoginPopup(props) {

  const isLoggedIn = isAuthenticated()

  return (props.trigger && !isLoggedIn) ? (
    <div className="popup">
      <div className="popup-inner">
        <button className="close-button" onClick={() => props.setTrigger(false)}>Close</button>
        {props.children}
      </div>
    </div>
  ) : ''
}
```

<img width="1425" alt="Screenshot 2021-10-08 at 15 06 05" src="https://user-images.githubusercontent.com/83759837/136571176-20e58834-10b9-4300-8bf9-0205e6c4cd7b.png">

# Wins

* There were a few wins during this project, but the biggest win I have to say was presenting a full stack app fully functioning, working exactly how I envisaged, on my own. I did miss out on the perks of working collaboratively such as fixing bugs and challenges together, and I really enjoy bouncing ideas off team mates. However I am happy I chose to do this project solo as all the challenges I faced I was able to overcome, and this has really boosted my confidence as a developer.

* A coding win was getting my save and unsave button to work. Understanding how it worked in the backend, creating a saved by feature to my design model and creating the appropriate post request, enabled me to successfully create my save and unsave functions in my frontend.

```python
class DesignSaveView(APIView):
    '''Add saved to a design or remove if already saved'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, design_pk):
        try:
            design_to_save = Design.objects.get(pk=design_pk)
        except Design.DoesNotExist:
            raise NotFound()
        
        if request.user in design_to_save.saved_by.all():
            design_to_save.saved_by.remove(request.user.id)
        else:
            design_to_save.saved_by.add(request.user.id)
        
        serialized_design = DesignSerializer(design_to_save)

        return Response(serialized_design.data, status=status.HTTP_202_ACCEPTED)
```
```javascript
const handleSave = async (e) => {
    e.preventDefault()
    try {
      await saveUnsaveDesign(designId)
      setIsClicked(true)
      setIsSaved(!isSaved)
    } catch (err) {
      console.log(err)
    }
  }

  const handleUnsave = async (e) => {
    e.preventDefault()
    try {
      setIsSaved(!isSaved)
      await saveUnsaveDesign(designId)
      setIsClicked(false)
    } catch (err) {
      console.log(err)
    }
  }
```

* I found I managed my work load really successfully throughout this project, keeping to my daily deadlines and schedules. I was happy with my planning as I found that even though my ideas for pushing the App even further was constantly flowing I was organised with my workload and ability for only a week's time frame.

# Challenges 

A challenge I faced during the beginning stages of this project was my permission classes. I started off creating the backend so that the users had to be logged in at all times to view anything other than the homepage and the about page. By having all my requests to be authenticated I created a cookie within my browser, which even after deleting all the authentications meant I was still receiving 403 forbidden errors when trying to get or post my data. I spent some time going over my models in the backend and trying to figure out why it was working Insomnia but somehow not in my browser. However upon realising it was to do with my browser cookies, I was able to delete them and successfully hook up my frontend and backend.

# Bugs 

A bug which I have noticed is when a user is uploading a design, if not all the required fields are filled in, the post request is being sent as an empty object, appearing to have been sent through with no errors. However a design can’t be created with an incorrect form and therefore would not have been created and visible on the appropriate pages. The fields in my design model have a required attribute attached to them and work correctly in Insomnia, sending an error message of the missing fields. However in the front end it still sends the incorrect object with a success status of 200. In order to fix this I would need to find out why my post request is not erroring correctly. 

# Key Learnings

* I have learnt a huge amount from this project. Not only how to create a backend using Python and Django but understanding in much more depth the relationships between the backend and the frontend. I have found working in Insomnia and TablePlus really helpful for this. During this project I pushed my skill sets and challenged myself by going solo and I am really happy with how it turned out. My understanding of axios and React.js has been enhanced dramatically and I am looking forward to creating future projects using the languages and frameworks used within this project.

* I really enjoyed making my App mobile responsive, I would like to start an App in the future by initially being mobile responsive and working on this screen size first. 

# Future Content: What would I like to add if I had more time

* If I was to have had a bit more time I would have liked to add a confirm delete popup, similar to my login popup for when you delete a design.

* When I was initially planning this App I thought about the idea of having two types of users, one being a freelance user and another being a company user. The freelance user would work exactly how the user works now, they can view other peoples designs, like, save, comment, have their own profile etc. The company user would be slightly different. I had the idea that a company could set up an account with Design Feed, registering all of their employees. The idea behind this was to add privacy to a company, and that only those working within that company can see that company's designs.  

* Another idea that I would love to implement is to create a following, where users could not only like other users designs they could follow them too.

* As the App grows and more users add designs and comments, I realised that a couple of things would need to be changed to make it visually pleasing. For the designs, I thought about adding boards to your profile page’s saved and added by section, much like Pinterest. As the user adds and likes more designs this page is going to fill up and would need to be organised, which is where I thought a board would work perfectly here. The cards would be organised into their categories, so for example we would have a trouser board, dress board and so on. For the comments an idea I had would be to group the comments into a more messaging box. As users added their comments, if there was say more than the 5 they would build up and you could scroll through them, much like a comment box on Instagram or WhatsApp.

* Clean up and refractor code. 
