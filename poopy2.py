import tkinter as tk
from tkinter import messagebox

def show_fullscreen_alert():
    root = tk.Tk()
    root.title("Security Alert")
    root.attributes('-fullscreen', True)  # Make the window fullscreen
    root.configure(bg='red')  # Red background for warning effect

    # Display centered warning text
    label = tk.Label(
        root, 
        text="VULNERABILITY FOUND", 
        font=("Arial", 60, "bold"), 
        fg="white", 
        bg="red"
    )
    label.pack(expand=True)

    # Optional: Press ESC to close
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()

show_fullscreen_alert()
