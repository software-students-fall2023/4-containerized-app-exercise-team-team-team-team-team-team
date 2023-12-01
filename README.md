[![check lint and format](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/lint.yml/badge.svg)](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/lint.yml)
[![CI/CD](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/python-app.yml/badge.svg)](https://github.com/software-students-fall2023/4-containerized-app-exercise-team-team-team-team-team-team/actions/workflows/python-app.yml)


# Team Members
`alexh212`- Alex Hmitti

`as13909` - Aaron Stein :)

`Rafinator123` - Rafael Nadal-Scala

`jk021227` - Jhon Kim 

# Concept

Ponyo Feels is an emotion recognition app that allows users to take a selfie and quickly have their facial expressions analyzed by a machine learning model. 

Using [Hume AI's facial expression model](https://hume.ai/products/facial-expression-model/), this analysis identifies and reports the most prominent emotions displayed in a selfie. 

In addition to recognizing emotions, Ponyo Feels currently suggests Spotify songs that match the identified emotion and has the capacity to expand media recommendations to include other content types reflecting the user's emotion. 

These emotions are then stored in a database, allowing the app to provide users with insights into the most common emotions experienced by all its users.

# Installation

To get started, clone the repository to your local machine and navigate to the project's directory. 

First you need to create an account on [hume](https://www.hume.ai). Once you've created an account on the left hand side of the screen you will see a button that says `API Keys` with a picture of a key next to it. Click on that button and copy your personal API Token. Reminder, this is a personal and private API token that is unique to you, do not share it with others! 

Inside of the `4-containerized-app-exercise-team-team-team-team-team-team/src/` create a file called `config.json` inside of that file you will copy and paste the folllowing:

```
{
    "api_token": "YOUR_API_TOKEN_HERE"
}
```

Replace the text `YOUR_API_TOKEN_HERE` leaving the quotes. When done save the file and exit it. 

Once done with that you need to go to the root directory `4-containerized-app-exercise-team-team-team-team-team-team/` create a file called `.env` and in that file copy and paste the following text: 
`DATABASE_CONNECTION_STRING = "mongodb+srv://jaar2023:me8rd2iS73YJLTfW@recipes01.ajqwb7q.mongodb.net/"` 
Once done save and close the file. 

Finally, ensure Docker is installed on your machine. If not, download and install it [here](https://www.docker.com/products/docker-desktop/).


# Usage
Begin the application by running the following command: `docker-compose up --build`

You'll see a series of1`` messages appearing, indicating the progress of the build process.

Once the build process is complete, you should see the following lines, indicating that the application is up and running:

```bash

ponyo-feels  |  * Serving Flask app 'web_app'
ponyo-feels  |  * Debug mode: off
ponyo-feels  | INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
ponyo-feels  |  * Running on all addresses (0.0.0.0)
ponyo-feels  |  * Running on http://127.0.0.1:5001
ponyo-feels  |  * Running on http://172.18.0.3:5001
ponyo-feels  | INFO:werkzeug:Press CTRL+C to quit

```

Open `http://127.0.0.1:5001` in your browser and click the button on the main page to reach the webcam interface. 

Make sure to grant camera access to the website and then click the button to have your selfie analyzed.
