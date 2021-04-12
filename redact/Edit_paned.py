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
    okrug = ""
    def enter_callback(self):
        print "hlk"
    def calendar(self, button, date):
        calendar = CalendarExample(self, date)




    def show(self, window, Mapsobj, listStore, myTree):
        treeselection = myTree.get_selection()
        (model, iter) = treeselection.get_selected()

        def _okrug():
            hbox = gtk.HBox(False, 10)
            self.okrug = gtk.combo_box_entry_new_text()
            for strType in OKRUG:
                self.okrug.append_text(strType)
            self.okrug.set_active(OKRUG.index(model[iter][1]))
            hbox.pack_start(self.okrug)
            return myFrame(" Округ ", hbox)
        def _familia():
            hbox = gtk.HBox(False, 10)
            self.entry_familia = gtk.Entry()
            self.entry_familia.set_max_length(50)
            self.entry_familia.set_text(model[iter][2])
            hbox.pack_start(self.entry_familia, True)
            return myFrame(" Фамилия ", hbox)
        def _imya():
            hbox = gtk.HBox(False, 10)
            self.entry_imya = gtk.Entry()
            self.entry_imya.set_max_length(50)
            self.entry_imya.set_text(model[iter][3])
            hbox.pack_start(self.entry_imya, True)
            return myFrame(" Имя ", hbox)

        def _othcestvo():
            hbox = gtk.HBox(False, 10)
            self.entry_othcestvo = gtk.Entry()
            self.entry_othcestvo.set_max_length(50)
            self.entry_othcestvo.set_text(model[iter][4])
            hbox.pack_start(self.entry_othcestvo, True)
            return myFrame(" Отчетство ", hbox)
        def _zvanie():
            hbox = gtk.HBox(False, 5)
            # self.entry_zvanie = gtk.Entry()
            # self.entry_zvanie.set_max_length(50)
            # hbox.pack_start(self.entry_zvanie, True)
            self.zvanie = gtk.combo_box_entry_new_text()
            for strType in ZVANIE:
                self.zvanie.append_text(strType)
            self.zvanie.set_active(ZVANIE.index(model[iter][5]))
            hbox.pack_start(self.zvanie)
            return myFrame(" Звание ", hbox)


        def _dateofbirth():
            hbox = gtk.HBox(False, 5)
            self.entry_dateofbirth = gtk.Entry()
            self.entry_dateofbirth.set_max_length(50)
            button = gtk.Button("...")
            button.connect('clicked', self.calendar, self.entry_dateofbirth)
            self.entry_dateofbirth.set_text(model[iter][6])
            hbox.pack_start(self.entry_dateofbirth, True)
            hbox.pack_start(button, False)
            return myFrame(" Дата рождения ", hbox)
        def _dateofdeat():
            hbox = gtk.HBox(False, 5)
            self.entry_dateofdeath = gtk.Entry()
            self.entry_dateofdeath.set_max_length(50)
            button = gtk.Button("...")
            button.connect('clicked', self.calendar, self.entry_dateofdeath)
            self.entry_dateofdeath.set_text(model[iter][7])
            hbox.pack_start(self.entry_dateofdeath, True)
            hbox.pack_start(button, False)
            return myFrame(" Дата смерти ", hbox)
        def _vchast():
            hbox = gtk.HBox(False, 5)
            self.entry_vchast = gtk.Entry()
            self.entry_vchast.set_max_length(50)
            self.entry_vchast.set_text(model[iter][8])
            hbox.pack_start(self.entry_vchast, True)
            return myFrame(" Военная часть ", hbox)
        def _disl():
            hbox = gtk.HBox(False, 5)
            self.entry_disl = gtk.Entry()
            self.entry_disl.set_max_length(50)
            self.entry_disl.set_text(model[iter][9])
            hbox.pack_start(self.entry_disl, True)
            return myFrame(" Дислокация ", hbox)
        def _rod_vid_voisk():
            hbox = gtk.HBox(False, 5)
            self.entry_rod_vid_voisk = gtk.Entry()
            self.entry_rod_vid_voisk.set_max_length(50)
            self.entry_rod_vid_voisk.set_text(model[iter][10])
            hbox.pack_start(self.entry_rod_vid_voisk, True)
            return myFrame(" Род/вид войск ", hbox)
        def _kontingent():
            hbox = gtk.HBox(False, 5)
            # self.entry_kontingent = gtk.Entry()
            # self.entry_kontingent.set_max_length(50)
            # hbox.pack_start(self.entry_kontingent, True)
            self.kontingent = gtk.combo_box_entry_new_text()
            for strType in KONTINGENT:
                self.kontingent.append_text(strType)
            self.kontingent.set_active(KONTINGENT.index(model[iter][11]))
            hbox.pack_start(self.kontingent)
            return myFrame(" Контингент ", hbox)
        def _pensioner():
            hbox = gtk.HBox(False, 5)
            self.pensioner = gtk.combo_box_entry_new_text()
            for strType in YES_NO:
                self.pensioner.append_text(strType)
            self.pensioner.set_active(YES_NO.index(model[iter][12]))
            hbox.pack_start(self.pensioner)
            return myFrame(" Пенсионер ", hbox)
        def _chlen_semi_voenosl():
            hbox = gtk.HBox(False, 5)
            # self.entry_chlen_semi_voenosl = gtk.Entry()
            # self.entry_chlen_semi_voenosl.set_max_length(50)
            # hbox.pack_start(self.entry_chlen_semi_voenosl, True)
            self.semi_voen = gtk.combo_box_entry_new_text()
            for strType in YES_NO:
                self.semi_voen.append_text(strType)
            self.semi_voen.set_active(YES_NO.index(model[iter][13]))
            hbox.pack_start(self.semi_voen)
            return myFrame(" Член семьи военнослужащего ", hbox)
        def _lgpvsrf():
            hbox = gtk.HBox(False, 5)
            self.entry_lgpvsrf = gtk.Entry()
            self.entry_lgpvsrf.set_max_length(50)
            self.entry_lgpvsrf.set_text(model[iter][14])
            hbox.pack_start(self.entry_lgpvsrf, True)
            return myFrame(" ЛГП ", hbox)
        def _data_per_v_tyaz_stepen():
            hbox = gtk.HBox(False, 5)
            self.entry_data_per_v_tyaz_stepen = gtk.Entry()
            self.entry_data_per_v_tyaz_stepen.set_max_length(50)
            button = gtk.Button("...")
            button.connect('clicked', self.calendar, self.entry_data_per_v_tyaz_stepen)
            self.entry_data_per_v_tyaz_stepen.set_text(model[iter][15])
            hbox.pack_start(self.entry_data_per_v_tyaz_stepen, True)
            hbox.pack_start(button, False)
            return myFrame(" Дата перехода в тяж степень ", hbox)
        def _OSK():
            hbox = gtk.HBox(False, 5)
            self.entry_OSK = gtk.Entry()
            self.entry_OSK.set_max_length(50)
            self.entry_OSK.set_text(model[iter][16])
            hbox.pack_start(self.entry_OSK, True)
            return myFrame(" ОСК ", hbox)
        def _tyaz_let():
            hbox = gtk.HBox(False, 5)
            self.tyaz_let = gtk.combo_box_entry_new_text()
            for strType in TYAZ_LET:
                self.tyaz_let.append_text(strType)
            self.tyaz_let.set_active(TYAZ_LET.index(model[iter][17]))
            hbox.pack_start(self.tyaz_let)
            return myFrame(" Тяжелые/летальные ", hbox)

        def _data_vybytia_is_tyaz():
            hbox = gtk.HBox(False, 5)
            self.entry_data_vybytia_is_tyaz = gtk.Entry()
            self.entry_data_vybytia_is_tyaz.set_max_length(50)
            button = gtk.Button("...")
            button.connect('clicked', self.calendar, self.entry_data_vybytia_is_tyaz)
            self.entry_data_vybytia_is_tyaz.set_text(model[iter][18])
            hbox.pack_start(self.entry_data_vybytia_is_tyaz, True)
            hbox.pack_start(button, False)
            return myFrame(" Дата выбытия из тяжелых ", hbox)
        def _data_pervichnogo_post_v_tyaz():
            hbox = gtk.HBox(False, 5)
            self.entry_data_pervichnogo_post_v_tyaz = gtk.Entry()
            self.entry_data_pervichnogo_post_v_tyaz.set_max_length(50)
            button = gtk.Button("...")
            button.connect('clicked', self.calendar, self.entry_data_pervichnogo_post_v_tyaz)
            self.entry_data_pervichnogo_post_v_tyaz.set_text(model[iter][19])
            hbox.pack_start(self.entry_data_pervichnogo_post_v_tyaz, True)
            hbox.pack_start(button, False)
            return myFrame(" Дата первичного поступления в тяж степень ", hbox)
        def _nozologii():
            hbox = gtk.HBox(False, 5)
            self.nozologii = gtk.combo_box_entry_new_text()
            hbox.pack_start(self.nozologii, True)
            for strType in NOZOLOGII:
                self.nozologii.append_text(strType)
            self.nozologii.set_active(NOZOLOGII.index(model[iter][20]))
            return myFrame(" Нозологии ", hbox)
        def _gorod_vch():
            hbox = gtk.HBox(False, 5)
            self.entry_gorod_vch = gtk.Entry()
            self.entry_gorod_vch.set_max_length(50)
            hbox.pack_start(self.entry_gorod_vch, True)
            self.entry_gorod_vch.set_text(model[iter][21])
            return myFrame(" Город в\ч ", hbox)

        hpaned = gtk.VPaned()
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        hbox.pack_start(_okrug())
        hbox.pack_start(_familia())
        hbox.pack_start(_imya())
        hbox.pack_start(_othcestvo())
        hbox.pack_start(_zvanie())
        vbox.pack_start(hbox, False)

        hbox = gtk.HBox()
        hbox.pack_start(_dateofbirth())
        hbox.pack_start(_dateofdeat())
        hbox.pack_start(_vchast())
        hbox.pack_start(_disl())
        hbox.pack_start(_rod_vid_voisk())
        vbox.pack_start(hbox, False)

        hbox = gtk.HBox()
        hbox.pack_start(_kontingent())
        hbox.pack_start(_pensioner())
        hbox.pack_start(_chlen_semi_voenosl())
        hbox.pack_start(_lgpvsrf())
        hbox.pack_start(_data_per_v_tyaz_stepen())
        vbox.pack_start(hbox, False)

        hbox = gtk.HBox()
        hbox.pack_start(_OSK())
        hbox.pack_start(_tyaz_let())
        hbox.pack_start(_data_vybytia_is_tyaz())
        hbox.pack_start(_data_pervichnogo_post_v_tyaz())
        vbox.pack_start(hbox, False)

        hbox = gtk.HBox()
        hbox.pack_start(_nozologii())
        hbox.pack_start(_gorod_vch())
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
        treeselection = myTree.get_selection()
        (model, iter) = treeselection.get_selected()
        def btn_edit_clicked(button):
            bd.edit_patients(model[iter][0], OKRUG[self.okrug.get_active()], self.entry_familia.get_text(), self.entry_imya.get_text(), self.entry_othcestvo.get_text(),
                   ZVANIE[self.zvanie.get_active()], self.entry_dateofbirth.get_text(), self.entry_dateofdeath.get_text(), self.entry_vchast.get_text(),
                   self.entry_disl.get_text(), self.entry_rod_vid_voisk.get_text(), KONTINGENT[self.kontingent.get_active()], YES_NO[self.pensioner.get_active()],
                   YES_NO[self.semi_voen.get_active()], self.entry_lgpvsrf.get_text(), self.entry_data_per_v_tyaz_stepen.get_text(), self.entry_OSK.get_text(),
                   TYAZ_LET[self.tyaz_let.get_active()], self.entry_data_vybytia_is_tyaz.get_text(), self.entry_data_pervichnogo_post_v_tyaz.get_text(),
                            NOZOLOGII[self.nozologii.get_active()], self.entry_gorod_vch.get_text())

            window.destroy()
            Mapsobj.refresh(listStore, myTree)
            # self.settingsw = Add(self, listStore, myTree)




        #
        # def btn_edit_clicked(button, listStore, myTree):
        #     Edit(self.model, self.treeiter, self, listStore, myTree)
        #
        # def btn_delete_clicked(button, listStore, myTree):
        #     treeSelection = myTree.get_selection()
        #     model, iter = treeSelection.get_selected()
        #     bd.delete(model[iter][0])
        #     self.refresh(listStore, myTree)






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



