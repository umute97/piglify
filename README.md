# Piglify - Managing the life of 3 little piglets since 2023.
This is a leisure project I have started to get familiar with the new vue 3 + TS tooling but it turned out to be quite the useful tool for my flatshare, so I made it public.

- [Piglify - Managing the life of 3 little piglets since 2023.](#piglify---managing-the-life-of-3-little-piglets-since-2023)
  - [Intro](#intro)
  - [Installation](#installation)
    - [Front End](#front-end)
    - [Back End](#back-end)
  - [About the Docker files in this repo](#about-the-docker-files-in-this-repo)
## Intro

The stack is composed of 
 - [`Django`](https://www.djangoproject.com/) storing three tables
   - `Users` - storing all flatmates and their data
   - `Chores` - storing all chores and their description
   - `Groceries` - storing a list of groceries to buy.
 - [`Vue 3 (TS)`](https://vuejs.org) with [`naive-ui`](https://naiveui.com) serving as the graphical user interface. It contains
   - a *Chores* view, displaying the chores of all flatmates and a quick tutorial for each chore, as well as a button to mark it as done
   - a *Groceries* view, listing all groceries that have or haven't been bought yet as well as a quick tutorial on how to add a new item.

## Installation
I'll be honest with you: I lack experience on the whole deployment process, so everything on this end is a mess.

### Front End
Change into the project's root and run
```bash
npm i
```
to install all dependencies.
To start a development server, run
```bash
npm run dev
```
You need an `.env` file that specifies a variable called `VITE_BACKEND_BASE_URL` and set it to the api endpoint of the Django app (will explain this in the Back End section).

### Back End
**Python >=3.9 is required.**

>**Without a virtual environment (not recommended)**

Change into the `backend` folder and install all dependencies with
```bash
pip install --user -r requirements.txt
```

>**With a virtual environment**

If you don't like to clutter your site-packages, just create a `venv`:
```bash
python -m venv <venv-name>
```
and activate it by running
```bash
source <venv-name>/bin/activate<.alt-shell>
```
Installing the dependencies should work by running
```bash
pip install -r requirements.txt
```
You will need a `.env` file that looks like
```ini
DEBUG=0
DJANGO_ALLOWED_HOSTS=<the ip your api is running on and associated aliases>
SECRET_KEY=<a long-ass secret key you cannot tell a soul or else>
```
Initialize the database with
```bash
python manage.py migrate
```
Go ahead and edit the `backend/fixtures` to your liking, adding the chores and users you require and apply them with
```bash
python manage.py loaddata fixtures/chores.yaml
python manage.py loaddata fixtures/users.yaml
```
in the `backend` directory.
Finally, we can run the development server by executing
```bash
python manage.py runserver
```

## About the Docker files in this repo
Those were for local testing only. They won't do you any good other than serving as a template.