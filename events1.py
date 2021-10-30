import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    print(event.char)

#events_list = []

#while True:
#    if event_list:
#        event = events_list[0]

#        if event.type == "keypress":
#            handle_keypress(event)

window.bind("<Key>", handle_keypress)

window.mainloop()

