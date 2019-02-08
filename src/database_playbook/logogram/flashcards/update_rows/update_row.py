""" Module for the UPDATING a flashcard in the Flashcards entity table"""
from logogram.common.execute.execute_command import ExecuteCommand


def update_flashcard_row(set_columns, flashcard_id):
    """ UPDATE flashcard"""
    command = (
        """
        UPDATE flashcards
            SET """ + set_columns + """
             WHERE id = """ + flashcard_id
        )
    ExecuteCommand().execute_command(command)
