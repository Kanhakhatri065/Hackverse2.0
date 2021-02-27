# Hackverse2.0

## Distributed Compiler
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)     ![image](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)      ![image](https://img.shields.io/badge/firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=white)

[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://GitHub.com/Naereen/)

![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

### Description
>  Have a low powered laptop?, Want to compile a huge project?, Stuck at home?, don't worry we got you covered !
> 
Distributed compiler aims to achieve compilation of programs and projects on the distributed network. 
All user needs to do is to share his code(by providing GitHub link) and request for compilation.
As soon as the idle hosts detect that a new job has been added to the queue, all the idle hosts download the program (via github) simultaneously and try to build it.
The host with the most computation power wins the race and pings the server that the job is done and is rewarded.

> More the computation power ==> Faster Builds ==> More Revenue for 'miners'.

> Faster Builds ==> Happy User ==> More Users on the Platform.

As you can see on a long run it is a win-win situation !!

Our project comes under the track "Let's go contactless".

### Tech Stack
1. Python ( requests, GitPython, zip )
2. Flask
3. JS
4. Firebase API
5. Heroku

### Libraries and Dependencies
All the required libraries and dependencies are
mentioned in [requirements.txt](https://github.com/Kanhakhatri065/Hackverse2.0/blob/main/requirements.txt)

### Installation Steps
#### Server Deployment - 
1. ```heruko login```
2. ```git init```
3. ```git add .```
4. ```git commit -m "deploying server"```
5. ```git push heroku master```
#### Host Machine Setup -
1. ```pip install -r requirements.txt```
2. ```python3 back_end_api_caller.py```

### Declaration Of Previous Work
This repository is a new project and is being presented as a hack by Team Babayaga
in Hackverse2.0 hackathon.

### Members of the Team
1. Divakar Lakhera
2. Kanha Khatri
3. Pankaj Kumar
