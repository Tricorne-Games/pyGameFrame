#!/usr/bin/env python3

"""contextmenu

This file is for a test context menu.

The idea is to separate components of an application
into all their own files so they can be worked on separately
and not cloud up other components.

For a list of wx IDs, useful for menus/icons:
https://wxpython.org/Phoenix/docs/html/stock_items.html#stock-items
https://wxpython.org/Phoenix/docs/html/wx.ArtProvider.html#wx-artprovider"""

# Import built-in libraries.
pass

# Import supplementary libraries.
import wx

# Import local modules.
pass





# TEST
class ContextMenu(wx.Menu):
    def __init__(self):
        wx.Menu.__init__(self)
        # Prepare
        self.Exit = wx.MenuItem(self, wx.ID_EXIT, 'E&xit', "Exit.")
        # Adjustments
        self.Exit.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_INFORMATION))
        # Build
        self.AppendSeparator()
        self.Append(self.Exit)
