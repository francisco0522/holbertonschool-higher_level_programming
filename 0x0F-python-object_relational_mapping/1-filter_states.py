#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    connectDb = MySQLdb.connect(host='localhost', user=user,
                                passwd=passwd, db=db, port=3306)
    cursor = connectDb.cursor()
    cursor.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY states.id")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    connectDb.close()
