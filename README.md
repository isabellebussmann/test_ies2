# Test IES2

## 📋 Project Description
<p align="center">This project was thought of as a version of an educational system while I was learning about the Django REST framework with caching (local or via Redis). So, to give continuity to this, I used some segments that could be registered within a school, such as students, courses, exams, etc., forming a data structure that can be linked with each other, making this API more efficient.</p>
<p align="center">👀 You can see the result <a href="https://test-ies2.herokuapp.com/">here.</a></p>
<h4 align="center">🚧 Status: Finished 🚧</h4>

<p align="center">
 <a href="#features">Features</a> • 
 <a href="#-how-it-works">How it works</a> • 
 <a href="#-tech-stack">Tech Stack</a> • 
 <a href="#author">Author</a> 
</p>

---

## Features

- [x] Educational entities can register on the API:
   - [x] students
   - [x] courses
   - [x] enrollment
   - [x] teachers
   - [x] exams
   - [x] questions
   - [x] in addition to selecting one or more items to correlate exams and questions

---

## 🚀 How it works

You have two options to view the project:
1. You can acess heroku - https://test-ies2.herokuapp.com/
2. You can clone the project (follow the steps below)

### Pre-requisites

Before you begin, you will need to have [Python3.9](https://www.python.org/).

#### Backend (API)

* To download the project follow the instructions below, install the dependencies and start the server:

```bash

# Clone this repository
$ git clone git@github.com:isabellebussmann/test_ies2.git

# Access the project folder cmd/terminal
$ cd test_ies2

# go to the setup folder
$ cd setup

# install the dependencies (requirements.txt)
$ pip install -r requirements.txt

# Run the application
$ python manage.py runserver

# The server will start at port: 8000 - go to http://localhost:8000

```
---

## 🛠 Tech Stack

The following tools and frameworks were used in the construction of the project:
<!--examples-->
- [Python](https://www.python.org/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Redis](https://redis.io/) (optional, in the settings)

---

## Author

👩🏻‍💻 Isabelle dos Santos Bussmann

[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/isabelle-bussmann-445b25138/)](https://www.linkedin.com/in/isabelle-bussmann-445b25138/)
[![Telegram Badge](https://img.shields.io/badge/-Telegram-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=telegram&logoColor=white&link=https://t.me/isabellebussmann)](https://t.me/isabellebussmann)
[![Hotmail Badge](https://img.shields.io/badge/-Hotmail-0078D4?style=flat-square&logo=microsoft-outlook&logoColor=white&link=mailto:isabellebussmann@hotmail.com)](mailto:isabellebussmann@hotmail.com)

