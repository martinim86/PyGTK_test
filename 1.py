#!/usr/bin/env python
# -*- coding: utf-8 -*-
# пример notebook.py

import pygtk
import sys
from constants import *
import MainFrame




pygtk.require('2.0')
import gtk


class NotebookExample:

    # Этот метод меняет расположение вкладок
    def rotate_book(self, button, notebook):
        notebook.set_tab_pos((notebook.get_tab_pos() + 1) % 4)

    # Добавляем/удаляем вкладки и границы
    def tabsborder_book(self, button, notebook):
        tval = False
        bval = False
        if self.show_tabs == False:
            tval = True
        if self.show_border == False:
            bval = True

        notebook.set_show_tabs(tval)
        self.show_tabs = tval
        notebook.set_show_border(bval)
        self.show_border = bval

    # Удаляем страницу
    def remove_book(self, button, notebook):
        page = notebook.get_current_page()
        notebook.remove_page(page)
        # Теперь нужна перезагрузка Notebook --
        # Это форсированная перерисовка его.
        notebook.queue_draw_area(0, 0, -1, -1)

    def delete(self, widget, event=None):
        gtk.main_quit()
        return False



    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.resize(800,800)
        window.connect("delete_event", self.delete)
        window.set_border_width(10)

        table = gtk.Table(3, 6, False)
        hbox = gtk.HBox('123')
        table.add(hbox)
        window.add(table)

        # Создаём Notebook, указываем расположение вкладок
        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_LEFT)
        table.attach(notebook, 0, 6, 0, 1)
        notebook.show()
        self.show_tabs = True
        self.show_border = True

        # Давайте добавим несколько страниц
        MainFrame_ex = MainFrame.MainFrame()
        for i in MENU:
            frame = gtk.Frame(i)
            frame.set_border_width(10)
            frame.set_size_request(500, 800)
            frame.show()
            label = gtk.Label(i)

            def text():
                return gtk.Label(123)

            label2 = text()
            if i == MENU[0]:
                frame.add(label2)
            if i == MENU[1]:
                frame.add(label)

            label.show()
            label = gtk.Label(i)
            notebook.append_page(frame, label)

        # Выбираем стартовую страницу (4)
        notebook.set_current_page(3)

        # Создаём несколько кнопок
        button = gtk.Button("закрыть")
        button.connect("clicked", self.delete)
        table.attach(button, 5, 6, 1, 2)
        button.show()

        button = gtk.Button("Летальные")
        button.connect("clicked", lambda w: notebook.next_page())
        table.attach(button, 1, 2, 1, 2)
        button.show()

        button = gtk.Button("ТМК")
        button.connect("clicked", lambda w: notebook.prev_page())
        table.attach(button, 2, 3, 1, 2)
        button.show()


        button = gtk.Button("Отчеты на Интерактивной карте")
        button.connect("clicked", self.tabsborder_book, notebook)
        table.attach(button, 4, 5, 1, 2)
        button.show()

        button = gtk.Button("Тяжелые")
        button.connect("clicked", self.remove_book, notebook)
        table.attach(button, 0, 1, 1, 2)
        button.show()

        button = gtk.Button("Все пациенты")
        button.connect("clicked", self.remove_book, notebook)
        table.attach(button, 0, 1, 2, 3)
        button.show()

        table.show()
        window.show()


def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    NotebookExample()
    main()