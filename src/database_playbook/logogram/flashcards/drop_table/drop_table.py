""" Module for dropping the Flashcards entity schema."""
from logogram.common.execute_command import execute_command


def drop_flashcards_table():
    """ Drop flashcards table in the PostgreSQL database"""
    command = (
        """
        DROP Table flashcards;
        """)
    execute_command(command)
