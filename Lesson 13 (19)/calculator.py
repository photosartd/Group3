from tkinter import *


def on_button_1_pressed():
    #взять текст и добавить 1
    text = main_label.cget('text')
    text = text + '1'
    main_label['text'] = text

def on_button_2_pressed():
    #взять текст и добавить 1
    text = main_label.cget('text')
    text = text + '2'
    main_label['text'] = text

def on_button_mult_pressed():
    # взять текст и добавить 1
    text = main_label.cget('text')
    text = text + '*'
    main_label['text'] = text

def on_button_eq_pressed():
    # взять текст и добавить 1
    text = main_label.cget('text')
    new_text = eval(text)
    main_label['text'] = str(new_text)

root = Tk()

root['bg'] = '#5d3954'
root.title('Calculator')
root.geometry('400x600')
root.resizable(width=True, height=True)

frame_top = Frame(root, bg='#fff44f', bd=5)
frame_top.place(relwidth=1., relheight=0.3, rely=0.)

frame_bottom = Frame(root, bg='#d0d0d0', bd=5)
frame_bottom.place(relwidth=0.9, relheight=0.6, rely=0.35,
                   relx=0.05)

main_label = Label(frame_top, text='', bg='#FFFFFF', font=24)
main_label.place(relwidth=0.9, relheight=0.6, rely=0.2,
                 relx=0.05)

button_1 = Button(frame_bottom, text='1', bg='#dad871', font=24,
                  command=on_button_1_pressed)
button_1.place(relwidth=0.15, relheight=0.15, rely=0.05,
               relx=0.05)
button_2 = Button(frame_bottom, text='2', bg='#dad871', font=24,
                  command=on_button_2_pressed)
button_2.place(relwidth=0.15, relheight=0.15, rely=0.05,
               relx=0.25)
button_3 = Button(frame_bottom, text='*', bg='#dad871', font=24,
                  command=on_button_mult_pressed)
button_3.place(relwidth=0.15, relheight=0.15, rely=0.05,
               relx=0.45)
button_4 = Button(frame_bottom, text='=', bg='#dad871', font=24,
                  command=on_button_eq_pressed)
button_4.place(relwidth=0.15, relheight=0.15, rely=0.05,
               relx=0.65)

root.mainloop()
