import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ananthadas2002!",database="student")

mycursor=mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor:
	print(i)