import tkinter as tk
window = tk.Tk()

for i in range(3):
    for j in range(4):
        frame = tk.Frame(relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text="Row " + str(i) + "\nColumn " + str(j))
        label.pack(padx=10, pady=10)

window.mainloop()
