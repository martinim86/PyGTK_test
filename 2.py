#!/usr/bin/env python
# -*- coding: utf-8 -*-
# example treeviewdnd.py

import pygtk

pygtk.require('2.0')
import gtk


class TreeViewDnDExample:
    TARGETS = [
        ('MY_TREE_MODEL_ROW', gtk.TARGET_SAME_WIDGET, 0),
        ('text/plain', 0, 1),
        ('TEXT', 0, 2),
        ('STRING', 0, 3),
    ]

    # закрываем окно и выходим
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def clear_selected(self, button):
        selection = self.treeview.get_selection()
        model, iter = selection.get_selected()
        if iter:
            model.remove(iter)
        return

    def __init__(self):
        # Создаём новое окно
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("URL Cache")

        self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        self.scrolledwindow = gtk.ScrolledWindow()
        self.vbox = gtk.VBox()
        self.hbox = gtk.HButtonBox()
        self.vbox.pack_start(self.scrolledwindow, True)
        self.vbox.pack_start(self.hbox, False)
        self.b0 = gtk.Button(None, gtk.STOCK_CLEAR)
        self.b1 = gtk.Button(None, gtk.STOCK_CUT)
        self.hbox.pack_start(self.b0)
        self.hbox.pack_start(self.b1)

        # создааём liststore с одним строковым столбцом
        self.liststore = gtk.ListStore(str)

        # создаём TreeView используя liststore
        self.treeview = gtk.TreeView(self.liststore)

        # создаём CellRenderer для отображения данных
        self.cell = gtk.CellRendererText()

        # создаём TreeViewColumn для отображения данных
        self.tvcolumn = gtk.TreeViewColumn('URL', self.cell, text=0)

        # добавляем столбцы в treeview
        self.treeview.append_column(self.tvcolumn)
        self.b0.connect_object('clicked', gtk.ListStore.clear, self.liststore)
        self.b1.connect('clicked', self.clear_selected)
        # make treeview searchable
        self.treeview.set_search_column(0)

        # разрешаем сортировку
        self.tvcolumn.set_sort_column_id(0)

        # Включаем перетаскивание веток включая перемещение
        self.treeview.enable_model_drag_source(gtk.gdk.BUTTON1_MASK,
                                               self.TARGETS,
                                               gtk.gdk.ACTION_DEFAULT |
                                               gtk.gdk.ACTION_MOVE)
        self.treeview.enable_model_drag_dest(self.TARGETS,
                                             gtk.gdk.ACTION_DEFAULT)

        self.treeview.connect("drag_data_get", self.drag_data_get_data)
        self.treeview.connect("drag_data_received",
                              self.drag_data_received_data)

        self.scrolledwindow.add(self.treeview)
        self.window.add(self.vbox)
        self.window.show_all()

    def drag_data_get_data(self, treeview, context, selection, target_id,
                           etime):
        treeselection = treeview.get_selection()
        model, iter = treeselection.get_selected()
        data = model.get_value(iter, 0)
        selection.set(selection.target, 8, data)

    def drag_data_received_data(self, treeview, context, x, y, selection,
                                info, etime):
        model = treeview.get_model()
        data = selection.data
        drop_info = treeview.get_dest_row_at_pos(x, y)
        if drop_info:
            path, position = drop_info
            iter = model.get_iter(path)
            if (position == gtk.TREE_VIEW_DROP_BEFORE
                    or position == gtk.TREE_VIEW_DROP_INTO_OR_BEFORE):
                model.insert_before(iter, [data])
            else:
                model.insert_after(iter, [data])
        else:
            model.append([data])
        if context.action == gtk.gdk.ACTION_MOVE:
            context.finish(True, True, etime)
        return


def main():
    gtk.main()


if __name__ == "__main__":
    treeviewdndex = TreeViewDnDExample()
    for i in ['www.yandex.ru', 'www.google.ru', 'www.pygtk.ru', 'www.rosix.ru']:
        treeviewdndex.liststore.append([i])
    main()

