import win32api
import win32gui
import win32con
import time
def enlarge():
    win32api.keybd_event(17,0,0,0) #Ctrl
    win32api.keybd_event(107,0,0,0) #+
    win32api.keybd_event(107,0,win32con.KEYEVENTF_KEYUP,0) #Realize the Ctrl button
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) #Realize the Tab button

def smaller():
    win32api.keybd_event(17,0,0,0) #Ctrl
    win32api.keybd_event(109,0,0,0) #+
    win32api.keybd_event(109,0,win32con.KEYEVENTF_KEYUP,0) #Realize the Ctrl button
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) #Realize the Tab button\
    
time.sleep(2)
smaller()
time.sleep(2)
enlarge()
