#!/usr/bin/python3
"""lists all cities from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    connectDb = MySQLdb.connect(host='localhost', user=user,
                                passwd=passwd, db=db, port=3306)
    cursor = connectDb.cursor()
    command = """SELECT * FROM cities.id, cities.name, states.name
           FROM cities, states WHERE cities.state_id = states.id 
           ORDER BY cities.id"""
    cursor.execute(command)
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    connectDb.close()
