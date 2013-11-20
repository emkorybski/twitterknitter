import wx

class tkApp(wx.App):
   def OnInit(self):
       self.frame = tkMainFrame(None, title="Twitter Knitter GUI Console")
       self.SetTopWindow(self.frame)
       self.frame.Show()
       
       return True

class tkMainFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name="Twitter Knitter GUI Console"):
        super(tkMainFrame, self).__init__(parent, id, title,
                                      pos, size, style, name)
        # Attributes
        self.panel = wx.Panel(self)
        #self.panel.SetBackgroundColour(wx.GREEN)
        button = wx.Button(self.panel,
                                label="Search for Twit",
                                pos=(30, 150))
        self.btnId = button.GetId()
        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton, button)
        
        
    def OnButton(self, event):
        """Called when the Button is clicked"""
        print "\nFrame GetChildren:"
        for child in self.GetChildren():
            print "%s" % repr(child)
            
        print "\nPanel FindWindowById:"
        button = self.panel.FindWindowById(self.btnId)
        print "%s" % repr(button)
        # Change the Button's label
        button.SetLabel("Changed Label")
        
        print "\nButton GetParent:"
        panel = button.GetParent()
        print "%s" % repr(panel)
        
        print "\nGet the Application Object:"
        app = wx.GetApp()
        print "%s" % repr(app)
        
        print "\nGet the Frame from the App:"
        frame = app.GetTopWindow()
        print "%s" % repr(frame)    
        
        
if __name__ == "__main__":
    app = tkApp(False)
    app.MainLoop()