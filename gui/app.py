#!/usr/bin/env python3

"""app

This file contains the main application."""

# Import built-in libraries.
import sys

# Import supplementary Libraries.
import wx
print(wx.version())

# Import local modules.
from appframe import AppFrame





class Application(wx.App):
    """The main application."""
    def __init__(self):
        """Initialize the application."""
        wx.App.__init__(self)
        self.frame = AppFrame()
    def run(self):
        """Start the application."""
        app = wx.App(False)
        self.frame.Center()
        self.frame.Show()
        app.MainLoop()
        sys.exit(0)
