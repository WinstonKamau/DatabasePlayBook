"""Test insert_rows application use case for Users entity """
from logogram.tests.base_test import BaseTestCase
from django.core import management
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)
from logogram.flashcards.insert_rows.insert_row import insert_row
from logogram.users.insert_rows.insert_rows import (
    insert_row as insert_user_row)


class CreateUserTable(BaseTestCase):

    def setUp(self):
        super(CreateUserTable, self).setUp()
        management.call_command('createtables')
        values = (
            """
            'password', 'pointer@gmail.com', 'false', 'false',
            NULL, NULL, now(), NULL
            """
            )
        insert_user_row(values)

    def tearDown(self):
        management.call_command('droptables')

    def test_create_new_flashcard(self):
        """
        Test that when you pass values to the insert_row method for a
        flashcard's table that the function creates a flashcard with the
        specified values.
        """
        values = (
            """
            'Computer Science', 'Computer Science Flashcard', 1
            """
            )
        insert_row(values)
        select_user_command = (
            """
            SELECT * FROM flashcards
            WHERE name = 'Computer Science';
            """
            )
        data = ExecuteCommandFetchData().execute_command(select_user_command)
        self.assertEqual(data[0][0], 1)
        self.assertEqual(data[0][1], 'Computer Science')
        self.assertEqual(data[0][2], 'Computer Science Flashcard')
        self.assertEqual(data[0][3], 1)
