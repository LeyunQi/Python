#!/usr/bin/python
# -*-coding : UTF-8 -*-

import re
import os
import pymysql


st = ""
def  readFile(st,db):
        
        f = open("../IO/test.txt", "r")
     
        st = f.readlines()
        dict1={'A':0, 'T':0,'C':0, 'G':0}
        tempStr1 = ""
        tempStr2 = ""
        for line in st: 
            if (line.startswith('>')) :
                tempStr1 = line
                print(tempStr1)
               
            elif(line == "\n"):
                print(tempStr2)
                dbInsert(db,tempStr1,tempStr2)
                countNum(dict1,tempStr2)
                tempStr1 = ""
                tempStr2 = ""
               
            else:

                tempStr2 += line
                
              
        f.close()




def dbConnection():
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='111111', port=3300, charset='utf8')
    cursor = db.cursor()
    cursor.execute("drop database if exists analyseData")
    cursor.execute("create database analyseData")
    db.select_db("analyseData")
    return db

def dbCreation(db):
    #打开数据库连接
    #db = pymysql.connect(host='127.0.0.1', user='root', passwd='111111', port=3300, charset='utf8')
    #获取操作游标
    db.select_db("analyseData")
    cursor = db.cursor()
    #执行sql语句
    cursor.execute('drop table if exists analyseData')
    cursor.execute("create table analyseData(title varchar(20), content text(300))")
    #关闭数据库连接
    #db.close() 

def dbInsert(db, tempStr1, tempStr2):
    #打开数据库连接
    #db = pymysql.connect(host='127.0.0.1', user='root', passwd='111111', port=3300, charset='utf8')
    #获取操作游标
    cursor = db.cursor()
    #执行sql语句
    sql = "insert into analyseData(title, content) values('" + tempStr1 + "','" + tempStr2 + "')"
    try:
        cursor.execute(sql)
        db.commit()
       
    except Exception as e:
        db.rollback()
        raise e
    #finally:
        #关闭数据库连接
        #db.close() 
"""
def countNum(tempStr2):
    d={}
    f = open("../IO/test.txt", "r")
    for line in f.readlines():
        key = line.rstrip()
        if d.__contains__(key)==False :
            d[key] += 1
        else:
            d[key] = 1

    for k, v in d.items():
        print ("%s=%s" % (k, v))
"""

def countNum(dict1,st):
    #f=open("../IO/test.txt", "r")
    #st=f.readlines()
    #dict1={'A':0, 'T':0,'C':0, 'G':0}

    #print(st)
 
    for s in st:
        #dict1.__contains__(s):
        # check whether the dict contain the key "s"
        if s != '\n':
            '''if dict1.__contains__(s)==False :
                dict1[s] = 1
            else:'''
            dict1[s] += 1

        '''else:
    # added the key "s" and set the vaule to 1 if "s" not exist in dict.
            dict1.setdefault(s,'A')'''
    #f.close()
    
    for key,value in dict1.items():
        print (key,":",value)


if __name__ == '__main__':
    db = dbConnection()
    dbCreation(db)
    readFile(st,db)
    
