import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog as fd
from pathlib import Path
import pandas as pd

# from ttkbootstrap import Style
from datetime import date

from . import constants as cn
from . import functions as fn


class Sobrante(ttk.Frame):
    def __init__(self, parent, controller, path):
        super().__init__(parent)
        self.controller = controller
        self.rootPath = path
        self.database = fn.getDatabase(self.rootPath)
        self.filename = ""

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
        self.invFrame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.invFrame.rowconfigure((1, 2, 3, 4, 5, 6, 7), weight=2)
        self.invFrame.rowconfigure(0, weight=1)

        self.searckSobrante = tk.Entry(self.invFrame)
        self.searckSobrante.grid(
            row=0, column=0, columnspan=8, sticky="NESW", padx=10, pady=20
        )

        self.listadoSobrante = ttk.Treeview(
            self.invFrame, columns=cn.invHeadigns, show="headings"
        )
        for i in cn.invHeadigns:
            self.listadoSobrante.heading(i, text=i)
        for i in range(len(cn.invHeadigns)):
            self.listadoSobrante.column(cn.invHeadigns[i], width=100, anchor="center")
        # self.listadoSobrante.pack()
        self.listadoSobrante.grid(
            row=1,
            column=0,
            columnspan=8,
            rowspan=7,
            sticky="NSEW",
            padx=(10, 10),
            pady=(0, 10),
        )

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

        self.searchButton = tk.Button(
            self.addDataFrame, text="Buscar", command=self.searchForFile
        )
        self.searchButton.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

        self.addCargaLabel = ttk.Label(
            self.addDataFrame, text="buscar", relief="solid", anchor="center"
        )
        self.addCargaLabel.grid(
            row=0, column=1, columnspan=5, sticky="NSEW", padx=10, pady=10
        )

        #######################################################################
        # Add the tabs
        self.notebook.add(self.invFrame, text="Sobrante")
        self.notebook.add(self.searchFrame, text="Buscar")
        self.notebook.add(self.addDataFrame, text="Agregar")

    def searchForFile(self):
        filetypes = (("excel file", "*.xlsx"), ("All files", "*.*"))
        filename = fd.askopenfilename(
            title="Buscar Archivo",
            initialdir=f"{Path.home()}/Documents",
            filetypes=filetypes,
        )
        self.filename = filename
        truncated = self.filename.split("/")[-1]
        self.addCargaLabel.config(text=truncated)
        carga = pd.read_excel(self.filename)
        print(carga)
