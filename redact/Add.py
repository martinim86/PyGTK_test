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
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("CRUD")

        self.window.set_size_request(800, 800)


        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_LEFT)
        MainFrame_ex = MainFrame.MainFrame()

        frame = gtk.Frame("Добавление")
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




def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    Add()
    main()