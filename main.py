from tkinter import *
from tkinter import ttk
from recursos.menu_bar import * # importa MenuBar

class MainApp(object):
	def __init__(self):

		# --------------------- inicializacion de la ventana ---------------------
		self.ventana = Tk()
		self.ventana.geometry('640x480')
		self.ventana.title('Organizer')
		self.ventana.minsize(320, 240)
		self.ventana['menu'] = MenuBar(self.ventana)

		
		
		
		self.ventana.mainloop()

		

	


if __name__ == '__main__':
	MainApp()