# Emerging Economies

## Introduction
This website compares a few key economic and financial indicators for selected emerging economies, including India. These indicators document the countries' economic performance, financial markets, financial access, and human development trends.

## Backend Descriptions
We have created the backend using Python's Django Framework. The backend is responsible for fetching data from open source APIs, namely IMF, World Bank's and UNDP, and cleaning the data thoroughly before sending it to the frontend.
#### Libraries and Framework used (Backend):
1) **django** (Framework) [Link](https://docs.djangoproject.com/en/4.0/)
2) **asgiref** (Library) [Link](https://pypi.org/project/asgiref/)
3) **django-environ** (Library) [Link](https://django-environ.readthedocs.io/en/latest/)
4) **django-heroku** (Library) [Link](https://devcenter.heroku.com/articles/django-app-configuration)
5) **idna** (Library) [Link](https://pypi.org/project/idna/)
6) **python-dateutil** (Library) [Link](https://pypi.org/project/python-dateutil/)
7) **requests** (Library) [Link](https://pypi.org/project/requests/)
8) **tzdata** (Library) [Link](https://pypi.org/project/tzdata/)
9) **urllib3** (Library) [Link](https://pypi.org/project/urllib3/)
10) **waitress** (Library) [Link](https://pypi.org/project/waitress/)
11) **whitenoise** (Library) [Link](https://whitenoise.evans.io/en/stable/)

## Frontend Descriptions
The frontend is created using HTML, CSS, JavaScript, Bootstrap and Plotly.js. HTML, CSS, JavaScript and Bootstrap are responsible for the page's layout. Plotly.js is used to render the graphs.
#### Libraries and Framework used (Frontend):
1) **Bootstrap** (CSS Framework) [Link](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
2) **Plotly.js** (JS Library) [Link](https://plotly.com/javascript/)
3) **jQuery** (JS Library) [Link](https://jquery.com/)
4) **Propper.js** (JS Library) [Link](https://popper.js.org/docs/v2/)
5) **Font-Awesome** (Icon Library & Toolkit) [Link](https://fontawesome.com/icons)

## Server Descriptions
The Web App is hosted on **Heroku Server** ( Heroku is a container-based cloud Platform as a Service **(PaaS)**. It is used for deploying, managing, and scaling modern apps. This platform is flexible and easy to use. )

We are using the **Free Tier Plan** of the Heroku server. As this server is free, it has some limitations, like, It cannot serve many users at a time, but the major challenge is that apps on the free plan **"go to sleep"** after a period of inactivity.

Heroku Free Tier shuts down app containers to free up system resources. However, the app **"wakes up"** with a delayed response of some seconds once it gets a web request from users. So it's **not recommended** to use this accessible server for **Commercial Purposes.**

## Github Link
Emerging-Economies : [Source Code Link](https://github.com/ABHISHEK-SIN-GH/Emerging-Economies)

## Folder Structure and File Descriptions
### EcoFinWeb/Code/Staticfiles
1. **CSS Files**
(a) Bootstrap.css [ Contains predefined Bootstrap CSS classes ]\
(b) style.css [ Contains custom made CSS classes ]

2. **Image Files**
(a) loader.gif [ The gif that is showed while the page is loading. ]

3. **JavaScript Files**
(a) plotly.js [ Custom made plotting library for the charts ]\
(b) Remaining files are source code for the frontend libraries used.

### EcoFinWeb/Code/Templates
1. **header.html**
(a) We are including all the libraries required, in this html file

2. **dashboard.html**
(a) This is the main html file, which contains the entire frontend code for our website
(b) This file also contains the plotly.js functions which render the graphs

### EcoFinWeb/Code/Django Source Code
1. **EcoFin** [ Contains all necessary files and folders of our Django Web App ]
2. **EcoFinWeb** [ Contains all configuration files of our Django Project ]
3. **manage.py** [ Command line utility provides various necessary commands required to run the Django project ]
4. **requirements.txt** [ Contains the names of all the libraries that our Django project is dependent on. ]

### Django Source Code/EcoFin
1. **urls.py** [ Contains the router logic ]
2. **pycache, migrations, apps.py** [ These are auto generated Django files ]
3. **views.py**
(a) This is the main file where the backend logic is implemented\
(b) we are requesting data from the APIs, cleaning the received data, and then sending the data to the frontend using this file.\
(c) we have made 4 functions for fetching data from various APIs\
      1. **hrdoAPI()** : handles requests to the UNDP API\
      2. **imfAPI()** : handles requests to the IMF API\
      3. **wbAPI()** : handles requests to the World Bank API\
      4. **home()** : handles all the above APIs together



