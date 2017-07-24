#!/usr/bin/python
# -*-coding : UTF-8 -*-

#打开一个文件
import os
global str
str = ""
def readFile(str):
    f = open("../IO/test.txt", "r")
    str = f.readline()
    if os.path.exists("../IO/result.txt"):
       os.remove("../IO/result.txt")
    while str :
        print(str)
        writeFile(str)
        str = f.readline()
        
    f.close()

def writeFile(str):
    f = open("../IO/result.txt","a")
    str = f.write(str)
    f.close()

if __name__ == '__main__':
    readFile(str)
       
        
