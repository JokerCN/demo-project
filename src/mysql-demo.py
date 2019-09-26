# -*- coding: utf-8 -*-

import pymysql


if __name__ == '__main__':
    conn = pymysql.connect(user='yangyiwei', password='54321', database='test')
    cursor = conn.cursor()
    cursor.execute('create table user( id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user(id, name) values(%s, %s)', ['1', 'Michael'])
    conn.commit()
    cursor.close()

    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()