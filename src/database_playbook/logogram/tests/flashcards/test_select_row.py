"""Test select_flashcard_row application use case for Flashcards entity """
from logogram.tests.base_test import BaseTestCase
from logogram.users.create_table.create_table import create_user_table
from logogram.users.drop_table.drop_table import drop_user_table
from logogram.users.insert_rows.insert_rows import insert_user_row
from logogram.users.select_rows.select_rows import select_user_row
import datetime


class SelecttUserTable(BaseTestCase):

    def setUp(self):
        super(SelecttUserTable, self).setUp()
        create_user_table()

    def tearDown(self):
        drop_user_table()

    def test_select_user(self):
        """
        Test that when you pass an email to the select_user_row method for a
        user's table that the function returns a user with his detailed values.
        """
        values = (
            """
            'password', 'pointer@gmail.com', 'false', 'false',
            NULL, NULL, now(), NULL
            """
            )
        insert_user_row(values)
        data = select_user_row('pointer@gmail.com')
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.assertEqual(data[0][0], 1)
        self.assertEqual(data[0][1], 'password')
        self.assertEqual(data[0][2], 'pointer@gmail.com')
        self.assertEqual(data[0][3], False)
        self.assertEqual(data[0][4], False)
        self.assertEqual(data[0][5], None)
        self.assertEqual(data[0][6], None)
        self.assertEqual(str(data[0][7]), date)
        self.assertEqual(data[0][8], None)
