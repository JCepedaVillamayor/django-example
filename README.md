# django-example

This repository is intended to show how to use pagination in Django

## Requirements

- Docker
- Docker-Compose

## How to run the application

1. Go to the repository folder (`cd <path/to/repository`>)
2. Build the files (`docker-compose build`)
3. Migrate the database (`docker-compose run web python manage.py migrate`)
4. (Optional) Generate sample users to show how the application works (100, for example)

   `docker-compose run web python manage.py generate_fake_data 100`

5. start the application. `docker-compose up`

## Testing

This application uses pytest for testing. The following things have been tested:

- Address creation / field constraints
- Pagination
- Page range

If you want to execute the tests, you must write:

- `docker-compose run web pytest`

## Additional information

Although the application works well, the users and passwords are visible inside the code. If you want to deploy the application in the cloud (aws, gcloud, your own vps, etc.) you must use your own passwords. This program facilitates this task by having a command to generate sample users and passwords. You can type `make generate-sample-envs` to generate sample env files inside `.envs` folder. Then. you will have the following files with this values:

.envs/.web

```ini
SECRET_KEY=secret
DJANGO_SETTINGS_MODULE=config.settings.local
```

.envs/.db

```ini
POSTGRES_USER=sample
POSTGRES_PASSWORD=sample
POSTGRES_DB=sample
```

It is recommended to change the values and put your own ones, because they are insecure since they are visible
