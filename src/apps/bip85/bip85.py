"""
Creates deterministic entropy from BIP32 keychains
"""

from app import BaseApp, AppError
from io import BytesIO
from binascii import hexlify
from gui.screens import Prompt, Menu

# Should be called App if you use a single file
class Bip85App(BaseApp):

    button = "Deterministic entropy"

    """Allows to query random bytes from on-board TRNG."""
    prefixes = [b"bip85"]

    async def process_host_command(self, stream, show_screen):
        """
        If command with one of the prefixes is received
        it will be passed to this method.
        Should return a tuple: 
        - stream (file, BytesIO etc) 
        - meta object with title and note
        """
        # reads prefix from the stream (until first space)
        prefix = self.get_prefix(stream)
        if prefix != b"bip85":
            # WTF? It's not our data...
            raise AppError("Prefix is not valid: %s" % prefix.decode())
        name = stream.read().decode()
        # ask the user if he really wants it
        # build a screen
        scr = Prompt("Say hello?", 
                     "Are you sure you want to say hello to\n\n%s?\n\n"
                     "Saying hello can compromise your security!"
                     % name)
        # show screen and wait for result
        res = await show_screen(scr)
        # check if he confirmed
        if not res:
            return
        obj = {
            "title": "Hello!",
        }
        d = b"Hello " + name.encode()
        return BytesIO(d), obj

    async def menu(self, show_screen, show_all=False):
        buttons = [
            (None, "Recommended"),
            (39, "BIP39"),
            (None, "Other"),
            (2, "WIF"),
            (32, "XPRV"),
            (128169, "HEX"),
            # (None, "Advanced"),
            # (128169, "RSA"),
            # (83696968, "RSA-GPG2")
        ]

        # wait for menu selection
        menuitem = await show_screen(Menu(buttons, last=(255, None),
                                          title="Select the applicaion",
                                          note="Several applications are defined in BIP85"))

        # process the menu button:
        # back button
        if menuitem == 255:
            return False
        elif menuitem == 39:
            return False
        elif menuitem == 2:
            return False
        elif menuitem == 32:
            return False
        elif menuitem == 128169:
            return False
        else:
            return False
