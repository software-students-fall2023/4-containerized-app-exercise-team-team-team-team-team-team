[![check lint and format](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/lint.yml/badge.svg)](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/lint.yml)
[![CI/CD](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/python-app.yml/badge.svg)](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/python-app.yml)

# Team Members
`alexh212`- Alex Hmitti

- Webpage design

`as13909` - Aaron Stein :)

- Machine learning model implementation

`Rafinator123` - Rafael Nadal-Scala

- Docker Implementation
- Creating a scaffolding for the project

`jk021227` - Jhon Kim 

- Frontend design
- Testing

# Containerized App Exercise

This app will open a webpage and allows the user to take a picture. Once the picture has been taken a machine learning model will anakyze the picture and return the most prominent emotions based off of the users facial expression. The emotions will then be sent to our database where we will present the user with the most prominent emotions from all of the users who've taken pictures. 

# Running
To run this project enter: `docker-compose up --build`. Once docker has finished running through the steps a text will appear like this: ``ponyo-feels  |  * Running on http://127.0.0.1:5001`` click on the link and it will bring you to the webpage where you can take a picture. Once on the webpage you must allow the page to access your computers camera. If you do not allow the camera or if your computer does not have a camera you sadly will not be able to use this application. 
