# -*- coding: utf-8 -*-
## @package gmapcatcher.widgets.customWidgets
# This is a collection of Custom Widgets

import gtk
import gobject

import warnings
warnings.filterwarnings("ignore")

ternary = lambda a, b, c: (b, c)[not a]


## A simple right justify label
def lbl(text):
    l = gtk.Label(text)
    l.set_justify(gtk.JUSTIFY_CENTER)
    return l


## Pack a given container in a nice frame
def myFrame(strName, container, spacing=10):
    frame = gtk.Frame(strName)
    vbox = gtk.VBox(False, spacing)
    vbox.set_border_width(spacing)
    vbox.pack_start(container)
    frame.add(vbox)
    return frame

