""" Module for dropping the Flashcards entity schema."""
from logogram.common.execute.execute_command import ExecuteCommand


def drop_flashcards_table():
    """ Drop flashcards table in the PostgreSQL database"""
    command = (
        """
        DROP Table flashcards;
        """)
    ExecuteCommand().execute_command(command)
