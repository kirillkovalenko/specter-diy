"""Derivation-related screens"""
import lvgl as lv
from ..common import *
from ..decorators import *
from ..components import MnemonicTable, HintKeyboard
from .screen import Screen

class DeriveMnemonicScreen(Screen):
    def __init__(self, mnemonic="", title="Create BIP39 Mnemonic", note=None):
        super().__init__()
        self.title = add_label(title, scr=self, style="title")
        if note is not None:
            lbl = add_label(note, scr=self, style="hint")
            lbl.align(self.title, lv.ALIGN.OUT_BOTTOM_MID, 0, 5)
        self.table = MnemonicTable(self)
        self.table.set_mnemonic(mnemonic)
        self.table.align(self.title, lv.ALIGN.OUT_BOTTOM_MID, 0, 30)

        self.close_button = add_button(scr=self, callback=on_release(self.release))

        self.close_label = lv.label(self.close_button)
        self.close_label.set_text("OK")
