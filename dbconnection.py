import pymysql
import datetime
import pickle
import os

# MySQL Connection
conn = pymysql.connect(
    host='34.64.105.45',
    user='hyuntek',
    password='000000',
    db='studyrun',
    charset='utf8')



def upload() :
    """
    upload study time to database
    """

    if os.path.isfile('save.dat') :
        with open('save.dat', 'rb') as f:
            ctime = pickle.load(f)
    else :
        print('Error : no save_data for uploading')
        return

    xpget = int(ctime[0:2])*60 + int(ctime[3:5])

    userNo = '1'
    saveDate = datetime.date.today()


    if conn.open:
        curs = conn.cursor()
        curs.execute("insert into user_log values(%s,%s,%s)", (userNo, saveDate.strftime('%y-%m-%d'), ctime))
        curs.execute("select XP from user_data where userNo = %s", userNo)
        XP = curs.fetchone()[0]
        XP += xpget
        curs.execute("update user_data set XP = %s" % XP + " where userNo = %s", userNo)
        conn.commit()
        conn.close()
        print('work done')
        with open('save.dat', 'wb') as f:
            pickle.dump('00:00:00', f)
    else :
        print("can't connect to db!")


def save(ctime) :
    """
    ctime = Concentration time data, format = '00:00:00'
    save concentration time and saveDate as dat file
    """
    if os.path.isfile('save.dat') :
        with open('save.dat', 'rb') as f:
            stime = pickle.load(f)

        hours 	= int(ctime[0:2]) + int(stime[0:2])
        mins 	= int(ctime[3:5]) + int(stime[3:5])
        sec 	= int(ctime[6:8]) + int(stime[6:8])

        if sec >= 60:
            sec -= 60
            mins += 1

        if mins >= 60:
            mins -= 60
            hours += 1

        ctime = ('%02d' % hours +'%02d' % mins +'%02d' % sec)
    with open('save.dat', 'wb') as f:
        pickle.dump(ctime, f)

def load():
    """
    return concentration time as string type, format = '00:00:00'
    """

    if os.path.isfile('save.dat') :
        with open('save.dat', 'rb') as f:
            return pickle.load(f)
    else :
        print('Error : no save data for loading')
        return




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
