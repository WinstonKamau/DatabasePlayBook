""" Module for the SELECTING a user in the Users entity table"""
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)


def select_user_row(email):
    """ SELECT user"""
    command = (
        """
        SELECT * FROM users WHERE email = '""" + email + """';
        """
        )
    return ExecuteCommandFetchData().execute_command(command)
