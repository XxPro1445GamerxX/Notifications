from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
import schedule

class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
           hicon = LoadImage(hinst, iconPathName, \
                    win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
          hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                          hicon, "Balloon  tooltip",title,200,msg))
        # self.show_balloon(title, msg)
        time.sleep(10)
        DestroyWindow(self.hwnd)
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.
def balloon_tip(title, msg):
    w=WindowsBalloonTip(msg, title)
#Makes the message and title
try:
    title = input('Enter the title: ').lower()
    mess = input('Enter the main message: ')
    curr = input('Do you want to have this event take place today or tmmr?: ')
    if curr == 'tmmr' or curr == 'tommorow':
        new_time = time.ctime()
        if 'Sat' in new_time:
            curr = 'sunday'
        elif 'Mon' in new_time:
            curr = 'tuesday'
        elif 'Tues' in new_time:
            curr = 'wednesday'
        elif 'Wed' in new_time:
            curr = 'thursday'
        elif 'Thurs' in new_time:
            curr = 'friday'
        elif 'Fri' in new_time:
            curr = 'saterday'
        elif 'Sun' in new_time:
            curr = 'monday'
    else:
        curr = 'day'
    #If the title and or msg were left blank, the code will nit run. This makes it so the title and or msg are not left blank.
    if title == '':
        title = 'None'
    if mess == '':
        mess = 'None'
    def runner():
    #Obtains the title and msg
        global title
        global mess
        balloon_tip(title, mess)
        #quits the app after the msg's are sent
        sys.exit()
    def inputer():
        global curr
        all_ = input('Enter the time and the time of day exp.(9:45pm):').lower()
        hour = (all_[0])
        if int(hour) > 0:
            hour = (all_[0])
            minute = (all_[2])
            minute2 = (all_[3])
            colen = (all_[1])
            try:
                pam = (all_[4])
                pam2 = (all_[5])
            except:
                pam = 'p'
                pam2 = 'm'
        #Sorts into more genral catigories 
            hour = (hour)
            minute = (minute + minute2)
            colen = (colen)
            pam = (pam + pam2)
            if pam == 'pm':
                #Checks if the time is 24 if it is than switches it to 00
                if (hour) == '12':
                    hour = '00'
                else:
                    hour = int(hour)
                    hour = hour + 12
                    hour = str(hour)
        #switches everything back to an str if og was int
            hour = str(hour)
            minute = str(minute)
            colen = str(colen)

            all1 = (hour + colen + minute)
            print(all1)
            # all1 is the hour colen and min put together so the schedule module will work
            if curr == 'day':
                schedule.every().day.at(all1).do(runner)
            elif curr == 'monday':
                print(curr)
                schedule.every().monday.at(all1).do(runner)
            elif curr == 'sunday':
                print(curr)
                schedule.every().sunday.at(all1).do(runner)
            elif curr == 'tuesday':
                print(curr)
                schedule.every().tuesday.at(all1).do(runner)
            elif curr == 'wednesday':
                print(curr)
                schedule.every().wednesday.at(all1).do(runner)
            elif curr == 'thursday':
                print(curr)
                schedule.every().thursday.at(all1).do(runner)
            elif curr == 'friday':
                print(curr)
                schedule.every().friday.at(all1).do(runner)
            elif curr == 'saterday':
                print(curr)
                schedule.every().saterday.at(all1).do(runner)
        else:
        #sorts into catigories
            hour = (all_[0])
            hour2 = (all_[1])
            minute = (all_[3])
            minute2 = (all_[4])
            colen = (all_[2])
            try:
                pam = (all_[5])
                pam2 = (all_[6])
            except:
                pam = 'p'
                pam2 = 'm'
        #Sorts into more genral catigories 
            hour = (hour + hour2)
            minute = (minute + minute2)
            colen = (colen)
            pam = (pam + pam2)
            if pam == 'pm':
                #Checks if the time is 24 if it is than switches it to 00
                if (hour) == '12':
                    hour = '00'
                else:
                    hour = int(hour)
                    hour = hour + 12
                    hour = str(hour)
        #switches everything back to an str if og was int
            hour = str(hour)
            minute = str(minute)
            colen = str(colen)

            all1 = (hour + colen + minute)
            print(all1)
            # all1 is the hour colen and min put together so the schedule module will work
            if curr == 'day':
                schedule.every().day.at(all1).do(runner)
            elif curr == 'monday':
                print(curr)
                schedule.every().monday.at(all1).do(runner)
            elif curr == 'sunday':
                print(curr)
                schedule.every().sunday.at(all1).do(runner)
            elif curr == 'tuesday':
                print(curr)
                schedule.every().tuesday.at(all1).do(runner)
            elif curr == 'wednesday':
                print(curr)
                schedule.every().wednesday.at(all1).do(runner)
            elif curr == 'thursday':
                print(curr)
                schedule.every().thursday.at(all1).do(runner)
            elif curr == 'friday':
                print(curr)
                schedule.every().friday.at(all1).do(runner)
            elif curr == 'saterday':
                print(curr)
                schedule.every().saterday.at(all1).do(runner)
        #Runs code
    inputer()
        #Runs the schedule and the time module
    while True:
        schedule.run_pending()
        time.sleep(1)
except ValueError:
    print('\nCheck That you put a valid time emp.(12:45pm)\n\nCommom error is you forgot the pm or am\n\nRestarting the program')
    inputer()
    
