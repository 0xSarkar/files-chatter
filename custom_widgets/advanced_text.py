import tkinter as tk
from tkinter import ttk

class AdvancedText(tk.Frame):
    def __init__(self, parent, default="", height = 3, enter_callback=None, callback_args=(), enter_clear=False):
        tk.Frame.__init__(self, parent)

        self.shift_pressed = False
        self.enter_callback = enter_callback
        self.callback_args = callback_args
        self.enter_clear = enter_clear

        self.txt = tk.Text(
            self,
            wrap=tk.WORD,
            height=height,
            spacing1=8,
            spacing2=4,
            padx=4
        )
        self.txt.grid(row=0, column=0, sticky="nsew")

        self.vsb = ttk.Scrollbar(self, orient='vertical', command=self.txt.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.vsb.grid_remove()

        self.txt.config(yscrollcommand=self.vsb.set)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.txt.insert("1.0", default)

        self.txt.bind("<Control-a>", self.chatbox_select_all)
        self.txt.bind("<Control-A>", self.chatbox_select_all)
        self.txt.bind("<Tab>", self.handle_tab)

        self.txt.bind("<KeyRelease>", self.handle_keyrelease)
        self.txt.bind("<KeyPress>", self.handle_keypress)
        self.txt.bind("<Configure>", self.update_vsb_visibility) # we must update the scrollbar visibility when window size changes and hence Text's size changes. Also this line helps hiding the scrollbar with non-overflowing default text, not sure why.

        self.txt.bind("<Return>", self.handle_enter)
        
    def handle_keypress(self, event):
        if event.keysym == "Shift_R" or event.keysym == "Shift_L":
            self.shift_pressed = True

    def handle_keyrelease(self, event):
        if event.keysym == "Shift_R" or event.keysym == "Shift_L":
            self.shift_pressed = False
        self.update_vsb_visibility()
    
    def handle_tab(self, event):
        self.tk_focusNext().focus()
        return "break"  # Prevent default tab behavior

    def handle_enter(self, event):
        if self.enter_callback is not None:
            # if a callback is provided, then check if its shift+enter or only enter
            if(self.shift_pressed):
                # insert new line on shift+enter
                self.insert(tk.INSERT, "\n")
            else:
                # call the callback if just enter
                self.enter_callback(self, *self.callback_args) if self.callback_args else self.enter_callback(self)
                    
        if self.enter_clear and not self.shift_pressed:
            self.txt.delete("1.0", tk.END)  # Clear all text

        if self.enter_callback is None and not self.enter_clear:
            # if there's no call back nor instruction to clear the Text, return normal behavior
            return
        
        return "break" # prevent default behavior on Enter

    def get_text_widget(self):
        return self.txt
    
    def chatbox_select_all(self, event=None):
        self.txt.tag_add(tk.SEL, "1.0", tk.END)
        return "break"

    def get(self):
        return self.txt.get("1.0", "end-1c")
    
    def insert(self, index, chars, *args):
        self.txt.insert(index, chars, *args)
        self.after(5, self.update_vsb_visibility) # a 5 ms delay is needed so that the Text's view is updated after the insert

    def update_vsb_visibility(self, event=None):
        yview = self.txt.yview()
        y_scrollable = yview != (0.0, 1.0)
        if y_scrollable:
            self.vsb.grid()  # Show the vertical scrollbar
        else:
            self.vsb.grid_remove()  # Hide the vertical scrollbar