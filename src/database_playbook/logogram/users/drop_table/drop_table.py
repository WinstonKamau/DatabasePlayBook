""" Module for dropping the Users entity schema."""
from logogram.common.execute_command import execute_command


def drop_user_table():
    """ Drop users table in the PostgreSQL database"""
    command = (
        """
        DROP Table users;
        """)
    execute_command(command)
