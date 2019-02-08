"""Test update_user_row application use case for Users entity """
from logogram.tests.base_test import BaseTestCase
from logogram.users.create_table.create_table import create_user_table
from logogram.users.drop_table.drop_table import drop_user_table
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)
from logogram.users.insert_rows.insert_rows import insert_user_row
from logogram.users.update_rows.update_row import update_user_row
import datetime


class UpdateUserTable(BaseTestCase):

    def setUp(self):
        super(UpdateUserTable, self).setUp()
        create_user_table()

    def tearDown(self):
        drop_user_table()

    def test_update_user(self):
        """
        Test that when you pass values to the update_user_row method for
        a user's table that the function updates a user with the specified
        values.
        """
        values = (
            """
            'password', 'pointer@gmail.com', 'false', 'false',
            NULL, NULL, now(), NULL
            """
            )
        insert_user_row(values)
        select_user_command = (
            """
            SELECT * FROM users
            WHERE email = 'pointer@gmail.com';
            """
            )
        data = ExecuteCommandFetchData().execute_command(select_user_command)
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
        set_columns = ("""first_name='Timon', last_name='Pumba'""")
        update_user_row(set_columns, '1')
        select_user_after_update_command = (
            """
            SELECT * FROM users
            WHERE email = 'pointer@gmail.com';
            """
            )
        data = ExecuteCommandFetchData().execute_command(
            select_user_after_update_command)
        self.assertEqual(data[0][5], 'Timon')
        self.assertEqual(data[0][6], 'Pumba')
