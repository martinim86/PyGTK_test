#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example entry.py
import gobject
import re
import sys
import time
import Notebook
import pygtk
import bd
import gtk
pygtk.require('2.0')




class EntryExample:
    def login(self, num, window):

        for i in bd.login_bd():
            if self.entry.get_text() == i[0] and self.password.get_text() == i[1] :
                Notebook.BasicTreeViewExample()
                window.destroy()



        # print
    def enter_callback(self, widget, entry):
        entry_text = entry.get_text()
        print "Entry contents: %s\n" % entry_text


    def password_toggle_visibility(self, checkbutton, password):
        password.set_visibility(checkbutton.get_active())

    def __init__(self):
        # Создаём новое окно
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(600, 600)
        window.set_title("Регистрация")
        window.connect("delete_event", lambda w, e: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()


        label = gtk.Label()
        label.set_text("Логин")
        self.entry = gtk.Entry()
        self.entry.set_max_length(50)
        self.entry.connect("activate", self.enter_callback, self.entry)
        self.entry.set_text("Логин")
        vbox.pack_start(self.entry, True, True, 0)
        vbox.pack_start(label, True, True, 0)

        self.entry.show()

        self.password = gtk.Entry()
        self.password.set_max_length(50)
        self.password.set_text("Пароль")
        vbox.pack_start(self.password, True, True, 0)
        self.password.show()

        hbox = gtk.HBox(False, 0)
        vbox.add(hbox)
        hbox.show()



        check = gtk.CheckButton("Видимые\nсимволы")
        hbox.pack_start(check, True, True, 0)
        check.connect("toggled", self.password_toggle_visibility, self.password)
        check.set_active(True)
        check.show()

        button_login = gtk.Button("Войти")
        vbox.pack_start(button_login, True, True, 0)
        button_login.connect("clicked", self.login, window)
        button_login.show()

        button = gtk.Button(stock=gtk.STOCK_CLOSE)
        button.connect("clicked", lambda w: gtk.main_quit())
        vbox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        window.show()




def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    EntryExample()
    main()