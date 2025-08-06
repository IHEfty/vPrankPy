## vPrankPy/Scam Baiter Prototype – Educational Tool

### ❗️DISCLAIMER:

This tool is strictly for **educational purposes** and **ethical scambaiting** only. It is **not intended** for illegal use. Do not use it without consent in real environments. The author takes **no responsibility** for misuse.

---

### 📌 Why I Made This

I was inspired by [Scammer Payback](https://www.youtube.com/c/ScammerPayback), a YouTube channel that fights scammers by turning the tables exposing and wasting their time to protect innocent people.

In one of their videos, Scammer Payback showed how they uploaded a file to a scammer's PC to confuse and distract them while deleting stolen data. That gave me the idea to create a harmless prototype that simulates such behavior **auto-play video, disable input, and create distraction** purely for fun and ethical use in a safe, controlled environment.

---

### ⚙️ Features

* Auto-plays a local video (`video.mp4`) in full screen
* Disables keyboard and mouse temporarily
* Hides all console windows (silent execution)
* Auto-start functionality (if used responsibly)
* Built with Python and PyInstaller

---

### 🧪 Use Case

This tool is only for:

* Ethical hacking demos
* Anti-scam education
* Cybersecurity awareness labs
* Offline prank use (with permission)

**DO NOT** use this for:

* Locking down someone’s PC without consent
* Malware or ransomware behavior
* Real-world machines without explicit permission

---

### How to Build

1. Place your video file in the same folder and name it `video.mp4`.
2. Install requirements:

   ```
   pip install pillow keyboard opencv-python
   ```
3. Build the EXE:

   ```bash
   pyinstaller --onefile --noconsole --add-data "video.mp4;." --hidden-import PIL --hidden-import PIL.Image --hidden-import PIL.ImageTk main.py
   ```

---
### 💸 Donations

Want to support my learning and help me.....

> **Dogecoin address:**

```
DHERUQ8925qMWCcGzJZQe43E9yEfnpVK3p
```

Even small tips help me explore more advanced topics like encrypted shells, AV evasion, and secure coding. Thanks! 🚀🐶

---
### Credits

* Idea: Scammer Payback YouTube Channel
* Built by: \IHEfty
* Tools: Python 3.13, PyInstaller, Pillow, OpenCV, Keyboard
