from tkinter import *
from tkinter import ttk

def mensaje(*args):
    try:
        mensaje.set(f'lugar: {btn_id}')
    except ValueError:
        pass

root = Tk()
root.geometry("300x300")
root.title("3x3")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

mensaje = StringVar()
ttk.Label(mainframe, textvariable=mensaje).grid(column=1, row=0, sticky=(W, E), padx=5, pady=5)

for i in range(3):
    for j in range(3):
        btn_id = i*3 + j+1
        ttk.Button(mainframe, text=f'boton {btn_id}', command=mensaje).grid(column=1, row=1, sticky=W)

root.bind("<Return>", lambda event: mensaje("Return"))

root.mainloop()