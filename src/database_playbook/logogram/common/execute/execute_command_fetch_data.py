"""
A common command for executing SQL commands on the database, fetching data
from that command execution and returning the data
"""
from logogram.common.execute.execute_command import ExecuteCommand


class ExecuteCommandFetchData(ExecuteCommand):

    def execute_statement(self, cursor, command, connection):
        cursor.execute(command)
        data = cursor.fetchall()
        cursor.close()
        connection.commit()
        return data
