import pymysql

db = pymysql.connect(host="localhost", user='root',
    password = '123456',database = 'test_day04',charset='utf8')

cur = db.cursor()

try:
    sql_select = "select * from sheng;"
    cur.execute(sql_select)
    data1 = cur.fetchall()
    data2 = cur.fetchmany(3)
    print(data1)
    print(data2)
    db.commit()
except Exception as e1:
    print(e1)

cur.close()
db.close()

