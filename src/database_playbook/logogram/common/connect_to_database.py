import psycopg2
from django.conf import settings
from django.core.management.base import CommandError


def connect_to_database():
    """Connect to the PostgreSQL database server"""
    connection = None
    try:
        db = fetch_database_config_variables()
        connection = psycopg2.connect(**db)
        cursor = connection.cursor()
        return cursor
    except (Exception, psycopg2.DatabaseError) as error:
        raise CommandError(error)


def fetch_database_config_variables():
    """
    Fetch database config variables for psycopg2 connecgtion
    """
    psycopg2_db_keys = ["host", "database", "user", "password"]
    db = {}
    for key in psycopg2_db_keys:
        database_credential = settings.DATABASES.get(
            'default').get(key.upper())
        if key == "database":
            database_credential = settings.DATABASES.get(
                'default').get('NAME')
            check_variables("name", database_credential)
        else:
            check_variables(key, database_credential)
        db.update({key: database_credential})
    return db


def check_variables(key, database_credential):
    """
    Check that all database credentatials for each pyscopg2 is granted
    except for the password.
    """
    if not database_credential and key != "password":
        raise CommandError("The database {} was not provided".format(key))
