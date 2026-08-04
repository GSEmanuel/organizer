from tkinter import *
from tkinter import ttk


class MainApp(object):
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('640x480')
        self.ventana.title('Organizer')

        self.ventana.mainloop()


if __name__ == '__main__':
    MainApp()