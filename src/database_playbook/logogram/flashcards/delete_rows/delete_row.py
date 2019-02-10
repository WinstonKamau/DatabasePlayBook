""" Module for the DELETING a flashcard in the Flashcards entity table"""
from logogram.common.execute.execute_command import ExecuteCommand


def delete_flashcard_row(flashcard_id):
    """ DELETE flashcard"""
    command = (
        """
        DELETE
        FROM flashcards
        WHERE id = """ + flashcard_id + """;
        """
        )
    ExecuteCommand().execute_command(command)
