#!/usr/bin/env python
# -*- coding: utf-8 -*-
# пример notebook.py


import sqlite3

conn = sqlite3.connect("mydb.db")
conn.text_factory = str
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE patients(id INTEGER PRIMARY KEY NOT NULL, okrug text,  familia text, imya text, otchestvo text, zvanie text, dateofbirth timestamp, dateofdeath timestamp, vchast text, disl text, rod_vid_voisk text, kontingent text, pensioner text, chlen_semi_voenosl text, lgpvsrf text, data_per_v_tyaz_stepen timestamp, OSK text, tyaz_let text, data_vybytia_is_tyaz timestamp, data_pervichnogo_post_v_tyaz timestamp, nozologii text, gorod_vch text)""")
# conn.commit()
# cursor.execute("""INSERT INTO user
#                   VALUES ('admin','admin')"""
#                )
# sql = "SELECT login,pass FROM user "
# sql = "CREATE TABLE patients(id INTEGER PRIMARY KEY AUTOINCREMENT, okrug INTEGER, zvanie INTEGER, familia text, imya text, otchestvo text, date timestamp, chast text, dislokation text, rod_voisk INTEGER, " \
#       " kontingent INTEGER, pensioner INTEGER, chlen_sem_voenosl INTEGER, lgp INTEGER, prizv_po_dog INTEGER, data_v_tyazelu_st timestamp, vozrast  text, osk text, kategory text, vzv text, tyz_let INTEGER, " \
#       " data_smerti timestamp, data_vybytsia_iz_tyazh timestamp, pervichno_postup_v_tyaz_st timestamp, nozologii INTEGER, gorod_vch INTEGER )"
# cursor.execute(sql)
# conn.commit()

def login_bd():
    sql = "SELECT login,pass FROM user1"
    return cursor.execute(sql)
def get_tyaz_from_db():
    sql = "SELECT * FROM patients"
    return cursor.execute(sql)

def add(entry, password):

    sql = """INSERT INTO user1
                              (login, pass)
                              VALUES
                              (?, ?);"""
    data_tuple = (entry, password)
    cursor.execute(sql, data_tuple)
    conn.commit()
def add_patients(okrug, familia, imya, otchestvo,
                   zvanie, dateofbirth, dateofdeath, vchast,
                   disl, rod_vid_voisk, kontingent, pensioner,
                   chlen_semi_voenosl, lgpvsrf, data_per_v_tyaz_stepen, OSK,
                   tyaz_let, data_vybytia_is_tyaz, data_pervichnogo_post_v_tyaz,
                            nozologii, gorod_vch):

    sql = """INSERT INTO patients
                              (okrug, familia, imya, otchestvo,
                   zvanie, dateofbirth, dateofdeath, vchast,
                   disl, rod_vid_voisk, kontingent, pensioner,
                   chlen_semi_voenosl, lgpvsrf, data_per_v_tyaz_stepen, OSK,
                   tyaz_let, data_vybytia_is_tyaz, data_pervichnogo_post_v_tyaz,
                            nozologii, gorod_vch)
                              VALUES
                              (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );"""
    data_tuple = (okrug, familia, imya, otchestvo,
                   zvanie, dateofbirth, dateofdeath, vchast,
                   disl, rod_vid_voisk, kontingent, pensioner,
                   chlen_semi_voenosl, lgpvsrf, data_per_v_tyaz_stepen, OSK,
                   tyaz_let, data_vybytia_is_tyaz, data_pervichnogo_post_v_tyaz,
                            nozologii, gorod_vch)
    cursor.execute(sql, data_tuple)
    conn.commit()

# def edit(id, entry, password):
#     sql = """Update user1 set  login = ?, pass = ? where a = ?"""
#     data_tuple = (entry,password, id)
#     cursor.execute(sql, data_tuple)
#     conn.commit()
def edit_patients(id, okrug, familia, imya, otchestvo,
                   zvanie, dateofbirth, dateofdeath, vchast,
                   disl, rod_vid_voisk, kontingent, pensioner,
                   chlen_semi_voenosl, lgpvsrf, data_per_v_tyaz_stepen, OSK,
                   tyaz_let, data_vybytia_is_tyaz, data_pervichnogo_post_v_tyaz,
                            nozologii, gorod_vch):
    sql = """Update patients set  okrug = ?, familia = ?, imya = ?, otchestvo = ?, zvanie = ?, dateofbirth = ?, 
    dateofdeath = ?, vchast = ?, disl = ?, rod_vid_voisk = ?, kontingent = ?, pensioner = ?, chlen_semi_voenosl = ?, 
    lgpvsrf = ?, data_per_v_tyaz_stepen = ?, OSK = ?, tyaz_let = ?, data_vybytia_is_tyaz = ?, data_pervichnogo_post_v_tyaz = ?, nozologii = ?, gorod_vch = ? where id = ?"""
    data_tuple = (okrug, familia, imya, otchestvo,
                   zvanie, dateofbirth, dateofdeath, vchast,
                   disl, rod_vid_voisk, kontingent, pensioner,
                   chlen_semi_voenosl, lgpvsrf, data_per_v_tyaz_stepen, OSK,
                   tyaz_let, data_vybytia_is_tyaz, data_pervichnogo_post_v_tyaz,
                            nozologii, gorod_vch, id)
    cursor.execute(sql, data_tuple)
    conn.commit()


def delete(id):
    sql = """DELETE from patients where id = ?"""
    # data_tuple = (id)
    cursor.execute(sql, (id, ))
    conn.commit()

