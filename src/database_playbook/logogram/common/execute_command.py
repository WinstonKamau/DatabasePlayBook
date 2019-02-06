""" A common command for executing SQL commands on the database"""
import psycopg2
from django.core.management.base import CommandError
from logogram.common.connect_to_database import connect_to_database


def execute_command(command):
    connection = None
    try:
        (cursor, connection) = connect_to_database()
        cursor.execute(command)
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        raise CommandError(error)
    finally:
        if connection is not None:
            connection.close()
