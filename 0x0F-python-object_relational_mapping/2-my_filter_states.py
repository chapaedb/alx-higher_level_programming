#!/usr/bin/python3
"""Displayes states contents where satified"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    rows = cur.fetchall()
    for row in rows:
    print(row)
    cur.close()
    conn.close()


