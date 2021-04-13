# -*- coding: utf-8 -*-
## @package gmapcatcher.widgets.widMySettings
# Settings widget that displays common settings.
# Displayed inside a tab in MapTools.

from redact.Add import *
from redact.Edit_old import *
from CustomWidgets import  myFrame, lbl
import bd
from constants import *
from widg.calendar import CalendarExample

class Edit_paned():

    def calendar(self, button, date):
        calendar = CalendarExample(self, date)

    def show(self, window, Mapsobj, listStore, myTree):
        treeselection = myTree.get_selection()
        (model, iter) = treeselection.get_selected()

        def _field():
            hbox = gtk.HBox(False, 10)
            self.field = gtk.combo_box_entry_new_text()
            for strType in CONST:
                self.field.append_text(strType)
            self.field.set_active(CONST.index(model[iter][1]))
            hbox.pack_start(self.field)
            return myFrame(" Поле ", hbox)


        hpaned = gtk.VPaned()
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        hbox.pack_start(_field())


        hpaned.pack1(vbox, True, True)
        buttons = self.__action_buttons(window, Mapsobj, listStore, myTree)
        hpaned.pack2(buttons, False, False)


        return hpaned

    def refresh(self, listStore, myTree):
        listStore.clear()
        myTree.set_model(self.liststore_tz(listStore))
        listStore.set_sort_column_id(0, gtk.SORT_ASCENDING)
        myTree.grab_focus()

    def __action_buttons(self, window, Mapsobj, listStore, myTree):
        treeselection = myTree.get_selection()
        (model, iter) = treeselection.get_selected()
        def btn_edit_clicked(button):
            bd.edit_new_pat(model[iter][0], CONST[self.field.get_active()],)

            window.destroy()
            Mapsobj.refresh(listStore, myTree)


        bbox = gtk.HButtonBox()
        bbox.set_layout(gtk.BUTTONBOX_END)
        bbox.set_border_width(10)
        bbox.set_spacing(60)

        button = gtk.Button(stock=gtk.STOCK_SAVE)
        button.connect('clicked', btn_edit_clicked)
        bbox.add(button)

        button = gtk.Button(stock=gtk.STOCK_CANCEL)
        # button.connect('clicked', btn_edit_clicked, listStore, myTree)
        bbox.add(button)



        return bbox
    def change_selection(self, myTree, intPath):
        if intPath >= 0:
            myTree.set_cursor(intPath)
            myTree.grab_focus()



