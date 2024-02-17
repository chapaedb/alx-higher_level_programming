#!/usr/bin/python3
"""Displayes states contents where satified"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
    print(row)
    cur.close()
    conn.close()


