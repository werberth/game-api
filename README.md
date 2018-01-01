# Game API

Project example from the book [Building RESTful Python Web Services by Gastón C. Hillar.](https://www.packtpub.com/application-development/building-restful-python-web-services)


## Installation

```
git clone git@github.com:werberth/scrum-api.git gameapi
cd gameapi
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

 - Rename the example.env file to .env and set the ```DEBUB``` variable to ```True```.
 - If you want to use PostgreSQL, replace the username for the database username, the password for the user's password, and database_name for the database name. Example:

 	```DATABASE_URL='postgres://username:password@localhost/database_name'```

 	Taking as an example a database with name "game_database", and a user with username "admin" and password "12345":

 	```DATABASE_URL='postgres://admin:12345@localhost/game_database```
 - Run ```python manage.py runserver``` 

 ## Using the API

 ### URLs

- **Game Categories Routes** 
	- ```game-categories/$ [name='gamecategory-list']```
	- ```game-categories/(?P<pk>[0-9]+)/$ [name='gamecategory-detail']```
- **Games Routes**
	- ```games/$ [name='game-list']```
	- ```games/(?P<pk>[0-9]+)/$ [name='game-detail']```
- **Players Routes**
	- ```players/$ [name='player-list']```
	- ```players/(?P<pk>[0-9]+)/$ [name='player-detail']```
- **Players Score Routes**
	- ```player-scores/$ [name='playerscore-list']```
	- ```player-scores/(?P<pk>[0-9]+)/$ [name='playerscore-detail']```
- **Users Routes**
	- ```users/$ [name='user-list']```
	- ```users/(?P<pk>[0-9]+)/$ [name='user-detail']```