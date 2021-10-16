import tkinter as tk

def PrintHello():
    print(entry.get())

window = tk.Tk()

greeting = tk.Label(
    text="Hello, Tkinter!",
    foreground="white",
    background="black",
    width=10, height=10)
greeting.pack()

button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow", command=PrintHello)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

window.mainloop()


