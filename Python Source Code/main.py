# Imports
from os import system
from ctypes import WinDLL, windll
from webbrowser import open as open_website
from threading import Thread
from time import sleep

def open_website():
    """
    Opens 10 rickroll tabs in the default browser, forever changing the
    victim's life.
    """
    times = 10 # Number of times to open the website using a single thread.
    for i in range(times):
    	open_website("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Get the user32 and kernel32
user32 = WinDLL("user32", use_last_error=True)
kernel32 = windll.kernel32

# Get the current foreground window and the current console window
active_window = user32.GetForegroundWindow()
current_window = kernel32.GetConsoleWindow()

# Enabling use of ansi escape sequences
system("")

# Set the title of the console
system('echo "\033]0;You Stoopid\007"')

# Clear the console
system("cls")

# Make the window fullscreen
user32.ShowWindow(current_window, 3)

# Get the screen width and height
screen_width = user32.GetSystemMetrics(0)
screen_height =  user32.GetSystemMetrics(1)

# Set the new window position and size
x, y, width, height = screen_width//2-(screen_width//4), screen_height//2-(screen_height//4), screen_width//2, screen_height//2

# Move the window
user32.MoveWindow(current_window, x, y, width, height, True)

# Calling the frinnd stupid
delay = 1.5
text = ["YOU", "ARE", "STUPID!"]

for i in text:
    print(i)
    sleep(delay)

# Clear the console
system("cls")

# Print the ascii art
print("""
                      █████████
  ███████          ███         ███
  █      █       ███             ███
   █      █    ██                  ██
    █     █   ██     ██      ██     ███
    █    █   ██     ████    ████      ██
   █████████████                      ██
   █            █         █           ██
 ██             █   ██          ██    ██
██   ███████████     ██        ██     ██
█               █      ████████       ██
██              █                     ██
 █   ███████████                     ██
 ██          ████                  ██
  ████████████   ██████████████████
""")


NumberOfThreads = 10 # Set the number of threads
threads = [] # Set a list for the threads

# Create the threads
for i in range(NumberOfThreads):
    # Create the thread and add it to the list
    threads.append(Thread(target=open_website))
    
	# Start the thread
    threads[i].start()
