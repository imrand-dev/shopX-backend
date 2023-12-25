# Welcome to ShopX Ecommerce

## Run this project locally

* clone the repo `https://github.com/imrand-dev/shopX-backend.git`
* enter `cd shopX-backend`
* create virtual environment `pipenv install`
* activate the virtual environment `pipenv shell`
* enter `cd projectile`
* edit the `.env-example` file and rename it `.env`
* migrate the project `python manage.py migrate`
* run the server `python manage.py runserver`

## Generate random SECRET_KEY 

```py
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```