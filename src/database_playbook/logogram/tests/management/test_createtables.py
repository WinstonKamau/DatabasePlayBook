"""Test the python command createtables """
from django.core import management
from logogram.tests.base_test import BaseTestCase
from logogram.common.execute.execute_command_fetch_data import (
    ExecuteCommandFetchData)


class CreateTables(BaseTestCase):

    def setUp(self):
        super(CreateTables, self).setUp()

    def tearDown(self):
        management.call_command('droptables')

    def test_create_tables_command(self):
        """
        Test that the create tables command creates tables.
        """
        management.call_command('createtables')
        command = (
            """
            SELECT tablename
            FROM pg_catalog.pg_tables
            WHERE schemaname = 'public';
            """)
        data = ExecuteCommandFetchData().execute_command(command)
        self.assertIn(('users',), data)
        self.assertIn(('flashcards',), data)
