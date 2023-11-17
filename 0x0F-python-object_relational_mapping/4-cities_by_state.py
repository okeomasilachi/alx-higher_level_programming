#!/usr/bin/python3

""" The module lists all states from the database hbtn_0e_0_usa """


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )
    cursor = db.cursor()
    quary = "SELECT GROUP_CONCAT(name ORDER BY id ASC SEPARATOR ', ') \
        FROM cities WHERE state_id = \
        (SELECT id FROM states WHERE name = %s)"
    cursor.execute(quary)
    states = cursor.fetchall()
    for state in states:
        for i in state:
            print(i)
    cursor.close()
    db.close()
