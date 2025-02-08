import tkinter as tk
from tkinter import ttk
from tkinter import font

# from ttkbootstrap import Style
from tkinter import ttk
from datetime import date

from . import constants as cn
from . import functions as fn


class Sobrante(ttk.Frame):
    def __init__(self, parent, controller, path):
        super().__init__(parent)
        self.controller = controller
        self.rootPath = path
        self.database = fn.getDatabase(self.rootPath)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="column")
        self.notebook = ttk.Notebook(self)

        self.notebook.pack(fill="both", expand=True)

        #######################################################################
        # Inventario de sobrantes

        self.invFrame = ttk.Frame(self.notebook)
        self.invFrame.pack(
            fill="both",
            expand=True,
        )
        # self.invFrame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        # self.invFrame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.listadoSobrante = ttk.Treeview(
            self.invFrame, columns=cn.invHeadigns, show="headings"
        )
        for i in cn.invHeadigns:
            self.listadoSobrante.heading(i, text=i)
        for i in range(len(cn.invHeadigns)):
            self.listadoSobrante.column(cn.invHeadigns[i], width=100, anchor="center")
        self.listadoSobrante.pack()

        self.listadoSobrante.tag_configure("oddrow", background="#333333")
        self.listadoSobrante.tag_configure("evenrow", background="#222222")

        #######################################################################
        # Search Tab

        self.searchFrame = ttk.Frame(self.notebook)
        self.searchFrame.pack(fill="both", expand=True)

        self.searchFrame.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="column"
        )

        #######################################################################
        # Data Tab

        self.addDataFrame = ttk.Frame(self.notebook)
        self.addDataFrame.pack(fill="both", expand=True)

        self.addDataFrame.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="column"
        )

        #######################################################################
        # Add the tabs
        self.notebook.add(self.invFrame, text="Sobrante")
        self.notebook.add(self.searchFrame, text="Buscar")
        self.notebook.add(self.addDataFrame, text="Agregar")
