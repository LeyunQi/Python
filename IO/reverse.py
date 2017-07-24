#!/usr/bin/python
# -*-coding : UTF-8 -*-

#打开一个文件
import re
import os
global st
st = ''
def  readFile(st):
    f = open("../IO/test.txt", "r")

    if os.path.exists("../IO/reverse.txt"):
        os.remove("../IO/reverse.txt")
    st = f.readlines()
    tempst = ''
    for line in st: 
        if (line.startswith('>')) :
            writeFile(line)
            tempst = ''
        elif(line == "\n"):
            line = tempst[::-1]
            writeFile(line)
            tempst = ''
        else:
            tempst += line
    
    f.close()

def writeFile(line):
    f = open("../IO/reverse.txt","a")
    st = f.write(line)
    f.write('\n')
    f.close()

'''
def sReverse(line):
    line = line[::-1]
    return line
'''

if __name__ == '__main__':
    readFile(st)