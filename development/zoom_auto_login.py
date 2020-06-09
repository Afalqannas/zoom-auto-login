from selenium import webdriver
import tkinter as tk
from datetime import datetime
from threading import Timer
import os


root= tk.Tk()
root.title('Open Zoom Automatically')
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

# Zoom link
label1 = tk.Label(root, text= 'Enter Zoom link', fg='blue')
canvas1.create_window(200, 60, window=label1)

entry1 = tk.Entry (root)
canvas1.create_window(200, 80, window=entry1)

# Time
label2 = tk.Label(root, text= 'Enter Time : Example: 23:01', fg='blue')
canvas1.create_window(200, 120, window=label2)

entry2 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry2)

label3 = tk.Label(root, text= '')
canvas1.create_window(200, 230, window=label3)

# Requirements
label4 = tk.Label(root, text= '**This program requires installation of Firefox browser**', fg='red')
canvas1.create_window(200, 280, window=label4)

def zoom_timer (event=None):  # event for <enter> button
    '''Function takes URL and TIME then will open the given URL at the given time'''
    zoom_link = entry1.get()
    start_time = entry2.get()
    if zoom_link == "" or start_time == "":
        label3.config(text='Please enter URL and Time')
    else:
        start_time = start_time.split(':')
        hour = start_time[0]
        minutes = start_time[1]
        label3.config(text=f'Go to sleep I will open Zoom at {hour}:{minutes}')
        x=datetime.today()
        y=x.replace(day=x.day+1, hour=int(hour), minute=int(minutes), second=0, microsecond=0)
        delta_t=y-x
        secs=delta_t.seconds+1
        def job():
            label3.config(text='Opening Zoom ...')
            fp = webdriver.FirefoxProfile('o253xtdm.zoom_auto')
            driver = webdriver.Firefox(executable_path='firefox_driver/geckodriver', firefox_profile=fp,
                                   service_log_path=os.devnull) # os.devnull will disable logs
            driver.get(zoom_link)
            return
    
        t = Timer(secs, job)
        t.start()

button1 = tk.Button(text='START', command=zoom_timer)
canvas1.create_window(200, 180, window=button1)

root.bind('<Return>', zoom_timer)
root.mainloop()

os._exit(1)   # to close the program from background processes in task manager

#zoom URL sample: https://zoom.us/j/98297230478?pwd=QVJKbThaQzNBdXFIQ3FON1pPM3dKUT09
