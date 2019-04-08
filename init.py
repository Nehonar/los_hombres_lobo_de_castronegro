import wx

class MyApp(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MyApp(None,u"menu")
    app.MainLoop()
