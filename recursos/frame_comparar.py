from tkinter import Frame
from tkinter import Label

class FrameComparar(Frame):
    def __init__(self, parent):
        super(FrameComparar, self).__init__(parent)
        label_Prueba = Label(self, text = 'Frame comparar/fusionar')
        label_Prueba.pack()