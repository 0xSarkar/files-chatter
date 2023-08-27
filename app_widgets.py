import tkinter as tk
from tkinter import ttk
from functools import partial

from custom_widgets.advanced_text import AdvancedText

txt_chatbox = None
txt_conv = None
vsb_conv = None
vsb_chatbox = None
chatbox_shift_pressed = 0

### === Widget Event Handlers === ###

def send_msg(caller=None, event=None, txt_conv=None, txt_chatbox=None):
    user_msg = caller.txt.get("1.0", tk.END)
    txt_conv.config(state=tk.NORMAL)
    txt_conv.insert(tk.END, user_msg)
    txt_conv.config(state=tk.DISABLED)

    return "break"

def chatbox_select_all(event):
    txt_chatbox.tag_add(tk.SEL, "1.0", tk.END)
    return "break"

def chatbox_key_release(vsb_chatbox, txt_chatbox, event=None):
    vsb_visibility(vsb_chatbox, txt_chatbox)

def set_chatbox_shift_pressed(value):
    global chatbox_shift_pressed
    chatbox_shift_pressed = value

def chatbox_handle_return(event):
    global chatbox_shift_pressed
    if(chatbox_shift_pressed):
        event.widget.insert(tk.INSERT, "\n")
    else:
        send_msg()

    return "break"

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

    frame_conv.grid(row=0, column=0, sticky="nsew")

    # Conversation frame grid configuration
    frame_conv.grid_columnconfigure(0, weight=1)
    frame_conv.grid_columnconfigure(1, weight=0)
    frame_conv.grid_rowconfigure(0, weight=1)


    ### === Chatbox Widgets === ###

    frame_chat = ttk.Frame(root)

    global txt_chatbox
    txt_chatbox= tk.Text(
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
    global vsb_chatbox
    vsb_chatbox = ttk.Scrollbar(frame_chat, orient='vertical', command=txt_chatbox.yview)
    vsb_chatbox.grid(row=0, column=1, padx=(0, 2), pady=8, sticky="ns")
    vsb_chatbox.grid_remove()  # Hide the scrollbar initially

    txt_chatbox['yscrollcommand'] = vsb_chatbox.set
    txt_chatbox.bind("<KeyRelease>", partial(chatbox_key_release, vsb_chatbox, txt_chatbox))

    txt_chatbox.bind("<KeyPress-Shift_L>", lambda event: set_chatbox_shift_pressed(1))
    txt_chatbox.bind("<KeyPress-Shift_R>", lambda event: set_chatbox_shift_pressed(1))
    txt_chatbox.bind("<KeyRelease-Shift_L>", lambda event: set_chatbox_shift_pressed(0))
    txt_chatbox.bind("<KeyRelease-Shift_R>", lambda event: set_chatbox_shift_pressed(0))

    txt_chatbox.bind("<Tab>", handle_tab)
    txt_chatbox.bind("<Return>", chatbox_handle_return)

    # Send Button
    btn_send = ttk.Button(frame_chat, text="Send", command=send_msg)
    btn_send.grid(row=0, column=2, padx=(2, 8), pady=8, sticky="nsew")

    btn_send.bind("<Return>", send_msg)

    frame_chat.grid(row=1, column=0, sticky="nsew")


    # Testing Advanced Text custom widget
    advanced_text = AdvancedText(
        frame_chat,
        default="Hello, this is some text.\n", 
        enter_callback=send_msg,
        callback_args=(None, txt_conv), 
        enter_clear=True
    )
    advanced_text.grid(row=1, column=0, columnspan=3, padx=4, pady=8)

    advanced_text.insert(tk.END, "Falana is not Dhikana.\n")

    advanced_text_TW = advanced_text.get_text_widget()
    advanced_text_TW.tag_configure("bold", font=("Helvetica", 12, "bold"))
    advanced_text.insert(tk.INSERT, bot_name, "bold")

    # Chat frame grid configuration
    frame_chat.grid_columnconfigure(0, weight=1)
    frame_chat.grid_columnconfigure(1, weight=0)
    frame_chat.grid_columnconfigure(2, weight=0)
    frame_chat.grid_rowconfigure(0, weight=0)
    frame_chat.grid_rowconfigure(1, weight=0)


    ### === Root Grid Configuration === ###

    # Set column weights to make them resize proportionally
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)
