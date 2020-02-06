from sikuli import *
from _uimap import *


class Browser(object):
    @classmethod
    def Start(self, url):
        type('r', Key.WIN)
        type("chrome " + url)
        type(Key.ENTER)
        wait(Browser_UI.button_Refresh, 5)

    @classmethod
    def Maximize(self):
        type(Key.SPACE, Key.ALT)
        type('x')

    @classmethod
    def OpenNewTab(self):
        type('t', Key.CTRL)

    @classmethod
    def OpenURL(self, url):
        type('d', Key.ALT)
        sleep(0.5)
        paste(url)
        type(Key.ENTER)

class Form_Login_UI(object):
    @classmethod
    def Start(self, url):
        type('r', Key.WIN)
        type(url)
        type(Key.ENTER)
        #wait(Form_Login_UI.button_Refresh, 5)

    @classmethod
    def Maximize(self):
        type(Key.SPACE, Key.ALT)
        type('x')
    
    @classmethod
    def ClickButton(self):
        click(Form_Login_UI.btn_Reload_Page)
        type('x')