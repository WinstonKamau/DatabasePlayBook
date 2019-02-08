""" Module for the INSERTING a flashcard in the Flashcards entity table"""
from logogram.common.execute.execute_command import ExecuteCommand


def insert_flashcard_row(values):
    """ INSERT flaschard"""
    command = (
        """
        INSERT INTO flashcards(
            name, description, users)
        VALUES(""" + values + """);
        """
        )
    ExecuteCommand().execute_command(command)
