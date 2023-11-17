#!/usr/bin/python3

""" The module lists all states from the
database hbtn_0e_0_usa """


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
    cur = db.cursor()
    qua = "SELECT * FROM states \
        WHERE name = '{}' ORDER BY \
            id ASC".format(args[3])
    cur.execute(qua)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()