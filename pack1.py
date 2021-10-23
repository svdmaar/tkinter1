import tkinter as tk
window = tk.Tk()

frame1 = tk.Frame(height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(height=25, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()

