"""Test entity application for Words entity """
from logogram.tests.base_test import BaseTestCase
from logogram.common.connect_to_database import (
    check_variables, fetch_database_config_variables, connect_to_database)
from django.core.management.base import CommandError
from django.test import override_settings


class DatabaseConnection(BaseTestCase):

    def setUp(self):
        super(DatabaseConnection, self).setUp()

    def test_check_variables(self):
        """
        Test that the check_variables method will raise an error if the second
        argument provided is None and not the string "password".
        """
        # calling with the string password raises no error
        check_variables("password", None)
        with self.assertRaises(CommandError):
            check_variables("user", None)

    @override_settings(DATABASES={'default': {
        'ENGINE': 'django.db.backends.postgresql', 'NAME': 'mandy_db',
        'USER': 'mandy', 'PASSWORD': 'mandy_password', 'HOST': 'localhost',
        'PORT': '5432', 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True,
        'CONN_MAX_AGE': 0, 'OPTIONS': {}, 'TIME_ZONE': None, 'TEST': {
            'CHARSET': None, 'COLLATION': None, 'NAME': None, 'MIRROR': None
            }}})
    def test_fetch_database_config_variables(self):
        """
        Test a successul return of the database credentials.
        """
        db_variables = fetch_database_config_variables()
        self.assertEqual(db_variables['host'], 'localhost')
        self.assertEqual(db_variables['database'], 'mandy_db')
        self.assertEqual(db_variables['user'], 'mandy')
        self.assertEqual(db_variables['password'], 'mandy_password')

    @override_settings(DATABASES={'default': {
        'ENGINE': 'django.db.backends.postgresql', 'NAME': 'mandy_db',
        'USER': '', 'PASSWORD': 'mandy_password', 'HOST': 'localhost',
        'PORT': '5432', 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True,
        'CONN_MAX_AGE': 0, 'OPTIONS': {}, 'TIME_ZONE': None, 'TEST': {
            'CHARSET': None, 'COLLATION': None, 'NAME': None, 'MIRROR': None
            }}})
    def test_fetch_database_config_variables_fail(self):
        """
        Test lack of a database credential such as user will raise an error
        """
        with self.assertRaises(CommandError):
            fetch_database_config_variables()

    def test_cursor_returned_executes(self):
        """
        Test that the cursor returned when executed will return some
        information
        """
        cursor = connect_to_database()
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        cursor.close
        self.assertIn('postgre', str(db_version).lower())

    @override_settings(DATABASES={'default': {
        'ENGINE': 'django.db.backends.postgresql', 'NAME': 'mandy_db',
        'USER': 'mandy', 'PASSWORD': 'mandy_password', 'HOST': 'localhost',
        'PORT': '5432', 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True,
        'CONN_MAX_AGE': 0, 'OPTIONS': {}, 'TIME_ZONE': None, 'TEST': {
            'CHARSET': None, 'COLLATION': None, 'NAME': None, 'MIRROR': None
            }}})
    def test_error_raised_wrong_credentials(self):
        """
        Test that an error is raised if the credentials are wrong
        """
        with self.assertRaises(CommandError):
            connect_to_database()
