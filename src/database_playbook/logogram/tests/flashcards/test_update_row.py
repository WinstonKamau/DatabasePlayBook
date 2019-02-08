"""Test update_user_row application use case for Users entity """
from logogram.tests.base_test import BaseTestCase
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)
from logogram.users.insert_rows.insert_rows import insert_user_row
from logogram.flashcards.insert_rows.insert_row import insert_flashcard_row
from logogram.flashcards.update_rows.update_row import update_flashcard_row
from django.core import management


class UpdateFlashcardsTable(BaseTestCase):

    def setUp(self):
        super(UpdateFlashcardsTable, self).setUp()
        management.call_command('createtables')
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

    def tearDown(self):
        management.call_command('droptables')

    def test_update_flashcard(self):
        """
        Test that when you pass values to the update_flashcard_row method for
        a user's table that the function updates a user with the specified
        values.
        """
        set_columns = ("""name='History', description='History Courses'""")
        update_flashcard_row(set_columns, '1')
        select_flashcard_after_update_command = (
            """
            SELECT * FROM flashcards
            WHERE name = 'History';
            """
            )
        data = ExecuteCommandFetchData().execute_command(
            select_flashcard_after_update_command)
        self.assertEqual(data[0][0], 1)
        self.assertEqual(data[0][1], 'History')
        self.assertEqual(data[0][2], 'History Courses')
        self.assertEqual(data[0][3], 1)
