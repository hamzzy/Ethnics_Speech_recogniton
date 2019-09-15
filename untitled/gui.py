import tkinter
from tkinter import filedialog, Button,Label
from scipy.io import wavfile
from tensorflow.keras.models import load_model
from  read_audio import wav2mfcc
import numpy as np


label={
    0:'hausa',
    1:'igbo',
    2:'yoruba'
}

top = tkinter.Tk()
# Code to add widgets will go here...
def ChooseAudio():
    table=[]
    tk = filedialog.askopenfilename()
    table.append(wav2mfcc(tk))
    t=load_model('the not/untitled/model.hdf5')
    tab=np.array(table)
    tw=t.predict_classes(tab)
    if 0 in tw :
       pre.set('predicted is hausa')
       percent.set(('Truth is %s'%(tk.split('/')[-2])))
    elif 1 in tw:
        pre.set('Predicted is  igbo  ')
        percent.set(('Truth is %s'%(tk.split('/')[-2])))
    else:
        pre.set('predicted is yoruba ')
        percent.set(('Truth is %s'%(tk.split('/')[-2])))
    
pre=tkinter.StringVar() 
percent=tkinter.StringVar()
lbt=Label(top,text='Ethnic Recognition',font=("TkDefaultFont", 30), wraplength=400)
lbt.grid(row=2,column=3)
btn = Button(top,text="choose file",command=ChooseAudio)
btn.grid(row=3,column=5)


lb=Label(top, textvariable=pre,font=("TkDefaultFont", 30), wraplength=400)
lb.grid(row=4,column=3)
lb1=Label(top, textvariable=percent,font=("TkDefaultFont", 30), wraplength=400)
lb1.grid(row=5,column=3)
top.geometry("800x600")
top.mainloop()
