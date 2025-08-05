#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ventana para el método de Euler
"""

import tkinter as tk
from tkinter import ttk, messagebox
from numerical_methods.methods import euler_method
from numerical_methods.plotting import create_differential_equation_plot, is_matplotlib_available

class EulerWindow:
    """Ventana para el método de Euler"""
    
    def __init__(self, parent, back_callback):
        self.parent = parent
        self.back_callback = back_callback
        
        # Frame principal
        self.frame = tk.Frame(parent, bg='#2c3e50')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la ventana de Euler"""
        
        # Título
        title_label = tk.Label(self.frame,
                              text="MÉTODO DE EULER",
                              font=('Arial', 20, 'bold'),
                              fg='white',
                              bg='#2c3e50',
                              pady=15)
        title_label.pack()
        
        # Subtítulo explicativo
        subtitle_label = tk.Label(self.frame,
                                 text="Resolución numérica de ecuaciones diferenciales: dy/dx = f(x,y)",
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
                             text="Nota: Use 'x' e 'y' en la función. Ejemplo: x + y, x*y, x**2 + y**2",
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
                                   bg='#f39c12',
                                   activebackground='#e67e22',
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
                                   font=('Courier New', 10),
                                   bg='#ecf0f1',
                                   fg='#2c3e50',
                                   wrap=tk.WORD,
                                   height=12)
        
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
        """Ejecuta el método de Euler"""
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
            
            # Ejecutar método de Euler
            result = euler_method(func_str, x0, y0, h, x_final)
            
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
        self.results_text.insert(tk.END, "=" * 80 + "\n")
        self.results_text.insert(tk.END, "MÉTODO DE EULER - RESULTADOS\n")
        self.results_text.insert(tk.END, "=" * 80 + "\n\n")
        
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
            self.results_text.insert(tk.END, "-" * 70 + "\n")
            self.results_text.insert(tk.END, f"{'Paso':<4} {'xᵢ':<12} {'yᵢ':<12} {'f(xᵢ,yᵢ)':<12} {'yᵢ₊₁':<12}\n")
            self.results_text.insert(tk.END, "-" * 70 + "\n")
            
            for step in result['steps']:
                self.results_text.insert(tk.END, 
                    f"{step['iteration']:<4} "
                    f"{step['x']:<12.8g} "
                    f"{step['y']:<12.8g} "
                    f"{step['f_xy']:<12.8g} "
                    f"{step['y_new']:<12.8g}\n")
            
            # Explicación del método
            self.results_text.insert(tk.END, "\n" + "=" * 80 + "\n")
            self.results_text.insert(tk.END, "EXPLICACIÓN DEL MÉTODO:\n")
            self.results_text.insert(tk.END, "=" * 80 + "\n")
            self.results_text.insert(tk.END, "El método de Euler utiliza la fórmula:\n")
            self.results_text.insert(tk.END, "yᵢ₊₁ = yᵢ + h × f(xᵢ, yᵢ)\n")
            self.results_text.insert(tk.END, "xᵢ₊₁ = xᵢ + h\n\n")
            self.results_text.insert(tk.END, "Donde:\n")
            self.results_text.insert(tk.END, "• h es el tamaño del paso\n")
            self.results_text.insert(tk.END, "• f(xᵢ, yᵢ) es la función evaluada en el punto actual\n")
            self.results_text.insert(tk.END, "• (xᵢ, yᵢ) es el punto actual\n")
            self.results_text.insert(tk.END, "• (xᵢ₊₁, yᵢ₊₁) es el siguiente punto aproximado\n")
    
    def show_plot(self):
        """Muestra la gráfica del método de Euler"""
        if not is_matplotlib_available():
            messagebox.showerror("Error", "Matplotlib no está disponible. Instale matplotlib para ver gráficas.")
            return
        
        try:
            if hasattr(self, 'last_result') and self.last_result:
                # Crear ventana para la gráfica
                plot_window = tk.Toplevel(self.parent)
                plot_window.title("Gráfica - Método de Euler")
                plot_window.geometry("900x700")
                plot_window.configure(bg='#ecf0f1')
                
                # Crear frame para la gráfica
                plot_frame = tk.Frame(plot_window, bg='#ecf0f1')
                plot_frame.pack(fill='both', expand=True, padx=10, pady=10)
                
                # Crear gráfica
                plot_widget = create_differential_equation_plot(plot_frame, self.last_func, 
                                                               self.last_result['steps'], 
                                                               "Euler")
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