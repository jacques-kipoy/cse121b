# Grade 9 Sc Project
# Bell Alarm Project

import time
import winsound

def ring_bell():  # This is a function for the ring_bell
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

def main():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == "07:30" or current_time == "20:54":
            ring_bell()
            ring_bell()
            ring_bell()
            ring_bell()
            ring_bell()
        time.sleep(100)

if __name__ == "__main__":
    main()

# This program uses the time and winsound modules to play a sound at certain times of the day. The ring_bell() function plays a beep sound using the winsound module. The main() function runs in an infinite loop, checking the current time every 30 seconds using time.strftime(). If the current time is 8:00 AM or 1:00 PM, the ring_bell() function is called to play the sound.

# To run this program, save it as a .py file and run it from the command line using python filename.py. Note that this program is designed for Windows operating systems. If you're using a different operating system, you'll need to modify the winsound module or use a different sound-playing method.