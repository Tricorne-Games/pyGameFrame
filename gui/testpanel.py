#!/usr/bin/env python3

"""testpanel

This file is a test panel, used for separating the
layout of the frame's widgets from the frame itself."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import wx

# Import local modules.
from contextmenu import ContextMenu





# TEST
class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        test = wx.StaticText(self, label="Test")
        test2 = wx.StaticText(self, label='Test2')
        self.CM = ContextMenu()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(test2)
        sizer.Add(test)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_CONTEXT_MENU, self.showCM)

    def showCM(self, event):
        pos = event.GetPosition()
        pos = self.ScreenToClient(pos)
        self.PopupMenu(self.CM, pos)
        # NOTE: Somehow, the Exit item in the CM cleanly quits.
