#!/usr/bin/python
# -*-coding : UTF-8 -*-
import re
import os
global str
str = ""
def  readFile(str):
    try:
        file = open("../IO/test.txt", "r")
    except IOError:
        pass
    else:
        if os.path.exists("../IO/interception.txt"):
            os.remove("../IO/interception.txt")
        while True:
            str = file.readlines()
            tempStr = ""
            for line in str: 
                if (line.startswith('>')) :
                    print(line)
                    writeFile(line)
                    tempStr = ""
                elif(line == "\n"):
                   
                    line = tempStr[29:99]
                    
                    writeFile(line)
                    tempStr = ""
                    print("-----------")
                else:

                    tempStr += line
            
            break
        file.close()

def writeFile(line):
    file = open("../IO/interception.txt","a")
    str = file.write(line)
    file.write('\n')
    file.close()

if __name__ == '__main__':
    readFile(str)