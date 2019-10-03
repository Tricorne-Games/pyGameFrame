#!/usr/bin/env python3

"""test

This file is for a test wx frame."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import wx

# Import local modules.
from mainmenu import MainMenu
from contextmenu import ContextMenu
from testpanel import TestPanel
pass





# Set up the frame.
class AppFrame(wx.Frame):
    """The application frame."""
    def __init__(self, parent=None, title='New'):
        """Initialize the frame."""
        # Initialize
        wx.Frame.__init__(self, parent=parent, title=title)
        self.MM = MainMenu()
        
        # Menu Bar
        self.SetMenuBar(self.MM)
        
        # Panels
        self.MP = TestPanel(self)
        
        # Status Bar
        self.CreateStatusBar()

        # Bindings
        self.Bind(wx.EVT_MENU, self.exit, id=wx.ID_EXIT)

    def exit(self, event):
        """Close the frame."""
        self.Close(True)
