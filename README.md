# Food Swipe
<p>Ayda Sholani</p>

## Create envrionment
Create a environment at the project level!
```bash
$ py -m venv .venv
```
### Activate
```bash
$ source .venv/Scripts/activate
```
### Install requirements
```bash
$ pip install -r requirements.txt
```

## Create a .env file 
```python
LOCAL_DATABASE_URI = "database.sqlite"
SECRET_KEY="SECRET_KEY"
SECURITY_PASSWORD_SALT="SECURITY_PASSWORD_SALT"
```

## Create .flaskenv file for environment variables
```python
FLASK_APP = swiper
FLASK_DEBUG = True
```

# Create initial database with tables and data
```bash
$ flask init-db
```

### Run the app with the commando 
```bash
$ flask run 
```
