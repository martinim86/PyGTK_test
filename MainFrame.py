# -*- coding: utf-8 -*-
## @package gmapcatcher.widgets.widMySettings
# Settings widget that displays common settings.
# Displayed inside a tab in MapTools.

from redact.Add import *
from redact.Edit import *

class MainFrame():
    model = ""
    treeiter = ""

    def liststore_tz(self, listStore):
        for i in bd.get_tyaz_from_db():
            listStore.append([i[0], i[1], i[2]])
        return listStore



    def show(self, i):
        listStore = gtk.ListStore(str, str, str)

        myTree = gtk.TreeView(self.liststore_tz(listStore))
        strCols = ['Index','login', 'pass']
        treeselection = myTree.get_selection()
        def on_tree_selection_changed(selection):
            model, treeiter = treeselection.get_selected()
            self.model = model
            self.treeiter = treeiter

        treeselection.connect("changed", on_tree_selection_changed)
        (model, iter) = treeselection.get_selected()




        for intPos in range(len(strCols)):
            # Create a CellRenderers to render the data
            cell = gtk.CellRendererText()
            # Allow Cells to be editable
            cell.set_property('editable', True)
            # Create the TreeViewColumns to display the data
            tvcolumn = gtk.TreeViewColumn(strCols[intPos])
            myTree.append_column(tvcolumn)
            tvcolumn.pack_start(cell, True)
            tvcolumn.set_attributes(cell, text=intPos)
            tvcolumn.set_sort_column_id(intPos)
            tvcolumn.set_resizable(True)
            if intPos == 0:
                tvcolumn.set_expand(True)
            else:
                tvcolumn.set_min_width(75)
        myTree.set_search_column(0)
        listStore.set_sort_column_id(0, gtk.SORT_ASCENDING)

        hpaned = gtk.VPaned()
        scrolledwindow = gtk.ScrolledWindow()
        scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scrolledwindow.add(myTree)
        hpaned.pack1(scrolledwindow, True, True)
        label = gtk.Label(i)
        buttons = self.__action_buttons(listStore, myTree)
        hpaned.pack2(buttons, False, False)


        return hpaned

    def __action_buttons(self, listStore, myTree):
        def btn_add_clicked(button):
            Add()
        def btn_edit_clicked(button):
            Edit(self.model, self.treeiter)

        def btn_delete_clicked(button):
            print "hi"
        bbox = gtk.HButtonBox()
        bbox.set_layout(gtk.BUTTONBOX_END)
        bbox.set_border_width(10)
        bbox.set_spacing(60)

        button = gtk.Button(stock=gtk.STOCK_ADD)
        button.connect('clicked', btn_add_clicked)
        bbox.add(button)

        button = gtk.Button(stock=gtk.STOCK_EDIT)
        button.connect('clicked', btn_edit_clicked)
        bbox.add(button)


        button = gtk.Button(stock=gtk.STOCK_DELETE)
        button.connect('clicked', btn_delete_clicked, listStore, myTree )
        bbox.add(button)

        return bbox



