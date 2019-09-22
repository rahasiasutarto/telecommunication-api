# Olist Test

This application aims to receives calls with details records, and calculates monthly bills for a given telephone number using a HTTP REST API to attend the requirements.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. Install pipenv
2. Clone this repository
3. Install the project dependencies
4. Activate the virtual environment
5. Configure the instance with .env
6. Run the tests

### Installing

What things you need to install the software and how to install them.

```console
git clone git@github.com:pauloh06/ph-work-at-olist.git olist
pipenv install
pipenv shell
cp contrib/env-sample .env
make test
```

## Deployment

These instructions will show you how to deploy this application on a live system using Heroku.

1. Create a heroku app
2. Set the configuration
3. Set SECRET KEY, DEBUG, ALLOWED_HOSTS
4. Set DEBUG false
5. Deploy

```console
heroku create myinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com
git push heroku master
```


## Built With

* [Pipenv](https://docs.pipenv.org/en/latest/) - Dependency Management
* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework
* [Django Rest Framework](https://www.django-rest-framework.org/) - The web framework for building APIs

## Author

* **Paulo Henrique** - [paulohos06](https://github.com/paulohos06)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
