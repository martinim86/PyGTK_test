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
import Edit_paned




class Edit:


    def __init__(self,  Mapsobj, listStore, myTree):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("CRUD")
        self.window.set_size_request(800, 800)
        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_LEFT)
        MainFrame_ex = MainFrame.MainFrame()
        frame = gtk.Frame("Редактирование записи")
        frame.set_border_width(10)
        frame.set_size_request(100, 75)
        frame.show()
        label = gtk.Label("")
        add_paned = Edit_paned.Edit_paned()
        frame.add(add_paned.show(self.window, Mapsobj, listStore, myTree))
        label = gtk.Label("Редактирование записи")
        notebook.append_page(frame, label)
        notebook.set_current_page(0)
        self.window.add(notebook)
        self.window.show_all()

def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    Edit()
    main()