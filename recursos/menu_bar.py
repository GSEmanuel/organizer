# from tkinter import *
from tkinter import Menu

__all__ = ['MenuBar']

class MenuBar(Menu):
	def __init__(self, parent):
		super(MenuBar, self).__init__(parent.ventana)
		parent.ventana.option_add('*tearOff', False)

		# ----------------------------------------------------
		# -------------------- menu archivo ------------------
		# ----------------------------------------------------
		sub_menu_principal = Menu(self)
		sub_menu_principal.add_command(label = 'Mostrar punto de venta',
									   underline = 17,
									   # command = lambda: parent.mostrar_frame(parent.frame_punto_venta),
									   # accelerator = 'Shift + V'
									   )

		sub_menu_principal.add_command(label = 'Mostrar inventario',
									  # command = lambda: parent.mostrar_frame(parent.frame_inventario)
									  )
		sub_menu_principal.add_command(label = 'Mostrar resumen')

		self.add_cascade(menu = sub_menu_principal, label = 'Creampie')
		# ----------------------------------------------------


		# ----------------------------------------------------
		# -------------------- menu ayuda --------------------
		# ----------------------------------------------------
		sub_menu_ayuda = Menu(self)
		sub_menu_ayuda.add_command(label = 'Acerca de',
								   command = lambda: parent.mostrar_ayuda(),
								   accelerator = 'F1')

		self.add_cascade(menu = sub_menu_ayuda, label = 'Ayuda')
		# ----------------------------------------------------



