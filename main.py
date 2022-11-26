import monitor
import upload
import globals

import time
from pynput import keyboard

from ctypes import windll

#import spammer

from pynput import keyboard

if globals.dbg:
                print("ShitX starting - globals loaded")
                print("url: ",globals.url,"psswd: ", globals.passwd)





def main():

#   delay = "2"
#
#    num = False
#
#    while num == False:
#       if delay.isnumeric():
#           print(delay)
#           num = True
#      else:
#          print("input wasnt numeric")
#           delay = input()



    if globals.monitoron:


        curr = monitor.clipboard_mon()

        if curr:
                #print(upload.user_upload('temp_image.jpg'))
                print(curr)
                time.sleep(2)#no spam
                if windll.user32.OpenClipboard(None):
                        windll.user32.EmptyClipboard()
                        windll.user32.CloseClipboard()

                #globals.monitoron = False
                return True


        elif monitor.clipboard_mon() == 0:
                time.sleep(1)#no spam
                print("err: no image in clipboard - yet (await) - scuffed")
                if globals.monitoron:

                    main()
                else:
                    return True

        #elif globals.dbg:
        #    print("win key not hit innit")
        #    globals.monitoron = False
        #   return False




###########################


def on_activate():
    print('Global hotkey activated!')
    globals.monitoron = True
    if main():
        globals.monitoron = False
        print(upload.user_upload('temp_image.jpg'))
    else:
        print("error")


def on_quit():
    exit()

#def for_canonical(f):
#    return lambda k: f(l.canonical(k))

#hotkey = keyboard.HotKey(
#    keyboard.HotKey.parse('<cmd>+<shift>+s'),
#    on_activate)

#with keyboard.Listener(
#        on_press=for_canonical(hotkey.press),
#        on_release=for_canonical(hotkey.release)) as l:
#   l.join()




with keyboard.GlobalHotKeys({
        '<cmd>+<shift>+s': on_activate,
        '<ctrl>+c': on_quit}) as h:
        h.join()
