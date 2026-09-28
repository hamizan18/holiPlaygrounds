import tkinter as tk

def key_pressed(event):
    key = event.keysym
    
    with open("keylog.txt", "a") as file:
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