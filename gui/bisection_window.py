#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ventana para el método de Bisección
"""

import tkinter as tk
from tkinter import ttk, messagebox
from numerical_methods.methods import bisection_method
from numerical_methods.plotting import create_bisection_plot, is_matplotlib_available

class BisectionWindow:
    """Ventana para el método de Bisección"""
    
    def __init__(self, parent, back_callback):
        self.parent = parent
        self.back_callback = back_callback
        
        # Frame principal
        self.frame = tk.Frame(parent, bg='#2c3e50')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la ventana de bisección"""
        
        # Título
        title_label = tk.Label(self.frame,
                              text="MÉTODO DE BISECCIÓN",
                              font=('Arial', 20, 'bold'),
                              fg='white',
                              bg='#2c3e50',
                              pady=15)
        title_label.pack()
        
        # Frame principal con scroll
        main_container = tk.Frame(self.frame, bg='#2c3e50')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Frame de entrada de datos
        input_frame = tk.LabelFrame(main_container,
                                   text="Parámetros de Entrada",
                                   font=('Arial', 12, 'bold'),
                                   fg='white',
                                   bg='#34495e',
                                   relief='raised',
                                   bd=2)
        input_frame.pack(fill=tk.X, pady=10)
        
        # Función
        tk.Label(input_frame, text="Función f(x):", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.func_entry = tk.Entry(input_frame, font=('Arial', 11), width=30)
        self.func_entry.grid(row=0, column=1, padx=10, pady=5)
        self.func_entry.insert(0, "x**2 - 4")  # Ejemplo por defecto
        
        # Intervalo [a, b]
        tk.Label(input_frame, text="Límite inferior (a):", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.a_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.a_entry.grid(row=1, column=1, sticky='w', padx=10, pady=5)
        self.a_entry.insert(0, "0")
        
        tk.Label(input_frame, text="Límite superior (b):", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.b_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.b_entry.grid(row=2, column=1, sticky='w', padx=10, pady=5)
        self.b_entry.insert(0, "3")
        
        # Tolerancia
        tk.Label(input_frame, text="Tolerancia:", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.tolerance_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.tolerance_entry.grid(row=3, column=1, sticky='w', padx=10, pady=5)
        self.tolerance_entry.insert(0, "0.000001")
        
        # Botones
        buttons_frame = tk.Frame(input_frame, bg='#34495e')
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=15)
        
        calculate_button = tk.Button(buttons_frame,
                                   text="CALCULAR",
                                   font=('Arial', 12, 'bold'),
                                   fg='white',
                                   bg='#3498db',
                                   activebackground='#2980b9',
                                   relief='raised',
                                   bd=2,
                                   command=self.calculate)
        calculate_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(buttons_frame,
                               text="LIMPIAR",
                               font=('Arial', 12, 'bold'),
                               fg='white',
                               bg='#f39c12',
                               activebackground='#e67e22',
                               relief='raised',
                               bd=2,
                               command=self.clear_results)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Botón para mostrar gráfica
        plot_button = tk.Button(buttons_frame,
                               text="GRÁFICA",
                               font=('Arial', 12, 'bold'),
                               fg='white',
                               bg='#9b59b6',
                               activebackground='#8e44ad',
                               relief='raised',
                               bd=2,
                               command=self.show_plot)
        plot_button.pack(side=tk.LEFT, padx=5)
        
        # Frame de resultados
        self.results_frame = tk.LabelFrame(main_container,
                                          text="Resultados",
                                          font=('Arial', 12, 'bold'),
                                          fg='white',
                                          bg='#34495e',
                                          relief='raised',
                                          bd=2)
        self.results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Área de texto para mostrar pasos
        self.results_text = tk.Text(self.results_frame,
                                   font=('Courier New', 10),
                                   bg='#ecf0f1',
                                   fg='#2c3e50',
                                   wrap=tk.WORD,
                                   height=15)
        
        scrollbar = tk.Scrollbar(self.results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5)
        
        # Botón para volver
        back_button = tk.Button(self.frame,
                               text="← VOLVER AL MENÚ",
                               font=('Arial', 12),
                               fg='white',
                               bg='#7f8c8d',
                               activebackground='#95a5a6',
                               relief='raised',
                               bd=2,
                               command=self.back_callback)
        back_button.pack(side=tk.BOTTOM, pady=10)
    
    def calculate(self):
        """Ejecuta el método de bisección"""
        try:
            # Obtener valores de entrada
            func_str = self.func_entry.get().strip()
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            tolerance = float(self.tolerance_entry.get())
            
            if not func_str:
                messagebox.showerror("Error", "Por favor ingrese una función")
                return
            
            # Ejecutar método de bisección
            result = bisection_method(func_str, a, b, tolerance)
            
            # Guardar resultado para gráficas
            self.last_result = result
            self.last_func = func_str
            self.last_a = a
            self.last_b = b
            
            # Mostrar resultados
            self.display_results(result, func_str)
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error en los valores de entrada: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")
    
    def display_results(self, result, func_str):
        """Muestra los resultados del método"""
        self.results_text.delete(1.0, tk.END)
        
        # Encabezado
        self.results_text.insert(tk.END, "=" * 80 + "\n")
        self.results_text.insert(tk.END, "MÉTODO DE BISECCIÓN - RESULTADOS\n")
        self.results_text.insert(tk.END, "=" * 80 + "\n\n")
        
        self.results_text.insert(tk.END, f"Función: f(x) = {func_str}\n")
        self.results_text.insert(tk.END, f"Intervalo inicial: [{self.a_entry.get()}, {self.b_entry.get()}]\n")
        self.results_text.insert(tk.END, f"Tolerancia: {self.tolerance_entry.get()}\n\n")
        
        if result['success']:
            self.results_text.insert(tk.END, f"RAÍZ ENCONTRADA: {result['root']:.8f}\n")
            self.results_text.insert(tk.END, f"Iteraciones: {result['iterations']}\n")
            self.results_text.insert(tk.END, f"Error final: {result['final_error']:.2e}\n\n")
        else:
            self.results_text.insert(tk.END, f"ERROR: {result['error']}\n\n")
        
        # Mostrar pasos
        if result['steps']:
            self.results_text.insert(tk.END, "PASOS DEL MÉTODO:\n")
            self.results_text.insert(tk.END, "-" * 80 + "\n")
            self.results_text.insert(tk.END, f"{'Iter':<4} {'a':<12} {'b':<12} {'c':<12} {'f(a)':<12} {'f(c)':<12} {'Error':<12}\n")
            self.results_text.insert(tk.END, "-" * 80 + "\n")
            
            for step in result['steps']:
                # Formatear sin notación científica
                error_str = f"{step['error']:.8f}" if step['error'] >= 0.0001 else f"{step['error']:.2e}"
                self.results_text.insert(tk.END, 
                    f"{step['iteration']:<4} "
                    f"{step['a']:<12.6f} "
                    f"{step['b']:<12.6f} "
                    f"{step['c']:<12.6f} "
                    f"{step['f_a']:<12.6f} "
                    f"{step['f_c']:<12.6f} "
                    f"{error_str:<12}\n")
    
    def show_plot(self):
        """Muestra la gráfica del método de bisección"""
        if not is_matplotlib_available():
            messagebox.showerror("Error", "Matplotlib no está disponible. Instale matplotlib para ver gráficas.")
            return
        
        try:
            if hasattr(self, 'last_result') and self.last_result:
                # Crear ventana para la gráfica
                plot_window = tk.Toplevel(self.parent)
                plot_window.title("Gráfica - Método de Bisección")
                plot_window.geometry("900x700")
                plot_window.configure(bg='#ecf0f1')
                
                # Crear frame para la gráfica
                plot_frame = tk.Frame(plot_window, bg='#ecf0f1')
                plot_frame.pack(fill='both', expand=True, padx=10, pady=10)
                
                # Crear gráfica
                plot_widget = create_bisection_plot(plot_frame, self.last_func, 
                                                   self.last_result['steps'], 
                                                   self.last_a, self.last_b)
                if plot_widget:
                    plot_widget.pack(fill='both', expand=True)
            else:
                messagebox.showinfo("Información", "Primero debe calcular el método para mostrar la gráfica")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la gráfica: {str(e)}")
    
    def clear_results(self):
        """Limpia el área de resultados"""
        self.results_text.delete(1.0, tk.END)
        if hasattr(self, 'last_result'):
            self.last_result = None
    
    def destroy(self):
        """Destruye el frame de la ventana"""
        self.frame.destroy()