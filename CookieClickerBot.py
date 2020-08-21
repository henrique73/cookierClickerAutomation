import PIL.ImageGrab
from ctypes import windll, Structure, c_long, byref
import win32api, win32con
import time
import threading as th
import keyboard

PIL.ImageGrab.grab().size

rgb = 0


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def input_thread(a_list):
    raw_input()
    a_list.append(True)


keep_going = True
def key_capture_thread():
    global keep_going
    a = keyboard.read_key()
    if a== "esc":
        keep_going = False


def do_stuff():
    check = 380
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    i=0
    while keep_going:
        #Upgrades
        rgb = PIL.ImageGrab.grab().load()[1612,268]
        if rgb == (2, 5, 7):
            click(1612,268)
        #Cursor
        rgb = PIL.ImageGrab.grab().load()[1809,398]
        if rgb == (148, 147, 129):
            click(1809,398)
        #Grandma
        rgb = PIL.ImageGrab.grab().load()[1824,459]
        if rgb == (141, 134, 118):
            click(1824,459)
        #Farm
        rgb = PIL.ImageGrab.grab().load()[1814,532]
        if rgb == (139, 137, 124):
            click(1814,532)
        #Mine
        rgb = PIL.ImageGrab.grab().load()[1799,597]
        if rgb == (175, 172, 155):
            click(1799,597)
        #Factory
        rgb = PIL.ImageGrab.grab().load()[1807,665]
        if rgb == (148, 145, 130):
            click(1807,665)
        #Bank
        rgb = PIL.ImageGrab.grab().load()[1797,715]
        if rgb == (145, 142, 127):
            click(1797,715)

        else:
            click(278,463)
        
        i=i+1


do_stuff()




