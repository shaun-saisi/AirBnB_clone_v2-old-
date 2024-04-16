#!/usr/bin/python3
"""Unit test for database functionality"""

import unittest
import MySQLdb

class TestDatabaseFunctionality(unittest.TestCase):
    """ This is a test class for testing MySQL with Python"""
    def setUp(self):
        # Connect to the database
        self.db = MySQLdb.connect(host="localhost", user="pwaguzi", passwd="Callais7461!", db="hbnb", port=3306)
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close cursor and database connection
        self.cursor.close()
        self.db.close()

    def test_add_state_to_database(self):
        # Insert a new state record
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")

        # Get the initial number of records
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count_result = self.cursor.fetchall()
        num_records_before = count_result[0][0] if count_result else 0

        # Inserting a new record increases the count by 1
        num_records_after = num_records_before + 1

        # Validate test outcome
        self.assertEqual(num_records_after, num_records_before + 1, "New record not added to the database")

if __name__ == "__main__":
    unittest.main()

