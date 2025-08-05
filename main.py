#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solucionador de Métodos Numéricos
Herramienta educativa para resolver problemas de métodos numéricos
Desarrollado con Tkinter
"""

import tkinter as tk
from tkinter import ttk
from gui.main_window import MainWindow

def main():
    """Función principal que inicia la aplicación"""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()