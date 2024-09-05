# Piglify - Managing the life of 3 little piglets since 2023.
This is a leisure project I have started to get familiar with the new vue 3 + TS tooling but it turned out to be quite the useful tool for my flatshare, so I made it public.

  - [Intro](#intro)
  - [Installation](#installation)

Currently hosted on my shitty little RPi 2... [Website (for you, just and auth wall)](https://piglify.duckdns.org)

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
First, go ahead and edit the `backend/fixtures` to your liking, adding the chores and users you require and apply them with in the `backend` directory.

From here on out, everything is dockerized! So, just build the images:
```bash
docker build . -t piglify-frontend
cd backend
docker build . -t piglify-backend
```

You will need a file called `.env` in this app's root that exposes the following variables:
```ini
DEBUG=0 or 1, depending on if you want debugging features or not

DJANGO_ALLOWED_HOSTS=<the ip your api is running on and associated aliases, incl. localhost for the default setup>

SECRET_KEY=<a long-ass secret key you cannot tell a soul or else>

VITE_BACKEND_BASE_URL=http://localhost:8000/piglify
```

After adjusting these values to your liking, let's fire it up with
```bash
docker compose up -d
```
