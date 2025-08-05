#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ventana para el método de Runge-Kutta (RK4)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from numerical_methods.methods import runge_kutta_method
from numerical_methods.plotting import create_differential_equation_plot, is_matplotlib_available

class RungeKuttaWindow:
    """Ventana para el método de Runge-Kutta de cuarto orden"""
    
    def __init__(self, parent, back_callback):
        self.parent = parent
        self.back_callback = back_callback
        
        # Frame principal
        self.frame = tk.Frame(parent, bg='#2c3e50')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la ventana de Runge-Kutta"""
        
        # Título
        title_label = tk.Label(self.frame,
                              text="MÉTODO DE RUNGE-KUTTA (RK4)",
                              font=('Arial', 20, 'bold'),
                              fg='white',
                              bg='#2c3e50',
                              pady=15)
        title_label.pack()
        
        # Subtítulo explicativo
        subtitle_label = tk.Label(self.frame,
                                 text="Método de cuarto orden para ecuaciones diferenciales: dy/dx = f(x,y)",
                                 font=('Arial', 12, 'italic'),
                                 fg='#ecf0f1',
                                 bg='#2c3e50',
                                 pady=5)
        subtitle_label.pack()
        
        # Frame principal
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
        
        # Función f(x,y)
        tk.Label(input_frame, text="Función f(x,y):", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.func_entry = tk.Entry(input_frame, font=('Arial', 11), width=30)
        self.func_entry.grid(row=0, column=1, padx=10, pady=5)
        self.func_entry.insert(0, "x + y")  # Ejemplo por defecto
        
        # Condiciones iniciales
        tk.Label(input_frame, text="Valor inicial x₀:", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.x0_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.x0_entry.grid(row=1, column=1, sticky='w', padx=10, pady=5)
        self.x0_entry.insert(0, "0")
        
        tk.Label(input_frame, text="Valor inicial y₀:", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.y0_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.y0_entry.grid(row=2, column=1, sticky='w', padx=10, pady=5)
        self.y0_entry.insert(0, "1")
        
        # Parámetros del método
        tk.Label(input_frame, text="Tamaño del paso (h):", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.h_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.h_entry.grid(row=3, column=1, sticky='w', padx=10, pady=5)
        self.h_entry.insert(0, "0.1")
        
        tk.Label(input_frame, text="Valor final de x:", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=4, column=0, sticky='w', padx=10, pady=5)
        self.x_final_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.x_final_entry.grid(row=4, column=1, sticky='w', padx=10, pady=5)
        self.x_final_entry.insert(0, "1")
        
        # Nota explicativa
        note_label = tk.Label(input_frame,
                             text="Nota: Use 'x' e 'y' en la función. RK4 es más preciso que Euler",
                             font=('Arial', 9, 'italic'),
                             fg='#bdc3c7',
                             bg='#34495e')
        note_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Botones
        buttons_frame = tk.Frame(input_frame, bg='#34495e')
        buttons_frame.grid(row=6, column=0, columnspan=2, pady=15)
        
        calculate_button = tk.Button(buttons_frame,
                                   text="CALCULAR",
                                   font=('Arial', 12, 'bold'),
                                   fg='white',
                                   bg='#27ae60',
                                   activebackground='#2ecc71',
                                   relief='raised',
                                   bd=2,
                                   command=self.calculate)
        calculate_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(buttons_frame,
                               text="LIMPIAR",
                               font=('Arial', 12, 'bold'),
                               fg='white',
                               bg='#95a5a6',
                               activebackground='#7f8c8d',
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
                                   font=('Courier New', 9),
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
        """Ejecuta el método de Runge-Kutta"""
        try:
            # Obtener valores de entrada
            func_str = self.func_entry.get().strip()
            x0 = float(self.x0_entry.get())
            y0 = float(self.y0_entry.get())
            h = float(self.h_entry.get())
            x_final = float(self.x_final_entry.get())
            
            if not func_str:
                messagebox.showerror("Error", "Por favor ingrese una función")
                return
            
            if h <= 0:
                messagebox.showerror("Error", "El tamaño del paso debe ser positivo")
                return
            
            if x_final <= x0:
                messagebox.showerror("Error", "El valor final de x debe ser mayor que x₀")
                return
            
            # Ejecutar método de Runge-Kutta
            result = runge_kutta_method(func_str, x0, y0, h, x_final)
            
            # Guardar resultado para gráficas
            self.last_result = result
            self.last_func = func_str
            
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
        self.results_text.insert(tk.END, "=" * 90 + "\n")
        self.results_text.insert(tk.END, "MÉTODO DE RUNGE-KUTTA (RK4) - RESULTADOS\n")
        self.results_text.insert(tk.END, "=" * 90 + "\n\n")
        
        self.results_text.insert(tk.END, f"Ecuación diferencial: dy/dx = {func_str}\n")
        self.results_text.insert(tk.END, f"Condiciones iniciales: x₀ = {self.x0_entry.get()}, y₀ = {self.y0_entry.get()}\n")
        self.results_text.insert(tk.END, f"Tamaño del paso: h = {self.h_entry.get()}\n")
        self.results_text.insert(tk.END, f"Intervalo: [{self.x0_entry.get()}, {self.x_final_entry.get()}]\n\n")
        
        if result['success']:
            self.results_text.insert(tk.END, f"SOLUCIÓN FINAL:\n")
            self.results_text.insert(tk.END, f"x = {result['final_x']:.6f}\n")
            self.results_text.insert(tk.END, f"y = {result['final_y']:.6f}\n\n")
        
        # Mostrar pasos
        if result['steps']:
            self.results_text.insert(tk.END, "PASOS DEL MÉTODO:\n")
            self.results_text.insert(tk.END, "-" * 90 + "\n")
            self.results_text.insert(tk.END, f"{'Paso':<4} {'xᵢ':<10} {'yᵢ':<10} {'k₁':<10} {'k₂':<10} {'k₃':<10} {'k₄':<10} {'yᵢ₊₁':<10}\n")
            self.results_text.insert(tk.END, "-" * 90 + "\n")
            
            for step in result['steps']:
                if step['iteration'] == 0:  # Condición inicial
                    self.results_text.insert(tk.END, 
                        f"{step['iteration']:<4} "
                        f"{step['x']:<10.8g} "
                        f"{step['y']:<10.8g} "
                        f"{'---':<10} "
                        f"{'---':<10} "
                        f"{'---':<10} "
                        f"{'---':<10} "
                        f"{'(inicial)':<10}\n")
                else:
                    self.results_text.insert(tk.END, 
                        f"{step['iteration']:<4} "
                        f"{step['x']:<10.8g} "
                        f"{step['y']:<10.8g} "
                        f"{step['k1']:<10.8g} "
                        f"{step['k2']:<10.8g} "
                        f"{step['k3']:<10.8g} "
                        f"{step['k4']:<10.8g} "
                        f"{step['y_new']:<10.8g}\n")
            
            # Explicación del método
            self.results_text.insert(tk.END, "\n" + "=" * 90 + "\n")
            self.results_text.insert(tk.END, "EXPLICACIÓN DEL MÉTODO RUNGE-KUTTA (RK4):\n")
            self.results_text.insert(tk.END, "=" * 90 + "\n")
            self.results_text.insert(tk.END, "El método RK4 utiliza las siguientes fórmulas:\n\n")
            self.results_text.insert(tk.END, "k₁ = h × f(xᵢ, yᵢ)\n")
            self.results_text.insert(tk.END, "k₂ = h × f(xᵢ + h/2, yᵢ + k₁/2)\n")
            self.results_text.insert(tk.END, "k₃ = h × f(xᵢ + h/2, yᵢ + k₂/2)\n")
            self.results_text.insert(tk.END, "k₄ = h × f(xᵢ + h, yᵢ + k₃)\n\n")
            self.results_text.insert(tk.END, "yᵢ₊₁ = yᵢ + (k₁ + 2k₂ + 2k₃ + k₄)/6\n")
            self.results_text.insert(tk.END, "xᵢ₊₁ = xᵢ + h\n\n")
            self.results_text.insert(tk.END, "Ventajas del RK4:\n")
            self.results_text.insert(tk.END, "• Mayor precisión que el método de Euler\n")
            self.results_text.insert(tk.END, "• Error de truncamiento de orden O(h⁵)\n")
            self.results_text.insert(tk.END, "• Estabilidad numérica mejorada\n")
            self.results_text.insert(tk.END, "• Ampliamente utilizado en aplicaciones prácticas\n")
    
    def show_plot(self):
        """Muestra la gráfica del método de Runge-Kutta"""
        if not is_matplotlib_available():
            messagebox.showerror("Error", "Matplotlib no está disponible. Instale matplotlib para ver gráficas.")
            return
        
        try:
            if hasattr(self, 'last_result') and self.last_result:
                # Crear ventana para la gráfica
                plot_window = tk.Toplevel(self.parent)
                plot_window.title("Gráfica - Método de Runge-Kutta (RK4)")
                plot_window.geometry("900x700")
                plot_window.configure(bg='#ecf0f1')
                
                # Crear frame para la gráfica
                plot_frame = tk.Frame(plot_window, bg='#ecf0f1')
                plot_frame.pack(fill='both', expand=True, padx=10, pady=10)
                
                # Crear gráfica
                plot_widget = create_differential_equation_plot(plot_frame, self.last_func, 
                                                               self.last_result['steps'], 
                                                               "Runge-Kutta (RK4)")
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