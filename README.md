# Weather app

My final project - Weather app

## Features
- sending emails (user verification)
- information about weather


## Installation

Linux:

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
pip install requirements.txt
```

## Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Testing Emails

To output an account verification message to a console use this in your settings.py file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
To send order confirmations use:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

## Built With
- Django
<<<<<<< HEAD
- PostgreSQL
=======
- PostgresSQL
>>>>>>> 01f0d279f9e22e319456cda0ec9e6e05a04d9c51
