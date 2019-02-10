"""Test select_user_row application use case for Users entity """
from logogram.tests.base_test import BaseTestCase
from django.core import management
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)
from logogram.flashcards.insert_rows.insert_row import insert_flashcard_row
from logogram.users.insert_rows.insert_rows import insert_user_row
from logogram.flashcards.select_rows.select_rows import select_flashcard_row


class InsertUserTable(BaseTestCase):

    def setUp(self):
        super(InsertUserTable, self).setUp()
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

    def test_create_new_flashcard(self):
        """
        Test that when you pass the name of a flashcard to the
        select_flashard_row method for a flashcard's table that the function
        returnss a flashcard with the specified values.
        """
        data = select_flashcard_row('Computer Science')
        self.assertEqual(data[0][0], 1)
        self.assertEqual(data[0][1], 'Computer Science')
        self.assertEqual(data[0][2], 'Computer Science Flashcard')
        self.assertEqual(data[0][3], 1)
