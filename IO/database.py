#!/usr/bin/env python
#encoding=utf8
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='111111', port=3300, charset='utf8')
cursor = conn.cursor()
cursor.execute("drop database if exists python")
cursor.execute("create database python")
conn.select_db("python")


cursor.execute("create table python(id int, name varchar(20), address varchar(20), age tinyint(3))")
cursor.execute("insert into python values(101, 'Alan', 'address1', '20'), (102, 'Paul', 'address2','50'), (103, 'Tom', 'address3','35'), (104, 'Alex', 'address4','67')")
conn.commit();#The data can be seen in database only after the commit statement is executed.
cursor.execute("select * from python")
print ("--Add data test--") #Add data
result = cursor.fetchall()
print (type(result))
for column in result:
    print (column[0], column[1], column[2], column[3])
    #print columni #Print all results.(print out pointers)

#delete data
cursor.execute("delete from python where id = 101")
cursor.execute("select * from python")
result = cursor.fetchall()
print ("--Delete data test--")
for column in result:
    print (column[0], column[1], column[2], column[3])

#update data
cursor.execute("update python set address = 'address4' where id = 103")
cursor.execute("select * from python")
print ("--Update data test--")
result = cursor.fetchall()
for column in result:
    print (column[0], column[1], column[2], column[3])

#show in order
cursor.execute('select id, name FROM python ORDER BY id DESC')  
conn.commit();  
print ("--Show in order")
result = cursor.fetchall()
for column in result:
    print (column[0], column[1])


#clear data
cursor.execute("delete from python")
cursor.execute("select * from python")
print ("--Clear data test--")
result = cursor.fetchall()
for column in result:
    print (column[0], column[1], column[2], column[3])

#drop table
#cursor.execute("drop table python")
#cursor.execute("drop database python")
cursor.close()    #Pointer closed
conn.close()      #Close the connection