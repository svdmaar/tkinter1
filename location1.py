import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B", bg="black", fg="white")
label2.grid(row=1, column=0, sticky="swen")

window.mainloop()
