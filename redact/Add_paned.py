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

class Add_paned():
    okrug = ""
    def calendar(self, button, date):
        calendar = CalendarExample(self, date)




    def show(self, window, Mapsobj, listStore, myTree):
        def field(self):
            hbox = gtk.HBox(False, 10)
            self.field = gtk.combo_box_entry_new_text()
            for strType in CONST1:
                self.field.append_text(strType)
            hbox.pack_start(self.field)
            return myFrame(" Поле ", hbox)



        hpaned = gtk.VPaned()
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        hbox.pack_start(self._field())


        vbox.pack_start(hbox, False)

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
        def btn_add_clicked(button):
            bd.add_patients(self.field)


            window.destroy()
            Mapsobj.refresh(listStore, myTree)





        bbox = gtk.HButtonBox()
        bbox.set_layout(gtk.BUTTONBOX_END)
        bbox.set_border_width(10)
        bbox.set_spacing(60)

        button = gtk.Button(stock=gtk.STOCK_SAVE)
        button.connect('clicked', btn_add_clicked)
        bbox.add(button)

        button = gtk.Button(stock=gtk.STOCK_CANCEL)
        bbox.add(button)



        return bbox
    def change_selection(self, myTree, intPath):
        if intPath >= 0:
            myTree.set_cursor(intPath)
            myTree.grab_focus()



