from tkinter import Toplevel
from tkinter.ttk import Label
from tkinter.ttk import Button
from tkinter import RIGHT

__all__ = ['Ayuda',]

class Ayuda(Toplevel):
	def __init__(self):
		super(Ayuda, self).__init__()
		self.text = '\n'.join(['Es una app para organizar sencillo y util para su uso personal.',
							   'Su uso es libre y no se cobrará por su uso.',
							   'creado por: Gonzalez Santiago',
							   'contacto: ',
							   '\n',
							   '	e-mail: gsemanuel@yahoo.com',
							   '\n',
							   'Se agradece su referencia a mi trabajo.',
							   'si tienes una sugerencia, aviso, refactoring o detectaste',
							   'un bug estare agradecido el contacto para darme aviso.',
							   'Ojalá algun dia nos crucemos y trabajemos juntos en ',
							   'un proyecto, estare encantado al leer tus ideas. :D',])

 
		self.title('Ayuda')
		self.resizable(False,False)
		self.contenido = Label(self, text = self.text)
		self.contenido.pack(padx = 10, pady = 10)
		self.btn_ok = Button(self, text = 'Ok', command = self.destroy)
		self.btn_ok.pack(side = RIGHT, padx = 10, pady = 10)
		self.mainloop()

# ayuda = Ayuda()