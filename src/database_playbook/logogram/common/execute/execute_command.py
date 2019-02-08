"""
A common command for executing SQL commands on the database, fetching data
from that command execution and returning the data
"""
import psycopg2
from django.core.management.base import CommandError
from logogram.common.connect_to_database import connect_to_database


class ExecuteCommand(object):

    def execute_command(self, command):
        connection = None
        try:
            (cursor, connection) = connect_to_database()
            return self.execute_statement(cursor, command, connection)
        except (Exception, psycopg2.DatabaseError) as error:
            raise CommandError(error)
        finally:
            if connection is not None:
                connection.close()

    def execute_statement(self, cursor, command, connection):
        cursor.execute(command)
        cursor.close()
        connection.commit()
