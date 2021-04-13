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
        for i in bd.get_field():
            listStore.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[12]])
        return listStore



    def show(self, i):
        listStore = gtk.ListStore(int, str, str, str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)

        myTree = gtk.TreeView(self.liststore_tz(listStore))
        strCols = ['Index','Field_1',  'Field_2', 'Field_3', 'Field_4', 'Field_5', 'Field_6' , 'Field_7', 'Field_8', 'Field_9', 'Field_10', 'Field_11', 'Field_12', 'Field_13', 'Field_14', 'Field_15', 'Field_16', 'Field_17', 'Field_18', 'Field_19', 'Field_20', 'Field_21']
        treeselection = myTree.get_selection()
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

    def refresh(self, listStore, myTree):
        listStore.clear()
        myTree.set_model(self.liststore_tz(listStore))
        listStore.set_sort_column_id(0, gtk.SORT_ASCENDING)
        myTree.grab_focus()

    def __action_buttons(self, listStore, myTree):
        def btn_add_clicked(button, listStore, myTree):
            self.settingsw = Add(self, listStore, myTree)

        def btn_edit_clicked(button, listStore, myTree):
            Edit(self, listStore, myTree)

        def btn_delete_clicked(button, listStore, myTree):
            treeSelection = myTree.get_selection()
            model, iter = treeSelection.get_selected()
            bd.delete(model[iter][0])
            self.refresh(listStore, myTree)






        bbox = gtk.HButtonBox()
        bbox.set_layout(gtk.BUTTONBOX_END)
        bbox.set_border_width(10)
        bbox.set_spacing(60)

        button = gtk.Button(stock=gtk.STOCK_ADD)
        button.connect('clicked', btn_add_clicked, listStore, myTree)
        bbox.add(button)

        button = gtk.Button(stock=gtk.STOCK_EDIT)
        button.connect('clicked', btn_edit_clicked, listStore, myTree)
        bbox.add(button)


        button = gtk.Button(stock=gtk.STOCK_DELETE)
        button.connect('clicked', btn_delete_clicked, listStore, myTree )
        bbox.add(button)

        return bbox
    def change_selection(self, myTree, intPath):
        if intPath >= 0:
            myTree.set_cursor(intPath)
            myTree.grab_focus()



