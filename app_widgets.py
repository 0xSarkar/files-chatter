import tkinter as tk
from tkinter import ttk

from custom_widgets.advanced_text import AdvancedText
from inference_ggml import infer

txt_conv = None
vsb_conv = None

### === Widget Event Handlers === ###

def send_msg(caller, txt_conv):
    user_msg = caller.txt.get("1.0", tk.END)

    txt_conv.config(state=tk.NORMAL)
    txt_conv.tag_configure("bold", font=("Helvetica", 12, "bold"))
    txt_conv.insert(tk.END, "\n\nUser:\n", "bold")
    txt_conv.insert(tk.END, user_msg)
    txt_conv.config(state=tk.DISABLED)

    caller.txt.delete("1.0", tk.END) # clear the chatbox
    caller.update_idletasks() # force GUI to update before calling the infer() function else text will be deleted from chatbox AFTER infer function completes

    llm_resp = infer(user_msg, txt_conv)

    return "break"

def vsb_visibility(vsb_widget, txt_widget, event=None):
    xview = txt_widget.xview()
    yview = txt_widget.yview()
    if xview != (0.0, 1.0) or yview != (0.0, 1.0):
        vsb_widget.grid()  # Show the vertical scrollbar
    else:
        vsb_widget.grid_remove()  # Hide the vertical scrollbar

def create_widgets(root):

    ## === Conversation Area Widgets === ###

    # Frame for Conversation Text
    frame_conv = ttk.Frame(root)

    # Conversation Text
    global txt_conv
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

    first_bot_msg = """Hi, I'm Files Chatter Bot! 
- Add new files by clicking on Files -> Add Files menu.
- Start a new chat by clicking on Chats -> New Chat"""

    txt_conv.tag_configure("bold", font=("Helvetica", 12, "bold"))
    txt_conv.insert(tk.INSERT, "Bot:\n", "bold")
    txt_conv.insert(tk.INSERT, first_bot_msg)

    global vsb_conv
    vsb_conv = ttk.Scrollbar(frame_conv, orient='vertical', command=txt_conv.yview)
    vsb_conv.grid(row=0, column=1, sticky="ns")
    vsb_conv.grid_remove()  # Hide the scrollbar initially

    txt_conv['yscrollcommand'] = vsb_conv.set
    #txt_conv.bind("<KeyRelease>", partial(vsb_visibility, vsb_conv, txt_conv))

    txt_conv.config(
        state=tk.DISABLED,
        selectbackground="lightblue", 
        inactiveselectbackground="lightblue",
    )

    # Conversation frame grid configuration
    frame_conv.grid_columnconfigure(0, weight=1)
    frame_conv.grid_columnconfigure(1, weight=0)
    frame_conv.grid_rowconfigure(0, weight=1)

    frame_conv.grid(row=0, column=0, sticky="nsew")

    # Chatbox using Advanced Text custom widget
    chatbox_adtxt = AdvancedText(
        root,
        placeholder="Type here... Hit <Enter> to send, and <Shift-Enter> for new line.", 
        enter_callback=send_msg,
        callback_args=(txt_conv,) # the extra coma is for creating a single-item tuple
    )
    chatbox_adtxt.grid(row=1, column=0, padx=6, pady=8, sticky="nsew")


    ### === Root Grid Configuration === ###

    # Make the Conv area take up max space, and chatbox take up as much as it needs
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)
