"""Test the python command droptables """
from django.core import management
from logogram.tests.base_test import BaseTestCase
from logogram.common.execute_command_fetch_data import (
    execute_command_fetch_data)


class DropTables(BaseTestCase):

    def setUp(self):
        super(DropTables, self).setUp()
        management.call_command('createtables')

    def test_create_tables_command(self):
        """
        Test that the drop tables command drops tables.
        """
        management.call_command('droptables')
        command = (
            """
            SELECT tablename
            FROM pg_catalog.pg_tables
            WHERE schemaname = 'public';
            """)
        data = execute_command_fetch_data(command)
        self.assertNotIn(('users',), data)
        self.assertNotIn(('flashcards',), data)
