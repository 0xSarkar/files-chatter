import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

### === Widget Event Handlers === ###

def send_btn_click():
    print("Button clicked!")

def chatbox_select_all(event):
    txt_chatbox.tag_add(tk.SEL, "1.0", tk.END)
    return "break"

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
style = ttk.Style()
style.theme_use("clam")


## === Widgets === ###

# Conversation Text
txt_conv = tk.scrolledtext.ScrolledText(
    root,
    height=5,
    width=52,
    wrap=tk.WORD,
    spacing1=10,
    spacing2=4,
    highlightthickness=0,  # Remove the focus border
    bd=0,  # Remove the border
    relief=tk.FLAT,  # Set the relief to flat
    padx=8,
    pady=6,
)
 
Fact = """A long long very very long long very verylong long very very long long very very sentence.
A man can be arrested in Italy for wearing a skirt in public."""

txt_conv.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Insert The Fact.
txt_conv.insert(tk.END, Fact)

txt_conv.config(
    state=tk.DISABLED,
    selectbackground="lightblue", 
    inactiveselectbackground="lightblue",
)

# Chat box
txt_chatbox = tk.scrolledtext.ScrolledText(root, height=3, width=1)
txt_chatbox.grid(row=1, column=0, padx=(8, 2), pady=8, sticky="nsew")

# Bind Ctrl+A to select all text
txt_chatbox.bind("<Control-a>", chatbox_select_all)

# Send Button
btn_send = ttk.Button(root, text="Send", command=send_btn_click)
btn_send.grid(row=1, column=1, padx=(2, 8), pady=8, sticky="nsew")


### === Grid Configuration === ###

# Set column weights to make them resize proportionally
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

# Configure row 0 to expand vertically
root.grid_rowconfigure(0, weight=1)

# Start the main event loop
root.mainloop()