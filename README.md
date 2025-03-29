# Tractice (Track + Practice)

This is the server side repository made with Django. The client code is in a seperate repository that can be viewed [here](https://github.com/zmosher4/tractice_client).

I made this project, as a working musician, for people like myself to use to keep track of their upcoming shows and schedule time to practice. This is a web application that allows users to add upcoming shows (or performances), into a calendar. Once a user has added a show, they can then add practice sessions that are tied to specific shows. Users can add songs to the set list that they need to practice in these practice sessions, and keep notes here on what they will need to prepare for a performance.

To run this project locally on your machine, follow these steps:

1. Run `pipenv install` to install the dependencies needed for this project.
2. Run `pipenv shell` to activate a virtual environment.
3. If you'd like to use `venv` instead of `pipenv`, then follow these steps:
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```
4. To run migrations and load fixtures, run `./seed_data.sh`.
5. Start the development server with `python manage.py runserver`.
