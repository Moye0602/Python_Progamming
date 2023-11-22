#myfunc(nums)
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
#window
window=tkk.window(themename='journal')#journal
window.title('Tradebot V9_0_5')
window.geometry('500x300')#X by Y

def my_func():
    #print('words')
    user_input=entry_int.get()
    #print(entry_int.get())
    #print(entry.get())
    output_string.set(user_input)

#title
title_label=ttk.Label(master=window,text='main window',font='Calibri 10 underline')
title_label.pack()

#input field
input_frame=ttk.Frame(master=window)
entry_int=tk.IntVar()#stores and updates values
entry=ttk.Entry(master=input_frame,textvariable=entry_int)
button=ttk.Button(master=input_frame,text='do task',command=my_func)

entry.pack(side='left',padx=5)
button.pack(side='left')
input_frame.pack()

#output field
output_string=tk.StringVar()
output_lable=ttk.Label(master=window,
                        text='Output',
                        font='Calibri 10 underline',
                        textvariable=output_string)
output_lable.pack()
#run
window.mainloop()

'''trend
breakout
reversion to the mean 
break down
shorting System
if the trend fails, it must fail fast as hell and get back to business
#
stacking tradings
    30 second bar 
    5minute
    60 minute
    240 minuute
    480 minute
    1 day
    each interval is a seperate trade and working indipendetlly of the others
'''