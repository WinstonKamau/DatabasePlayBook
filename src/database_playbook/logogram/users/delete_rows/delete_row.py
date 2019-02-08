""" Module for the DELETING a user in the Users entity table"""
from logogram.common.execute.execute_command import ExecuteCommand


def delete_user_row(user_id):
    """ DELETE user"""
    command = (
        """
        DELETE
        FROM users
        WHERE id = """ + user_id + """;
        """
        )
    ExecuteCommand().execute_command(command)
