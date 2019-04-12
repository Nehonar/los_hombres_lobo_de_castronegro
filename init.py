#!/usr/bin/env python

import wx
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class MyApp(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title)
        self.Centre(True)
        self.Show()

        # create a menu bar
        self.makeMenuBar()

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        newGame = fileMenu.Append(-1, "&New Game...\tCtrl-N",
                "Start a new game")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnNewGame, newGame)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)

    def OnNewGame(self, event):
        """deal cards"""
        """"""

        img=mpimg.imread('carta.jpg')
        imgplot = plt.imshow(img)
        plt.show()

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)




if __name__=='__main__':
    app = wx.App()
    frame = MyApp(None,u"menu")
    app.MainLoop()
