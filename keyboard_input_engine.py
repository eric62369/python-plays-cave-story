# From https://www.cs.unc.edu/~gb/blog/2007/11/16/sending-key-events-to-pygame-programs/
from ctypes import *
import time
import os

# Constants for controls
CONTROLS = {
    'LEFT': 'a',
    'UP': 'w',
    'RIGHT': 'd',
    'DOWN': 's',

    'JUMP': 'k',
    'FIRE': 'j',
    'PREVIOUS_WEAPON': 'u',
    'NEXT_WEAPON': 'i',
    'INVENTORY': 'o',
    'OPEN_MAP': 'p'
}

if os.name == 'nt':
    PUL = POINTER(c_ulong)
    class KeyBdInput(Structure):
        _fields_ = [("wVk", c_ushort),
                    ("wScan", c_ushort),
                    ("dwFlags", c_ulong),
                    ("time", c_ulong),
                    ("dwExtraInfo", PUL)]

    class HardwareInput(Structure):
        _fields_ = [("uMsg", c_ulong),
                    ("wParamL", c_short),
                    ("wParamH", c_ushort)]

    class MouseInput(Structure):
        _fields_ = [("dx", c_long),
                    ("dy", c_long),
                    ("mouseData", c_ulong),
                    ("dwFlags", c_ulong),
                    ("time",c_ulong),
                    ("dwExtraInfo", PUL)]

    class Input_I(Union):
        _fields_ = [("ki", KeyBdInput),
                    ("mi", MouseInput),
                    ("hi", HardwareInput)]

    class Input(Structure):
        _fields_ = [("type", c_ulong),
                    ("ii", Input_I)]

    KEYEVENTF_KEYUP = 0x2
    KEYEVENTF_UNICODE = 0x4
    KEYEVENTF_SCANCODE = 0x8
    MAPVK_VK_TO_VSC = 0

    def SendInput(txt):
        i = Input()
        i.type = 1
        extra = c_ulong(0)
        pextra = pointer(extra)
        for c in txt:
            vk = windll.user32.VkKeyScanW(ord(c))
            sc = windll.user32.MapVirtualKeyW(vk&0xff, MAPVK_VK_TO_VSC)
            i.ii.ki.wVk = 0
            i.ii.ki.wScan = sc
            i.ii.ki.dwFlags = KEYEVENTF_SCANCODE
            i.ii.ki.time = 0
            i.ii.ki.dwExtraInfo = pextra
            windll.user32.SendInput(1, byref(i), sizeof(i))
            i.ii.ki.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP
            windll.user32.SendInput(1, byref(i), sizeof(i))

    def SendKeyPress(key):
        i = Input()
        i.type = 1
        extra = c_ulong(0)
        pextra = pointer(extra)
        vk = windll.user32.VkKeyScanW(ord(key))
        sc = windll.user32.MapVirtualKeyW(vk&0xff, MAPVK_VK_TO_VSC)
        i.ii.ki.wVk = 0
        i.ii.ki.wScan = sc
        i.ii.ki.dwFlags = KEYEVENTF_SCANCODE
        i.ii.ki.time = 0
        i.ii.ki.dwExtraInfo = pextra
        windll.user32.SendInput(1, byref(i), sizeof(i))

    def SendKeyRelease(key):
        i = Input()
        i.type = 1
        extra = c_ulong(0)
        pextra = pointer(extra)
        vk = windll.user32.VkKeyScanW(ord(key))
        sc = windll.user32.MapVirtualKeyW(vk&0xff, MAPVK_VK_TO_VSC)
        i.ii.ki.wVk = 0
        i.ii.ki.wScan = sc
        i.ii.ki.time = 0
        i.ii.ki.dwExtraInfo = pextra
        i.ii.ki.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP
        windll.user32.SendInput(1, byref(i), sizeof(i))


elif os.name == 'posix':
    Xtst = CDLL("libXtst.so.6")
    Xlib = CDLL("libX11.so.6")
    dpy = Xtst.XOpenDisplay(None)
    def SendInput( txt ):
        for c in txt:
            sym = Xlib.XStringToKeysym(c)
            code = Xlib.XKeysymToKeycode(dpy, sym)
            Xtst.XTestFakeKeyEvent(dpy, code, True, 0)
            Xtst.XTestFakeKeyEvent(dpy, code, False, 0)
        Xlib.XFlush(dpy)

    '''Take in a key (Z, X, J) etc. and execute a key press of it'''
    def SendKeyPress(key):
        sym = Xlib.XStringToKeysym(str(key))
        code = Xlib.XKeysymToKeycode(dpy, sym)
        Xtst.XTestFakeKeyEvent(dpy, code, True, 0)
        Xlib.XFlush(dpy)

    def SendKeyRelease(key):
        sym = Xlib.XStringToKeysym(str(key))
        code = Xlib.XKeysymToKeycode(dpy, sym)
        Xtst.XTestFakeKeyEvent(dpy, code, False, 0)
        Xlib.XFlush(dpy)

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
if (__name__ == '__main__'):
    while (True):
        SendKeyPress(CONTROLS['FIRE'])
        time.sleep(0.5)
        SendKeyRelease(CONTROLS['FIRE'])
        time.sleep(0.5)