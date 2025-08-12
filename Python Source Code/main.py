# Imports
from os import system
from webbrowser import open as open_website
from threading import Thread
from time import sleep

def open_website():
    """
    Opens 10 rickroll tabs in the default browser, forever changing the
    victim's life.
    """
    times = 10 # Number of times to open the website
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # Rickroll url
    urls = [url for i in range(times)] # List of 10 rickroll urls
    for url in urls:
        open_website(url)

def main():
    """
    The main function of the program. It clears the console, prints a
    title, and prints "YOU ARE STUPID!" to the console. It then prints
    out an ascii art and starts 10 threads to open the rickroll url in
    the default browser.

    Parameters:
        None

    Returns:
        None
    """
    # Enabling use of ansi escape sequences
    system("")

    # Set the title of the console
    system('echo "\033]0;You Stoopid\007"')

    # Clear the console
    system("cls")

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

# Run the main function
if __name__ == "__main__":
    main()
