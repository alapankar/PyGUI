import tkinter as tk
from tkinter import filedialog, Text

root=tk.Tk()

apps=[]

canvas=tk.Canvas(root, height=600, width=600, bg="#263d42")
canvas.pack()

frame=tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def addapp():
    filename=filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    for app in apps:
        label=tk.Label(frame, text=app , bg="grey")
        label.pack()



openfile=tk.Button(root, text="Open File", fg="white", bg="#263d42", padx=10, pady=5, command=addapp)
openfile.pack()

runapps =tk.Button(root, text="Run Apps", fg="white", bg="#263d42", padx=10, pady=5)
runapps.pack()



root.mainloop()
