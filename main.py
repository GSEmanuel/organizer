from tkinter import *
from tkinter import ttk

from recursos import *
from recursos.menu_bar import * # importa MenuBar
# from recursos.frame_ventana import * # importa FramePrincipal
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
		self.bind('<Control-q>', lambda x:self.destroy())
		self.bind('<Control-Q>', lambda x:self.destroy())

		# inicializamos el loop principal de la ventana

		# self.var_ruta_carpeta = StringVar()
		# ruta_carpeta = ttk.Entry(self, state= 'readonly',)

		# ruta_carpeta.grid(row = 0, column = 0)

		boton_principal = ttk.Button(self, text='Principal')
		boton_principal.grid(row = 0, column = 0, sticky = 'ew')

		boton_comparar = ttk.Button(self, text = 'Comparar/fusionar')
		boton_comparar.grid(row = 1, column = 0, sticky = 'ew')

		boton_respaldos = ttk.Button(self, text = 'Respaldos')
		boton_respaldos.grid(row = 2, column = 0, sticky = 'ew')

		# self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)
		self.columnconfigure(2, weight = 1)

		self.rowconfigure(0, weight = 1)
		self.rowconfigure(1, weight = 1)
		self.rowconfigure(2, weight = 1)

		self.mainloop()


	def mostrar_ayuda(self):
		Ayuda()
	
	def mostrar_frame(self, frame):
		frame.tkraise()
		

	


if __name__ == '__main__':
	MainApp()