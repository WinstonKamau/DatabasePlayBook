"""Test delete_user_row application use case for Users entity """
from logogram.tests.base_test import BaseTestCase
from logogram.users.create_table.create_table import create_user_table
from logogram.users.drop_table.drop_table import drop_user_table
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)
from logogram.users.insert_rows.insert_rows import insert_user_row
from logogram.users.delete_rows.delete_row import delete_user_row


class DeleteUserTable(BaseTestCase):

    def setUp(self):
        super(DeleteUserTable, self).setUp()
        create_user_table()

    def tearDown(self):
        drop_user_table()

    def test_delete_user(self):
        """
        Test that when you pass values to the delete_user_row method for
        a user's table that the function deletes a user with the specified
        value.
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
        data = ExecuteCommandFetchData().execute_command(
            select_user_command)
        self.assertEqual(data[0][2], 'pointer@gmail.com')
        delete_user_row('1')
        data = ExecuteCommandFetchData().execute_command(
            select_user_command)
        self.assertEqual(data, [])
