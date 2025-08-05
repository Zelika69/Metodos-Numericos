#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menú principal de métodos numéricos
"""

import tkinter as tk
from tkinter import ttk

class MethodsMenu:
    """Menú principal para seleccionar métodos numéricos"""
    
    def __init__(self, parent, on_method_select_callback):
        self.parent = parent
        self.on_method_select_callback = on_method_select_callback
        
        # Frame principal
        self.frame = tk.Frame(parent, bg='#2c3e50')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets del menú principal"""
        
        # Título
        title_label = tk.Label(self.frame,
                              text="MÉTODOS NUMÉRICOS",
                              font=('Arial', 24, 'bold'),
                              fg='white',
                              bg='#2c3e50',
                              pady=20)
        title_label.pack()
        
        # Subtítulo
        subtitle_label = tk.Label(self.frame,
                                 text="Seleccione el método que desea utilizar",
                                 font=('Arial', 14),
                                 fg='#ecf0f1',
                                 bg='#2c3e50',
                                 pady=10)
        subtitle_label.pack()
        
        # Frame para los botones de métodos
        methods_frame = tk.Frame(self.frame, bg='#2c3e50')
        methods_frame.pack(expand=True, pady=30)
        
        # Configurar grid para centrar los botones
        methods_frame.grid_rowconfigure(0, weight=1)
        methods_frame.grid_rowconfigure(1, weight=1)
        methods_frame.grid_columnconfigure(0, weight=1)
        methods_frame.grid_columnconfigure(1, weight=1)
        
        # Definir métodos con sus descripciones
        methods = [
            {
                'name': 'Método de Bisección',
                'description': 'Encuentra raíces de ecuaciones\nen intervalos dados',
                'key': 'bisection',
                'color': '#3498db'
            },
            {
                'name': 'Newton-Raphson',
                'description': 'Método iterativo para\nencontrar raíces',
                'key': 'newton_raphson',
                'color': '#e74c3c'
            },
            {
                'name': 'Método de Euler',
                'description': 'Resolución numérica de\necuaciones diferenciales',
                'key': 'euler',
                'color': '#f39c12'
            },
            {
                'name': 'Runge-Kutta (RK4)',
                'description': 'Método de cuarto orden para\necuaciones diferenciales',
                'key': 'runge_kutta',
                'color': '#27ae60'
            }
        ]
        
        # Crear botones para cada método
        for i, method in enumerate(methods):
            row = i // 2
            col = i % 2
            
            method_frame = tk.Frame(methods_frame, 
                                   bg=method['color'], 
                                   relief='raised', 
                                   bd=3)
            method_frame.grid(row=row, column=col, 
                             padx=20, pady=15, 
                             sticky='nsew', 
                             ipadx=20, ipady=20)
            
            # Título del método
            method_title = tk.Label(method_frame,
                                   text=method['name'],
                                   font=('Arial', 16, 'bold'),
                                   fg='white',
                                   bg=method['color'])
            method_title.pack(pady=(10, 5))
            
            # Descripción del método
            method_desc = tk.Label(method_frame,
                                  text=method['description'],
                                  font=('Arial', 10),
                                  fg='white',
                                  bg=method['color'],
                                  justify=tk.CENTER)
            method_desc.pack(pady=(0, 10))
            
            # Botón para seleccionar el método
            select_button = tk.Button(method_frame,
                                     text="SELECCIONAR",
                                     font=('Arial', 12, 'bold'),
                                     fg=method['color'],
                                     bg='white',
                                     activebackground='#ecf0f1',
                                     relief='raised',
                                     bd=2,
                                     command=lambda key=method['key']: self.select_method(key))
            select_button.pack(pady=(0, 10))
        
        # Botón para volver a la pantalla de bienvenida
        back_frame = tk.Frame(self.frame, bg='#2c3e50')
        back_frame.pack(side=tk.BOTTOM, pady=20)
        
        back_button = tk.Button(back_frame,
                               text="← VOLVER AL INICIO",
                               font=('Arial', 12),
                               fg='white',
                               bg='#7f8c8d',
                               activebackground='#95a5a6',
                               activeforeground='white',
                               relief='raised',
                               bd=2,
                               command=self.go_back)
        back_button.pack()
    
    def select_method(self, method_key):
        """Selecciona un método y llama al callback"""
        self.on_method_select_callback(method_key)
    
    def go_back(self):
        """Vuelve a la pantalla de bienvenida"""
        # Aquí podrías implementar la navegación hacia atrás
        # Por ahora, simplemente cerramos la aplicación o volvemos al inicio
        pass
    
    def destroy(self):
        """Destruye el frame del menú"""
        self.frame.destroy()