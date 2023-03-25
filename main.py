# > Import KivyMD
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
# > Import Kivy
from kivy.clock import Clock, ClockBase
from kivy.lang import Builder
from kivy.core.window import Window, WindowBase
from kivy.core.text import LabelBase
from kivy.properties import StringProperty, NumericProperty
# > Import Typing
from typing import Any, Union
# > Local Imports
from chatGPT import chat_message
from functions import get_asset_path
from unitsdata import *
# > Another Import
from translate import Translator
# > Windows Settings
Window: WindowBase
Clock: ClockBase

Window.size = WINDOW_SIZE
Window.icon = get_asset_path("icons/icon.png")

# > Classes
class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "MontReg"
    font_size = 17

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "MontReg"
    font_size = 17

# > Chat Class
class Chat:
    def __init__(self, screen: MDScreen) -> None:
        self.ms = screen
        self.val_gpt = ""
        self.val_trans = ""
    
    def add_msg(self, obj: Union[Response, Command]) -> None:
        self.ms.chat_list.add_widget(obj)
    
    def responce_gpt(self, *args):
        if self.val_gpt != "":
            tr = Translator(from_lang='Russian', to_lang='English')
            responce = chat_message(tr.translate(self.val_gpt))
            self.add_msg( Response(text=responce, size_hint_x=.75) )
            self.ms.state.text = "Online"

    def responce_trans(self, *args):
        try:
            if self.val_trans != "":
                tr = Translator(from_lang='russian', to_lang='english')
                responce = tr.translate(self.val_trans)
                self.add_msg(Response(text=responce, size_hint_x=.75) )
                self.ms.state.text = "Online"
        except: pass

    def send_gpt(self, *args: Any):
        if self.ms != "":
            print(self.ms.text_input_1.text)
            self.val_gpt = self.ms.text_input_1.text
            if self.val_gpt != "":
                lv = len(self.val_gpt)
                
                if lv < 6:      size, halign = .22, "center"
                elif lv < 11:   size, halign = .32, "center"
                elif lv < 16:   size, halign = .45, "center"
                elif lv < 21:   size, halign = .58, "center"
                elif lv < 26:   size, halign = .71, "center"
                else:           size, halign = .77, "left"
                
                self.ms.state.text = "typing..."
                self.add_msg(Command(text=self.val_gpt, size_hint_x=size, halign=halign))
                Clock.schedule_once(self.responce_gpt, 1)
                self.ms.text_input_1.text = ''
    
    def send_trans(self, *args: Any):
        if self.ms != "":
            self.val_trans = self.ms.text_input_2.text
            if self.val_trans != "":
                lv = len(self.val_trans)
                
                if lv < 6:      size, halign = .22, "center"
                elif lv < 11:   size, halign = .32, "center"
                elif lv < 16:   size, halign = .45, "center"
                elif lv < 21:   size, halign = .58, "center"
                elif lv < 26:   size, halign = .71, "center"
                else:           size, halign = .77, "left"
                
                self.ms.state.text = "typing..."
                self.add_msg(Command(text=self.val_trans, size_hint_x=size, halign=halign))
                Clock.schedule_once(self.responce_trans, 1)
                self.ms.text_input_2.text = ''
    
    def add(self, *args: Any) -> None: pass

# > Main Class
class MeSure(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.screen_manager = MDScreenManager()
    
    def change_screen(self, name: str):
        self.screen_manager.current = name

    def build(self):
        self.title = WINDOW_TITLE

        
        self.screen_manager.add_widget(Builder.load_file(get_asset_path("GPT.kv")))
        self.screen_manager.add_widget(Builder.load_file(get_asset_path("Translate.kv")))


        self.chat_control = Chat(self.screen_manager.get_screen('GPT'))
        self.chat_control = Chat(self.screen_manager.get_screen('trans'))

        return self.screen_manager

# > Starting
if __name__ == '__main__':
    LabelBase.register(name="MontReg", fn_regular=get_asset_path("Montserrat-Regular.ttf"))
    LabelBase.register(name="MontSem", fn_regular=get_asset_path("Montserrat-SemiBold.ttf"))
    MeSure().run()
