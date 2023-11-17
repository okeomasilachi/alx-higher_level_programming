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
    quary = "SELECT cities.id, cities.name, \
        states.name FROM cities JOIN states \
            ON cities.state_id = states.id \
                ORDER BY cities.id ASC"
    cursor.execute(quary)
    states = cursor.fetchall()
    for i in states:
        print(i)
    cursor.close()
    db.close()
