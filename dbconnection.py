import pymysql
import datetime


# MySQL Connection
conn = pymysql.connect(
    host='34.64.105.45',
    user='hyuntek',
    password='000000',
    db='studyrun',
    charset='utf8')



def upload(ctime,xpget) :
    """
    ctime = Concentration time data, format = '00:00:00'
    xpget = conversed xp data from studying, format = int
    upload study time to database
    """


    userNo = '1'
    saveDate = datetime.date.today()


    if conn.open:
        curs = conn.cursor()
        curs.execute("insert into user_log values(%s,%s,%s)", (userNo, saveDate.strftime('%y-%m-%d'), ctime))
        curs.execute("select XP from user_data where userNo = %s", userNo)
        XP = curs.fetchone()[0]
        XP += xpget
        curs.execute("update user_data set XP = %s" % XP + " where userNo = %s", userNo)
        conn.close()
        print('work done')
    else :
        print("can't connect to db!")


upload('00:15:00',500)



"""
# example codes

# data insert format
# sql = "insert into studydata values(%s,%s,%s)"
# curs.execute(sql,(str(userNo),saveDate,str(concenTime)))


# data read format with condition
sql = "select * from studydata where userNo = %s and saveDate = '%s'" % (str(userNo), saveDate)
curs.execute(sql)

# data Fetch & reading format
rows = curs.fetchall()      # get all data from db
for row in rows:
    print(row[2].seconds)   # change timedelta format to integer as seconds



# close connection
conn.close()
"""

