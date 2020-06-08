import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",database="user")
cursor = mydb.cursor()

sqlform = " Insert into details(Name, Age,Gender,Email) values (%s,%s,%s,%s) "
from Chat Bot
details = [(msg)]
cursor.executemany(sqlform,details)
mydb.commit()