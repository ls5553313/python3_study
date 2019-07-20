from python_sql import Mysql_python

sqlh = Mysql_python("test_day04")

sql_update = "update sheng set s_name=%s where s_name='日本省';"

sqlh.execute(sql_update,['澳大利亚'])


sql_select = "select * from sheng where id = %s"

data = sqlh.select(sql_select,[2])
print(data)