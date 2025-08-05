#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pantalla de bienvenida con estilo de calculadora científica
"""

import tkinter as tk
from tkinter import ttk

class WelcomeScreen:
    """Pantalla de bienvenida tipo calculadora científica"""
    
    def __init__(self, parent, on_start_callback):
        self.parent = parent
        self.on_start_callback = on_start_callback
        
        # Frame principal con estilo de calculadora
        self.frame = tk.Frame(parent, bg='#1a1a1a', relief='raised', bd=3)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la pantalla de bienvenida"""
        
        # Título principal con estilo retro
        title_frame = tk.Frame(self.frame, bg='#000000', relief='sunken', bd=2)
        title_frame.pack(fill=tk.X, padx=10, pady=10)
        
        title_label = tk.Label(title_frame, 
                              text="SOLUCIONADOR DE\nMÉTODOS NUMÉRICOS",
                              font=('Courier New', 20, 'bold'),
                              fg='#00ff00',
                              bg='#000000',
                              pady=15)
        title_label.pack()
        
        # Subtítulo
        subtitle_label = tk.Label(self.frame,
                                 text="Herramienta Educativa para Ingeniería",
                                 font=('Arial', 14, 'italic'),
                                 fg='#ecf0f1',
                                 bg='#1a1a1a',
                                 pady=10)
        subtitle_label.pack()
        
        # Pantalla LCD simulada
        lcd_frame = tk.Frame(self.frame, bg='#2d5016', relief='sunken', bd=3)
        lcd_frame.pack(fill=tk.X, padx=30, pady=20)
        
        welcome_text = tk.Label(lcd_frame,
                               text="Bienvenido al solucionador\nde métodos numéricos\n\nSeleccione INICIO para comenzar",
                               font=('Courier New', 12),
                               fg='#000000',
                               bg='#9acd32',
                               pady=20,
                               justify=tk.CENTER)
        welcome_text.pack(fill=tk.X)
        
        # Botones con estilo de calculadora
        buttons_frame = tk.Frame(self.frame, bg='#1a1a1a')
        buttons_frame.pack(pady=30)
        
        # Botón INICIO
        start_button = tk.Button(buttons_frame,
                                text="INICIO",
                                font=('Arial', 16, 'bold'),
                                fg='white',
                                bg='#27ae60',
                                activebackground='#2ecc71',
                                activeforeground='white',
                                relief='raised',
                                bd=3,
                                width=12,
                                height=2,
                                command=self.start_application)
        start_button.pack(side=tk.LEFT, padx=10)
        
        # Botón SALIR
        exit_button = tk.Button(buttons_frame,
                               text="SALIR",
                               font=('Arial', 16, 'bold'),
                               fg='white',
                               bg='#e74c3c',
                               activebackground='#c0392b',
                               activeforeground='white',
                               relief='raised',
                               bd=3,
                               width=12,
                               height=2,
                               command=self.exit_application)
        exit_button.pack(side=tk.LEFT, padx=10)
        
        # Información adicional
        info_frame = tk.Frame(self.frame, bg='#1a1a1a')
        info_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
        info_label = tk.Label(info_frame,
                             text="Métodos disponibles: Bisección • Newton-Raphson • Euler • Runge-Kutta",
                             font=('Arial', 10),
                             fg='#bdc3c7',
                             bg='#1a1a1a')
        info_label.pack()
    
    def start_application(self):
        """Inicia la aplicación llamando al callback"""
        self.on_start_callback()
    
    def exit_application(self):
        """Cierra la aplicación"""
        self.parent.master.quit()
    
    def destroy(self):
        """Destruye el frame de la pantalla"""
        self.frame.destroy()