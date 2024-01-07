import time
import playsound

def ring_bell(sound_file):
    playsound.playsound(sound_file)

def main():
    sound_file = "path/to/your/sound/file.mp3"  # replace with the path to your sound file
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == "08:00" or current_time == "13:00":
            ring_bell(sound_file)
        time.sleep(30)

if __name__ == "__main__":
    main()


# In this modified version of the code, we're using the playsound module to play a sound file instead of winsound. The ring_bell() function takes a sound_file parameter, which is the path to your sound file. The main() function initializes the sound_file variable with the path to your sound file and calls the ring_bell() function with this variable when it's time to play the sound.

# Make sure to replace "path/to/your/sound/file.mp3" with the actual path to your sound file on your computer. Note that the playsound module can play a variety of audio file formats, including MP3, WAV, and OGG.

# ex "C:/Users/Lap Kipoy/AppData/Local/Programs/Python/Python311/python.exe" 