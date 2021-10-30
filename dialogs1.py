import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askfloat
from tkinter.messagebox import showerror, askyesno, askyesnocancel

def OnButtonClick():
    #filepath = askopenfilename()
    #filepath = asksaveasfilename()
    #filepath = askfloat("title", "prompt")
    #print(filepath)
    #showerror("Error!!!!", "Something went wrong!!!!!")
    response = askyesnocancel("Question", "Are you having fun?")
    print(response)


window = tk.Tk()

button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow", command=OnButtonClick)
button.pack()

window.mainloop()
