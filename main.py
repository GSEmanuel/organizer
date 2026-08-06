from tkinter import *
from tkinter import ttk

from recursos import *
from recursos.menu_bar import * # importa MenuBar

class MainApp(object):
	def __init__(self):

		# --------------------- inicializacion de la ventana ---------------------
		self.ventana = Tk()
		self.ventana.geometry('640x480')
		self.ventana.title('Organizer')
		self.ventana.minsize(320, 240)

		# inicializamos la ventana
		self.ventana['menu'] = MenuBar(self)

		# agregamos los accesos rápidos
		self.ventana.bind('<F1>', lambda x:self.mostrar_ayuda())

		# inicializamos el loop principal de la ventana
		self.ventana.mainloop()

	def mostrar_ayuda(self):
		Ayuda()
		

	


if __name__ == '__main__':
	MainApp()