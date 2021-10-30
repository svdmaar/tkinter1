import tkinter as tk
window = tk.Tk()

rowCount = 3
columnCount = 4

for i in range(rowCount):
    window.rowconfigure(i, weight=1, minsize=70)

for j in range(columnCount):
    window.columnconfigure(j, weight=1, minsize=100)

for i in range(rowCount):
    for j in range(columnCount):
        frame = tk.Frame(relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text="Row " + str(i) + "\nColumn " + str(j))
        label.pack(padx=10, pady=10)

window.mainloop()
