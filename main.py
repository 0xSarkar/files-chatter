import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial

from app_menus import create_menu
from app_widgets import create_widgets


def main():
    ### === Root Window === ###

    # Create the main application window
    root = tk.Tk()
    root.title("Files Chatter")
    root.geometry("550x650")

    # Calculate the position to center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 500
    window_height = 600
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set the window position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Use the "calm" theme
    #style = ttk.Style()
    #style.theme_use("clam")

    create_menu(root)
    create_widgets(root)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()