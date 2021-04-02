#!/usr/bin/env python
# -*- coding: utf-8 -*-
# пример notebook.py


import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE user1(a INTEGER PRIMARY KEY NOT NULL, login text, pass text)""")
# conn.commit()
# cursor.execute("""INSERT INTO user
#                   VALUES ('admin','admin')"""
#                )
# sql = "SELECT login,pass FROM user "
# sql = "CREATE TABLE patients(id INTEGER PRIMARY KEY AUTOINCREMENT, okrug INTEGER, zvanie INTEGER, familia text, imya text, otchestvo text, date timestamp, chast text, dislokation text, rod_voisk INTEGER, " \
#       " kontingent INTEGER, pensioner INTEGER, chlen_sem_voenosl INTEGER, lgp INTEGER, prizv_po_dog INTEGER, data_v_tyazelu_st timestamp, vozrast  text, osk text, kategory text, vzv text, tyz_let INTEGER, " \
#       " data_smerti timestamp, data_vybytia_iz_tyazh timestamp, pervichno_postup_v_tyaz_st timestamp, nozologii INTEGER, gorod_vch INTEGER )"
# cursor.execute(sql)
# conn.commit()

def login_bd():
    sql = "SELECT login,pass FROM user1"
    return cursor.execute(sql)
def get_tyaz_from_db():
    sql = "SELECT a, login, pass FROM user1"
    return cursor.execute(sql)

def add(entry, password):

    sql = """INSERT INTO user1
                              (login, pass)
                              VALUES
                              (?, ?);"""
    data_tuple = (entry, password)
    cursor.execute(sql, data_tuple)
    conn.commit()

def edit(id, entry, password):

    sql = """Update user1 set  login = ?, pass = ? where a = ?"""
    data_tuple = (entry,password, id)
    cursor.execute(sql, data_tuple)
    conn.commit()
def delete(id):
    print id
    sql = """DELETE from user1 where a = ?"""
    data_tuple = (id)
    cursor.execute(sql, data_tuple)
    conn.commit()

