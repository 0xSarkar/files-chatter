import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial

### === Menu Items Handlers === ###

def add_files():
    messagebox.showinfo("Add Files", "Functionality for adding files goes here")

def view_files():
    messagebox.showinfo("View Files", "Functionality for viewing files goes here")

def close_app():
    root.destroy()

def about():
    messagebox.showinfo("About", "This is a sample app created using Tkinter")

def contact():
    messagebox.showinfo("Contact", "You can reach us at contact@example.com")


### === Widget Event Handlers === ###

def send_msg(event = None):
    user_msg = txt_chatbox.get("1.0", tk.END)
    txt_conv.config(state=tk.NORMAL)
    txt_conv.insert(tk.END, user_msg)
    txt_conv.config(state=tk.DISABLED)
    txt_chatbox.delete("1.0", tk.END)  # Clear the chatbox

    # update scrollbars of conv and chatbox
    vsb_visibility(vsb_conv, txt_conv)
    vsb_visibility(vsb_chatbox, txt_chatbox)

    return "break"

def chatbox_select_all(event):
    txt_chatbox.tag_add(tk.SEL, "1.0", tk.END)
    return "break"

def chatbox_update(event):
    print(event.state)
    vsb_visibility(vsb_chatbox, txt_chatbox)

def handle_tab(event):
    event.widget.tk_focusNext().focus()
    return "break"  # Prevent default tab behavior

def vsb_visibility(vsb_widget, txt_widget, event=None):
    xview = txt_widget.xview()
    yview = txt_widget.yview()
    if xview != (0.0, 1.0) or yview != (0.0, 1.0):
        vsb_widget.grid()  # Show the vertical scrollbar
    else:
        vsb_widget.grid_remove()  # Hide the vertical scrollbar
 
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

### === Menu bar === ###

menu_bar = tk.Menu(root)

# Files menu
files_menu = tk.Menu(menu_bar, tearoff=0)
files_menu.add_command(label="Add Files", command=add_files)
files_menu.add_command(label="View Files", command=view_files)
files_menu.add_separator()
files_menu.add_command(label="Close", command=close_app)
menu_bar.add_cascade(label="Files", menu=files_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Contact", command=contact)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

## === Conversation Area Widgets === ###

# Frame for Conversation Text
frame_conv = ttk.Frame(root)

# Conversation Text
txt_conv = tk.Text(
    frame_conv,
    height=5,
    width=52,
    wrap=tk.WORD,
    spacing1=10,
    spacing2=4,
    highlightthickness=0,  # Remove the focus border
    bd=0,  # Remove the border
    relief=tk.FLAT,  # Set the relief to flat
    padx=12,
    pady=6,
)

txt_conv.grid(row=0, column=0, sticky="nsew")

txt_conv_font = ("Arial", 12)
txt_conv.configure(font=txt_conv_font)

first_bot_msg = """Hi! 
- You can add new files to this chat by clicking on Files -> Add Files menu placed at the top left corner.
- You can start a new chat by clicking on Chats -> New Chat
- Type your messages in the text box at the bottom. Hit enter to send message or shift+enter to add a new line to your message.
"""

bot_name = "Bot:\n"
user_name = "User:\n"

txt_conv.tag_configure("bold", font=("Helvetica", 12, "bold"))
txt_conv.insert(tk.INSERT, bot_name, "bold")
txt_conv.insert(tk.INSERT, first_bot_msg)

vsb_conv= ttk.Scrollbar(frame_conv, orient='vertical', command=txt_conv.yview)
vsb_conv.grid(row=0, column=1, sticky="ns")
vsb_conv.grid_remove()  # Hide the scrollbar initially

txt_conv['yscrollcommand'] = vsb_conv.set
txt_conv.bind("<KeyRelease>", partial(vsb_visibility, vsb_conv, txt_conv))

txt_conv.config(
    state=tk.DISABLED,
    selectbackground="lightblue", 
    inactiveselectbackground="lightblue",
)

frame_conv.grid(row=0, column=0, sticky="nsew")

# Conversation frame grid configuration
frame_conv.grid_columnconfigure(0, weight=1)
frame_conv.grid_columnconfigure(1, weight=0)
frame_conv.grid_rowconfigure(0, weight=1)


### === Chatbox Widgets === ###

frame_chat = ttk.Frame(root)

txt_chatbox = tk.Text(
    frame_chat,
    wrap=tk.WORD, 
    height=3, 
    width=1,
    spacing1=8,
    spacing2=4,
    padx=4
)
txt_chatbox.grid(row=0, column=0, padx=(8, 2), pady=8, sticky="nsew")

# Bind Ctrl+A to select all text
txt_chatbox.bind("<Control-a>", chatbox_select_all)

# Chatbox Scrollbar
vsb_chatbox= ttk.Scrollbar(frame_chat, orient='vertical', command=txt_chatbox.yview)
vsb_chatbox.grid(row=0, column=1, padx=(0, 2), pady=8, sticky="ns")
vsb_chatbox.grid_remove()  # Hide the scrollbar initially

txt_chatbox['yscrollcommand'] = vsb_chatbox.set
txt_chatbox.bind("<KeyRelease>", chatbox_update)
txt_chatbox.bind("<Tab>", handle_tab)
#txt_chatbox.bind("<Return>", lambda event: print("boo") if(event.state == 1) else send_msg())

# Send Button
btn_send = ttk.Button(frame_chat, text="Send", command=send_msg)
btn_send.grid(row=0, column=2, padx=(2, 8), pady=8, sticky="nsew")

btn_send.bind("<Return>", send_msg)

frame_chat.grid(row=1, column=0, sticky="nsew")

# Chat frame grid configuration
frame_chat.grid_columnconfigure(0, weight=1)
frame_chat.grid_columnconfigure(1, weight=0)
frame_chat.grid_columnconfigure(2, weight=0)


### === Root Grid Configuration === ###

# Set column weights to make them resize proportionally
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)

# Start the main event loop
root.mainloop()
