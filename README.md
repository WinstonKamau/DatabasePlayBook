# DatabasePlayBook [![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)[![CircleCI](https://circleci.com/gh/WinstonKamau/DatabasePlayBook.svg?style=svg)](https://circleci.com/gh/WinstonKamau/DatabasePlayBook)[![Coverage Status](https://coveralls.io/repos/github/WinstonKamau/DatabasePlayBook/badge.svg)](https://coveralls.io/github/WinstonKamau/DatabasePlayBook)

DatabasePlaybook is a simple playbook, that showcases database queries that are usually run on applications.

# Description

The playbook implements the following functionalities in regards to database operations:

- It creates a users and flashcards table on a Postgres database.
- It drops the users and flashcards table on a Postgres database.
- It inserts rows to the users and flashcards tables.
- It updates rows to the users and flashcards tables.
- It deletes rows to the users and flashcards tables based on a selection of the user's id and flashcard's id respectively.
- It selects all rows in the users and flashcards tables.
- It tests each of the operations above.


## Documentation

## Setup

### Dependencies

This project uses the following technologies:

| **Version**     | **Packages/Languages/Frameworks**                              |
|-----------------|----------------------------------------------------------------|
|`3.7`            | [Python](https://www.python.org/downloads/release/python-370/) |
|`2018.10.13`     | [Pipenv](https://pypi.org/project/pipenv/2018.10.13/)          |
|`2.7.7`          | [psycopg2](http://initd.org/psycopg/docs/)                     |
|`2.1.5`          | [Django](https://www.djangoproject.com/)                       |
|`11.1`           | [Postgres](https://www.postgresql.org/docs/11/index.html)      |


Other application dependencies can be found [here](Pipfile)

### Getting Started

#### Clone this repository, and change directory into the DatabasePlayBook folder
    git clone https://github.com/WinstonKamau/DatabasePlayBook.git
    cd DatabasePlayBook
#### Install application dependencies
    pipenv --three install -d
#### Create a database on your local Postgres
    createdb <name of database>
#### Create a .env file on the root of your repository and add the secrets below.
    export DATABASE_NAME=<name of database>
    export DATABASE_USER=<database user>
    export DATABASE_PASSWORD=<database password>
    export POSTGRES_IP=localhost
    export DATABASE_PORT=5432
#### Create tables on the database
    cd src/database_playbook
    pipenv run python manage.py createtables
#### Drop tables on the database
    cd src/database_playbook
    pipenv run python manage.py droptables

## Testing

#### Run tests
    cd src/database_playbook
    pipenv run python manage.py test
#### Run tests with coverage
    cd src/database_playbook
    pipenv run coverage run --rcfile=../../.coveragerc manage.py test
    pipenv run coverage report --rcfile=../../.coveragerc
