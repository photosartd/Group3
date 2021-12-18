from tkinter import *

root = Tk()


def on_button():
    print('Im clicked!')


root['bg'] = '#fafafa'
root.title('Example app')
root.geometry('300x250')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=.15, rely=.15, relwidth=.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=.15, rely=.55, relwidth=.7, relheight=0.1)

formula_field = Entry(frame_top, bg='white', font=30)
formula_field.pack()

btn = Button(frame_top, text='Calculate', command=on_button)
btn.pack()

info = Label(frame_bottom, text='Calculator', bg='#ffb700', font=40)
info.pack()

root.mainloop()