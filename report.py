#!/usr/bin/python
import MySQLdb
import config
import datetime

db = MySQLdb.connect(config.host,
                     config.user,
                     config.passwd,
                     config.db)

cur = db.cursor()

d = datetime.date(2014,1,1)
end_day = d.today()

delta = datetime.timedelta(days=1)

while d<= end_day:

   cur.execute("SELECT count(id) FROM Tickets WHERE Date(Created) = %s;", (str(d)))

   for row in cur.fetchall() :
      print "%s,%s" % (d,row[0])

   d+=delta

