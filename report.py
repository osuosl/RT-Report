#!/usr/bin/python
import MySQLdb
import config

db = MySQLdb.connect(config.host,
                     config.user,
                     config.passwd,
                     config.db)

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT COUNT(id) FROM Tickets")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]
