import win32gui, time, keyboard, configparser
from playsound import *

config = configparser.ConfigParser()
config.read("config.ini")
game = config["DEFAULT"]["game"]
print(game)


def check_win():
    on = 1
    while True:
        time.sleep(1)
        if keyboard.is_pressed("shift+insert"):
            for i in range(3):
                playsound("beep.mp3")
            keyboard.release("end")    
            break
        elif keyboard.is_pressed("insert"):
                if on == 1:
                    on = 0
                    playsound("beep.mp3")
                elif on == 0:
                    on = 1
                    for i in range(2):
                        playsound("beep.mp3")

        if on == 1:
            now_active_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if now_active_window_name == game:
                
                keyboard.press("end")
        elif on == 0:
            keyboard.release("end")
check_win()