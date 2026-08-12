# from tkinter import *
from tkinter import Menu

__all__ = ['MenuBar']

class MenuBar(Menu):
	def __init__(self, parent):
		super(MenuBar, self).__init__(parent)
		parent.option_add('*tearOff', False)

		# ----------------------------------------------------
		# -------------------- menu archivo ------------------
		# ----------------------------------------------------
		sub_menu_principal = Menu(self)
		sub_menu_principal.add_command(label = 'Abrir carpeta',
									   underline = 0,
									   # command = lambda: parent.mostrar_frame(parent.frame_punto_venta),
									   accelerator = 'Ctrl + A',
									   )

		sub_menu_principal.add_command(label = 'Cambiar carpeta',
									  # command = lambda: parent.mostrar_frame(parent.frame_inventario)
									  )
		sub_menu_principal.add_command(label = 'Crear respaldos')

		sub_menu_principal.add_command(label = 'Salir',
									   command = parent.destroy,
									   accelerator = 'Ctrl + Q')
		# sub_menu_principal.add_command(Label = '')

		self.add_cascade(menu = sub_menu_principal, label = 'Archivo') # <-- Primera opcion Ventana

		# ----------------------------------------------------
		# ------------------ Menu ajustes --------------------
		# ----------------------------------------------------
		sub_menu_ajustes = Menu(self)
		sub_menu_ajustes.add_command(label = 'Preferencias')
		sub_menu_ajustes.add_command(label = 'Parámetros')
		
		self.add_cascade(menu = sub_menu_ajustes, label = 'Ajustes')

		# ----------------------------------------------------
		# -------------------- menu ayuda --------------------
		# ----------------------------------------------------
		sub_menu_ayuda = Menu(self)
		sub_menu_ayuda.add_command(label = 'Acerca de',
								   command = lambda: parent.mostrar_ayuda(),
								   accelerator = 'F1')

		self.add_cascade(menu = sub_menu_ayuda, label = 'Ayuda') # <-- Segunda Opcion ventana
		# ----------------------------------------------------

