#!/usr/bin/env python3

"""mainmenu

This file is the main menu, at the top of the application."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import wx

# Import local modules.
pass





class MainMenu(wx.MenuBar):
    """The Main Menu."""
    def __init__(self):
        """Initialize the Main Menu."""
        wx.MenuBar.__init__(self)
        # Prepare
        self.File = FileMenu()
        # Build
        self.Append(self.File, '&File')

class FileMenu(wx.Menu):
    """The File Menu."""
    def __init__(self):
        """Initialize the File Menu."""
        wx.Menu.__init__(self)
        # Prepare
        self.New = wx.MenuItem(self, wx.ID_NEW, 'New', "New file.") # Placeholder Item
        self.Open = wx.MenuItem(self, wx.ID_OPEN, 'Open', "Open file.") # Placeholder Item
        self.Exit = wx.MenuItem(self, wx.ID_EXIT, 'E&xit', "Exit.") # Functioning Menu Item
        # Adjustments
        self.Exit.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_WARNING))
        # Build
        self.Append(self.New)
        self.Append(self.Open)
        self.AppendSeparator()
        self.Append(self.Exit)
