""" Module for dropping the Users entity schema."""
from logogram.common.execute.execute_command import ExecuteCommand


def drop_user_table():
    """ Drop users table in the PostgreSQL database"""
    command = (
        """
        DROP Table users;
        """)
    ExecuteCommand().execute_command(command)
