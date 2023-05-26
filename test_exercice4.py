from exercice4 import *

def test_should_create_table():
    db = DatabaseManager(testdb)
    query = "CREATE TABLE IF NOTE EXISTS tab (name VARCHAR(255) NOT NULL, firstname VARCHAR(255) NOT NULL)"
    assert db.create_table(tab, [["name", "VARCHAR(255) NOT NULL"], ["firstname", "VARCHAR(255) NOT NULL"]]) == expected_perimeter