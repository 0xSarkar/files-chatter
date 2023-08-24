import tkinter as tk
from tkinter import messagebox

def add_files():
    messagebox.showinfo("Add Files", "Functionality for adding files goes here")

def view_files():
    messagebox.showinfo("View Files", "Functionality for viewing files goes here")

def close_app(root):
    root.destroy()

def about():
    messagebox.showinfo("About", "This is a sample app created using Tkinter")

def contact():
    messagebox.showinfo("Contact", "You can reach us at contact@example.com")

def create_menu(root):
    menu_bar = tk.Menu(root)

    # Files menu
    files_menu = tk.Menu(menu_bar, tearoff=0)
    files_menu.add_command(label="Add Files", command=add_files)
    files_menu.add_command(label="View Files", command=view_files)
    files_menu.add_separator()
    files_menu.add_command(label="Close", command=lambda: close_app(root))
    menu_bar.add_cascade(label="Files", menu=files_menu)

    # Chats menu
    chat_menu = tk.Menu(menu_bar, tearoff=0)
    chat_menu.add_command(label="New Chat", command=about)
    chat_menu.add_command(label="Open Chat", command=about)
    chat_menu.add_command(label="Save Chat", command=contact)
    menu_bar.add_cascade(label="Chats", menu=chat_menu)

    # Help menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=about)
    help_menu.add_command(label="Contact", command=contact)
    menu_bar.add_cascade(label="Help", menu=help_menu)


    root.config(menu=menu_bar)
