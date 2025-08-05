#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ventana principal de la aplicación
Contiene la pantalla de bienvenida y navegación entre métodos
"""

import tkinter as tk
from tkinter import ttk
from gui.welcome_screen import WelcomeScreen
from gui.methods_menu import MethodsMenu
from gui.bisection_window import BisectionWindow
from gui.newton_raphson_window import NewtonRaphsonWindow
from gui.euler_window import EulerWindow
from gui.runge_kutta_window import RungeKuttaWindow

class MainWindow:
    """Clase principal que maneja la ventana de la aplicación"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador de Métodos Numéricos")
        self.root.geometry("900x700")
        self.root.configure(bg='#2c3e50')
        
        # Configurar estilo
        self.setup_styles()
        
        # Frame principal que contendrá todas las pantallas
        self.main_frame = tk.Frame(root, bg='#2c3e50')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Inicializar con pantalla de bienvenida
        self.current_screen = None
        self.show_welcome_screen()
    
    def setup_styles(self):
        """Configura los estilos de la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo para botones principales
        style.configure('Main.TButton',
                       font=('Arial', 12, 'bold'),
                       padding=10)
        
        # Estilo para títulos
        style.configure('Title.TLabel',
                       font=('Arial', 16, 'bold'),
                       background='#2c3e50',
                       foreground='white')
    
    def clear_screen(self):
        """Limpia la pantalla actual"""
        if self.current_screen:
            self.current_screen.destroy()
    
    def show_welcome_screen(self):
        """Muestra la pantalla de bienvenida"""
        self.clear_screen()
        self.current_screen = WelcomeScreen(self.main_frame, self.show_methods_menu)
    
    def show_methods_menu(self):
        """Muestra el menú de métodos numéricos"""
        self.clear_screen()
        self.current_screen = MethodsMenu(self.main_frame, self.show_method_window)
    
    def show_method_window(self, method_name):
        """Muestra la ventana del método seleccionado"""
        self.clear_screen()
        
        if method_name == "bisection":
            self.current_screen = BisectionWindow(self.main_frame, self.show_methods_menu)
        elif method_name == "newton_raphson":
            self.current_screen = NewtonRaphsonWindow(self.main_frame, self.show_methods_menu)
        elif method_name == "euler":
            self.current_screen = EulerWindow(self.main_frame, self.show_methods_menu)
        elif method_name == "runge_kutta":
            self.current_screen = RungeKuttaWindow(self.main_frame, self.show_methods_menu)