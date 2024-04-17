import wx
from pyupdater.client import Client as PyUpdaterClient

def get_client_config():
    # Set up a dictionary for client configuration
    client_config = {
        'APP_NAME': 'MyApp',
        'APP_VERSION': '1.0.0',
        'UPDATE_URLS': ['http://example.com/updates/']
    }
    return client_config

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(300, 200))
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_hello = wx.StaticText(panel, label="Hello, World!")
        sizer.Add(self.text_hello, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(sizer)
        self.Show(True)

class MyApp(wx.App):
    def OnInit(self):
        self.init_update_check()
        frame = MainFrame(None, "Simple App")
        frame.Show()
        return True

    def init_update_check(self):
        client_config = get_client_config()
        client = PyUpdaterClient(client_config)
        client.refresh()
        app_update = client.update_check(client_config['APP_NAME'], client_config['APP_VERSION'])
        if app_update is not None and app_update.download():
            print("Update available. Please restart the application.")

def main():
    app = MyApp()
    app.MainLoop()

if __name__ == "__main__":
    main()
