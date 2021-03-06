#!/usr/bin/python
import MySQLdb
import config
import datetime

db = MySQLdb.connect(config.host,
                     config.user,
                     config.passwd,
                     config.db)

cur = db.cursor()

d = datetime.date(2005,8,1)
end_day = d.today()

delta = datetime.timedelta(days=1)

while d<= end_day:
   cur.execute(config.query % (d,d))
   for row in cur.fetchall() :
      print "%s,%s" % (d,row[0])
   d+=delta

