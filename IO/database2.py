#!/usr/bin/env python

import pymysql
from database1 import pyDATABASE1

def main():
    conn = pymysql.connect(host='localhost', user='root', passwd='111111', db='hero', port=3300, charset='utf8')
    cur = conn.cursor()
    
    # ------------------------------------------- create -----------------------------------------------------
    hero = pyDATABASE1('hero', conn, cur)
    hero.createTable('hero1')
    
    # ------------------------------------------- insert -----------------------------------------------------
    hero.insert('hero1', [3, 'Prophet', 0, 2000, 'The hero who inS fairy tale.'])

    # ------------------------------------------- select -----------------------------------------------------
    print ('-' * 60)
    print ('first record')
    result = hero.selectFirst('hero')
    print (result)
    
    print ('-' * 60)
    print ('last record')
    result = hero.selectLast('hero')
    print (result)
    
    print ('-' * 60)
    print ('more record')
    results = hero.selectNRecord('hero', 3)
    for item in results:
        print (item)
    
    print ('-' * 60)
    print ('all record')
    results = hero.selectAll('hero')
    for item in results:
        print (item)
        
    # ------------------------------------------- update -----------------------------------------------------
    hero.updateSingle('hero', ['Zeus', 1, 22000, 'The god.', 2])
    
    values = []
    values.append(['SunWukong', 1, 1300, 'The hero who in fairy tale.', 1])
    values.append(['Zeus', 1, 50000, 'The king who in The Quartet myth.', 2])
    values.append(['Prophet', 1, 20000, 'The hero who in fairy tale.3', 3])
    hero.update('hero', values)
    
    # ------------------------------------------- delete -----------------------------------------------------
    hero.deleteByID('hero', 1)
    
    hero.dropTable('hero')
    
    #hero.dropDB('hero')
    
if __name__ == '__main__':
    main()