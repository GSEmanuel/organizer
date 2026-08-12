from tkinter import *
from tkinter import ttk

from recursos import *
from recursos.menu_bar import * # importa MenuBar

class MainApp(Tk):
	def __init__(self):
		super(MainApp,self).__init__()
		# --------------------- inicializacion de la ventana ---------------------
		# self.ventana = Tk()
		self.geometry('640x480')
		self.title('Organizer')
		self.minsize(320, 240)

		# inicializamos la ventana
		self['menu'] = MenuBar(self)

		# agregamos los accesos rápidos
		self.bind('<F1>', lambda x:self.mostrar_ayuda())

		# inicializamos el loop principal de la ventana
		self.mainloop()

	def mostrar_ayuda(self):
		Ayuda()
		

	


if __name__ == '__main__':
	MainApp()