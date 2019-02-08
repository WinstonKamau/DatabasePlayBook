""" Module for the UPDATING a user in the Users entity table"""
from logogram.common.execute.execute_command import ExecuteCommand


def update_user_row(set_columns, user_id):
    """ UPDATE user"""
    command = (
        """
        UPDATE users
            SET """ + set_columns + """
             WHERE id = """ + user_id
        )
    ExecuteCommand().execute_command(command)
