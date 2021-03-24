import pymysql



# MySQL Connection
conn = pymysql.connect(
    host='34.64.105.45',
    user='hyuntek',
    password='000000',
    db='studyrun',
    charset='utf8')

# cursor from conn
curs = conn.cursor()

# preset data ignore...
userNo = '1'
saveDate = '2021-03-24'
concenTime = '600'


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


