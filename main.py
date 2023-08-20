import tkinter as tk
from tkinter import ttk

def button_click():
  print("Button clicked!")

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

# Set the theme
style = ttk.Style()
style.theme_use("clam")


# Create the Text area
text_area = tk.Text(root, height=3, width=1)
text_area.grid(row=0, column=0, padx=(8, 2), pady=8, sticky="nsew")

# Add a Scrollbar(vertical) for Text Area
text_area_scrollbar= ttk.Scrollbar(root, orient='vertical', command=text_area.yview)
text_area_scrollbar.grid(row=0, column=1, padx=(0, 2), pady=8, sticky="nsew")

text_area['yscrollcommand'] = text_area_scrollbar.set

# Create the Button
button = ttk.Button(root, text="Send", command=button_click)
button.grid(row=0, column=2, padx=(2, 8), pady=8, sticky="nsew")

# Set column weights to make them resize proportionally
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)

# Start the main event loop
root.mainloop()
