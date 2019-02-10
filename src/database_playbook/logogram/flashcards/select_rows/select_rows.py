""" Module for the SELECTING a flashcard in the Flashcards entity table"""
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)


def select_flashcard_row(flashcard):
    """ SELECT flashcard"""
    command = (
        """
        SELECT * FROM flashcards WHERE name = '""" + flashcard + """';
        """
        )
    return ExecuteCommandFetchData().execute_command(command)
