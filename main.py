import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading

from app_menus import create_menu
from app_widgets import create_widgets
from inference_ggml import load_llm_model

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

    create_menu(root)
    create_widgets(root)

    # Use threading to load the LLM model in the background
    model_thread_event = threading.Event()  # Event to signal the thread to stop
    model_thread = threading.Thread(target=load_llm_model, args=(model_thread_event,))
    model_thread.start()

    # Function to close the window and signal the model thread to stop
    def on_closing():
        model_thread_event.set()  # Signal the thread to stop
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()