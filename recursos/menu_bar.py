# from tkinter import *
from tkinter import Menu

__all__ = ['MenuBar']

class MenuBar(Menu):
	def __init__(self, parent):
		super(MenuBar, self).__init__(parent)
		parent.option_add('*tearOff', False)
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

		self.add_cascade(menu = sub_menu_principal, label = 'Principal')

