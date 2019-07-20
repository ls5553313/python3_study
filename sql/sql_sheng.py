import pymysql

db = pymysql.connect(host="localhost", user='root',
    password = '123456',database = 'test_day04',charset='utf8')

curt = db.cursor()

#curt.execute("insert into sheng values(14,20009,'云南省')")
curt.execute("update sheng set id=77 where id=14")
db.commit()
curt.close()
db.close()





