import tkinter as tk

def key_pressed(event):
    key = event.keysym
    
    with open("keylog.txt", "a") as file:
        if key == "space":
            file.write("[" + key.upper() + "] ")
        elif key == "BackSpace":
            file.write("[" + key.upper() + "] ")
        elif key == "Shift_L":
            file.write("[" + key.upper() + "] ")
        elif key == "Return":
            file.write("[" + key.upper() + "] ")
        elif key == "Escape":
            file.write("[" + key.upper() + "] ")
        elif key == "Shift_R":
            file.write("[" + key.upper() + "] ")
        elif key == "Home":
            file.write("[" + key.upper() + "] ")
        elif key == "Tab":
            file.write("[" + key.upper() + "] ")
        elif key == "Prior":
            file.write("[" + key.upper() + "] ")
        elif key == "Caps_Lock":
            file.write("[" + key.upper() + "] ")
        elif key == "End":
            file.write("[" + key.upper() + "] ")
        elif key == "Right":
            file.write("[" + key.upper() + "] ")
        elif key == "Down":
            file.write("[" + key.upper() + "] ")
        elif key == "Left":
            file.write("[" + key.upper() + "] ")
        elif key == "Control_R":
            file.write("[" + key.upper() + "] ")
        
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