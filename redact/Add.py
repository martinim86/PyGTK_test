#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example entry.py
import gobject
import re
import sys
import time
import MainFrame
import pygtk
import bd
import gtk
pygtk.require('2.0')
from constants import *
import Add_paned




class Add:


        # print
    def enter_callback(self, widget, entry):
        entry_text = entry.get_text()
        print "Entry contents: %s\n" % entry_text


    def password_toggle_visibility(self, checkbutton, password):
        password.set_visibility(checkbutton.get_active())
    # def test(self):
    #     MainFrame()

    def __init__(self, Mapsobj, listStore, myTree):
        # window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        # window.set_size_request(600, 600)
        # window.set_title("Добавление записи")
        # window.connect("delete_event", lambda w, e: Mapsobj.refresh(listStore, myTree))
        # window.set_destroy_with_parent(True)
        # vbox = gtk.VBox(False, 0)
        # window.add(vbox)
        # vbox.show()
        #
        #
        #
        # label = gtk.Label()
        # label.set_text("Логин")
        # self.entry = gtk.Entry()
        # self.entry.set_max_length(50)
        # self.entry.connect("activate", self.enter_callback, self.entry)
        #
        # vbox.pack_start(self.entry, True, True, 0)
        # vbox.pack_start(label, True, True, 0)
        # self.entry.show()
        #
        # self.password = gtk.Entry()
        # self.password.set_max_length(50)
        # # self.password.set_text("Пароль")
        # vbox.pack_start(self.password, True, True, 0)
        # self.password.show()
        #
        # hbox = gtk.HBox(False, 0)
        # vbox.add(hbox)
        # hbox.show()
        # button_login = gtk.Button("Сохранить")
        # hbox.pack_start(button_login, True, True, 0)
        # button_login.connect("clicked",self.key_press_event, window, Mapsobj, listStore, myTree)
        # button_login.show()
        #
        # button = gtk.Button(stock=gtk.STOCK_CLOSE)
        # button.connect("clicked", lambda w: gtk.main_quit())
        # hbox.pack_start(button, True, True, 0)
        # button.set_flags(gtk.CAN_DEFAULT)
        # button.grab_default()
        # button.show()

        # window.show()
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("База дежурного ЦКМО")

        self.window.set_size_request(800, 800)

        # self.window.connect("delete_event", self.delete_event)

        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_LEFT)
        MainFrame_ex = MainFrame.MainFrame()

        frame = gtk.Frame("Добавление тяжелого пациента")
        frame.set_border_width(10)
        frame.set_size_request(100, 75)
        frame.show()
        label = gtk.Label("Hi")
        add_paned = Add_paned.Add_paned()
        frame.add(add_paned.show(self.window, Mapsobj, listStore, myTree))

        label = gtk.Label("Добавлени записи")
        notebook.append_page(frame, label)
        notebook.set_current_page(0)
        self.window.add(notebook)
        self.window.show_all()

        def key_press_event(self,  event, window, Mapsobj, listStore, myTree):
        # bd.add(self.entry.get_text(), self.password.get_text())
        # window.destroy()
        # Mapsobj.refresh(listStore, myTree)
            print "Hi"



def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    Add()
    main()