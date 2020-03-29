#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) < 4:
        print('Usage: {} username password database'.format(argv[0]))
        exit(1)
    user = argv[1]
    passw = argv[2]
    db = argv[3]
    db = MySQLdb.connect(host='localhost', user=user,
                         passw=passw, db=db, port=3306)
    cursor = db.cursor()
    sql = cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)