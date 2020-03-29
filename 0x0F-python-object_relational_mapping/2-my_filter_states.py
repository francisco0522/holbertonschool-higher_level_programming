#!/usr/bin/python3
"""takes in an argument and displays all values"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    arg = argv[4]
    connectDb = MySQLdb.connect(host='localhost', user=user,
                                passwd=passwd, db=db, port=3306)
    cursor = connectDb.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY states.name = '{}' ORDER BY states.id"
        .format(arg))
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    connectDb.close()
