import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

root = Tk()


def on_button():
    print('Im clicked!')


root['bg'] = '#fafafa'
root.title('Example app')
root.geometry('900x900')

root.resizable(width=True, height=True)

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=.15, rely=.15, relwidth=.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=.15, rely=.55, relwidth=.7, relheight=0.1)

formula_field = Entry(frame_top, bg='white', font=30)
formula_field.pack()

btn = Button(frame_top, text='Calculate', command=on_button)
btn.pack()

info = Label(frame_bottom, text='Calculator', bg='#♦', font=40)
info.pack()



root.mainloop()