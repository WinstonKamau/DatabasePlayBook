""" Module for the INSERTING a user in the Users entity table"""
from logogram.common.execute.execute_command import ExecuteCommand


def insert_row(values):
    """ INSERT user"""
    command = (
        """
        INSERT INTO users(
            password, email, is_superuser, is_staff,
            first_name, last_name, date_joined, last_login)
        VALUES(""" + values + """);
        """
        )
    ExecuteCommand().execute_command(command)
