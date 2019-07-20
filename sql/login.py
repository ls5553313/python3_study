from python_sql import *
from hashlib import sha1

uname = input("pls input name: ")
pwd = input("pls input password: ")

s1 = sha1()
s1.update(pwd.encode("utf8"))
pwd2= s1.hexdigest()

sqlh = Mysql_python("user")
select = "select password from user where name = %s;"

data = sqlh.select(select,[uname])
print(data)
if not data:
    print("name is wrong!")
elif pwd2 == data[0][0]:
    print("login success")
elif pwd2 != data[0][0]:
    print("password is wrong!")
    
