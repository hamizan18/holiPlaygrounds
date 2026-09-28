import string as str
import tkinter as tk

def key_pressed(event):
    key = event.keysym
    letters = list(str.ascii_letters)
    
    with open("keylog.txt", "a") as file:
        if key == "Return":
            file.write("[" + key.upper() + "]" + "\n")
        elif key not in letters:
            file.write("[" + key.upper() + "] ")
        else:
            file.write(key + " ")
        
    print(f"Key pressed: {key}")
    
window = tk.Tk()
window.title("Keylogger Lab")
window.geometry("500x300")

label = tk.Label(
    window,
    text="Klik jendela ini, lalu tekan keyboard...",
    font=("Poppins", 14)
)

label.pack(pady=100)
window.bind("<Key>", key_pressed)
window.mainloop()