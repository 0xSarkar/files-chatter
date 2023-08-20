import tkinter as tk
from tkinter import ttk

### === Widget Event Handler Functions === ###

def send_btn_click():
    print("Button clicked!")


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
txt_conv = tk.Text(
    root,
    height=5,
    width=52,
    wrap=tk.WORD,
    highlightthickness=0,  # Remove the focus border
    bd=0,  # Remove the border
    relief=tk.FLAT,  # Set the relief to flat
    padx=8,
    pady=6,
)
 
Fact = """A man can be arrested in
Italy for wearing a skirt in public."""

txt_conv.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Insert The Fact.
txt_conv.insert(tk.END, Fact)

txt_conv.config(state=tk.DISABLED, selectbackground="lightblue", inactiveselectbackground="lightblue")

# Chat box
txt_chatbox = tk.Text(root, height=3, width=1)
txt_chatbox.grid(row=1, column=0, padx=(8, 2), pady=8, sticky="nsew")

# Add a Scrollbar(vertical) for Text Area
text_area_scrollbar= ttk.Scrollbar(root, orient='vertical', command=txt_chatbox.yview)
text_area_scrollbar.grid(row=1, column=1, padx=(0, 2), pady=8, sticky="nsew")

txt_chatbox['yscrollcommand'] = text_area_scrollbar.set

# Send Button
btn_send = ttk.Button(root, text="Send", command=send_btn_click)
btn_send.grid(row=1, column=2, padx=(2, 8), pady=8, sticky="nsew")


### === Grid Configuration === ###

# Set column weights to make them resize proportionally
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)

# Configure row 0 to expand vertically
root.grid_rowconfigure(0, weight=1)

# Start the main event loop
root.mainloop()
