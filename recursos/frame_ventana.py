from tkinter import Frame
from tkinter import Label

class FramePrincipal(Frame):
    def __init__(self, parent):
        super(FramePrincipal, self).__init__(parent)

        Label_ventana = Label(self, text = 'Frame Principal')
        Label_ventana.pack()


if __name__ == '__main__':
    from tkinter import *
    app = Tk()
    frame_prueba = FramePrincipal(app)
    frame_prueba.pack()

    app.mainloop()