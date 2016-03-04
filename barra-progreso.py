#!usr/bin/env Python

# -*- coding: utf-8 -*-

from gi.repository import GLib
from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):
    # a window

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Reparando Dispositivo. Sea Paciente", application=app)
        self.set_default_size(550, 20)

        # a progressbar
        self.progress_bar = Gtk.ProgressBar()
        # add the progressbar to the window
        self.add(self.progress_bar)

        # the method self.pulse is called each 100 milliseconds
        # and self.source_id is set to be the ID of the event source
        # (i.e. the bar changes position every 100 milliseconds)
        self.source_id = GLib.timeout_add(100, self.pulse)

        # source function
    # the progressbar is in "activity mode" when this method is called
    def pulse(self):
        self.progress_bar.pulse()
        # call the function again
        return True


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
