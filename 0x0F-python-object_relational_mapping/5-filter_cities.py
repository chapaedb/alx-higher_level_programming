#!/usr/bin/python3
"""Lists all cities from the given state in the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id = cities.state_id WHERE states.name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print({}.format(row[0], end = ", "))
    cur.close()
    db.close()
