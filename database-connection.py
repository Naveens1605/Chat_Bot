import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",database="user")
import bot
cursor = mydb.cursor()

sqlform = " Insert into `user details`(Name, Age,Gender,Email) values (%s,%s,%s,%s)"
name = bot.bot.
age = bot.age()
gender = bot.gender()
email = bot.email()
details = [(name, age, gender, email)]
cursor.executemany(sqlform,details)
mydb.commit()