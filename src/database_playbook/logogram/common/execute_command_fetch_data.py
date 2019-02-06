"""
A common command for executing SQL commands on the database, fetching data
from that command execution and returning the data
"""
import psycopg2
from django.core.management.base import CommandError
from logogram.common.connect_to_database import connect_to_database


def execute_command_fetch_data(command):
    connection = None
    try:
        (cursor, connection) = connect_to_database()
        cursor.execute(command)
        data = cursor.fetchall()
        cursor.close()
        connection.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        raise CommandError(error)
    finally:
        if connection is not None:
            connection.close()
