"""Test delete_flashcards_row application use case for Flashcards entity"""
from logogram.tests.base_test import BaseTestCase
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)
from logogram.users.insert_rows.insert_rows import insert_user_row
from logogram.flashcards.insert_rows.insert_row import insert_flashcard_row
from django.core import management
from logogram.flashcards.delete_rows.delete_row import delete_flashcard_row


class DeleteFlashcardsTable(BaseTestCase):

    def setUp(self):
        super(DeleteFlashcardsTable, self).setUp()
        management.call_command('createtables')

    def tearDown(self):
        management.call_command('droptables')

    def test_delete_flashcard(self):
        """
        Test that when you pass values to the delete_flashcard_row method for
        a user's table that the function deletes a flashcard with the specified
        value.
        """
        values = (
            """
            'password', 'pointer@gmail.com', 'false', 'false',
            NULL, NULL, now(), NULL
            """
            )
        insert_user_row(values)
        values = (
            """
            'Computer Science', 'Computer Science Flashcard', 1
            """
            )
        insert_flashcard_row(values)
        select_flashcard_command = (
            """
            SELECT * FROM flashcards
            WHERE id = 1;
            """
            )
        before_delete_data = ExecuteCommandFetchData().execute_command(
            select_flashcard_command)
        self.assertEqual(before_delete_data[0][1], 'Computer Science')
        delete_flashcard_row('1')
        after_delete_data = ExecuteCommandFetchData().execute_command(
            select_flashcard_command)
        self.assertEqual(after_delete_data, [])
