import pygtk
pygtk.require('2.0')
import gtk
from constants import *
import MainFrame
import bd


class BasicTreeViewExample:


    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("TreeView")

        self.window.set_size_request(600, 600)

        self.window.connect("delete_event", self.delete_event)

        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_LEFT)
        MainFrame_ex = MainFrame.MainFrame()
        for i in MENU:
            frame = gtk.Frame(i)
            frame.set_border_width(10)
            frame.set_size_request(100, 75)
            frame.show()
            label = gtk.Label(i)

            if i == MENU[0]:
                frame.add(MainFrame_ex.show(i))
            if i == MENU[1]:
                frame.add(label)

            label = gtk.Label(i)
            notebook.append_page(frame, label)
        notebook.set_current_page(0)
        self.window.add(notebook)
        self.window.show_all()


def main():
    gtk.main()


if __name__ == "__main__":
    tvexample = BasicTreeViewExample()
    main()