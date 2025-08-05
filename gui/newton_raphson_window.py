#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ventana para el método de Newton-Raphson
"""

import tkinter as tk
from tkinter import ttk, messagebox
from numerical_methods.methods import newton_raphson_method
from numerical_methods.derivatives import calculate_derivative, format_derivative
from numerical_methods.plotting import create_newton_raphson_plot, is_matplotlib_available

class NewtonRaphsonWindow:
    """Ventana para el método de Newton-Raphson"""
    
    def __init__(self, parent, back_callback):
        self.parent = parent
        self.back_callback = back_callback
        
        # Frame principal
        self.frame = tk.Frame(parent, bg='#2c3e50')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la ventana de Newton-Raphson"""
        
        # Título
        title_label = tk.Label(self.frame,
                              text="MÉTODO DE NEWTON-RAPHSON",
                              font=('Arial', 20, 'bold'),
                              fg='white',
                              bg='#2c3e50',
                              pady=15)
        title_label.pack()
        
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
        
        # Función
        tk.Label(input_frame, text="Función f(x):", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.func_entry = tk.Entry(input_frame, font=('Arial', 11), width=30)
        self.func_entry.grid(row=0, column=1, padx=10, pady=5)
        self.func_entry.insert(0, "x**2 - 4")  # Ejemplo por defecto
        
        # Derivada
        tk.Label(input_frame, text="Derivada f'(x):", 
                 font=('Arial', 11), fg='white', bg='#34495e').grid(row=1, column=0, sticky='w', padx=10, pady=5)
        
        derivative_frame = tk.Frame(input_frame, bg='#34495e')
        derivative_frame.grid(row=1, column=1, sticky='w', padx=10, pady=5)
        
        self.derivative_entry = tk.Entry(derivative_frame, font=('Arial', 11), width=20)
        self.derivative_entry.pack(side='left')
        self.derivative_entry.insert(0, "2*x")  # Ejemplo por defecto
        
        # Botón para calcular derivada automáticamente
        self.auto_derivative_btn = tk.Button(derivative_frame, text="Auto", 
                                           font=('Arial', 10, 'bold'),
                                           bg='#3498db', fg='white',
                                           command=self.calculate_auto_derivative,
                                           width=5)
        self.auto_derivative_btn.pack(side='left', padx=(5, 0))
        
        # Valor inicial
        tk.Label(input_frame, text="Valor inicial (x₀):", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.x0_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.x0_entry.grid(row=2, column=1, sticky='w', padx=10, pady=5)
        self.x0_entry.insert(0, "3")
        
        # Tolerancia
        tk.Label(input_frame, text="Tolerancia:", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.tolerance_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.tolerance_entry.grid(row=3, column=1, sticky='w', padx=10, pady=5)
        self.tolerance_entry.insert(0, "0.000001")
        
        # Máximo de iteraciones
        tk.Label(input_frame, text="Máx. iteraciones:", 
                font=('Arial', 11), fg='white', bg='#34495e').grid(row=4, column=0, sticky='w', padx=10, pady=5)
        self.max_iter_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.max_iter_entry.grid(row=4, column=1, sticky='w', padx=10, pady=5)
        self.max_iter_entry.insert(0, "100")
        
        # Botones
        buttons_frame = tk.Frame(input_frame, bg='#34495e')
        buttons_frame.grid(row=5, column=0, columnspan=2, pady=15)
        
        calculate_button = tk.Button(buttons_frame,
                                   text="CALCULAR",
                                   font=('Arial', 12, 'bold'),
                                   fg='white',
                                   bg='#e74c3c',
                                   activebackground='#c0392b',
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
        """Ejecuta el método de Newton-Raphson"""
        try:
            # Obtener valores de entrada
            func_str = self.func_entry.get().strip()
            derivative_str = self.derivative_entry.get().strip()
            x0 = float(self.x0_entry.get())
            tolerance = float(self.tolerance_entry.get())
            max_iterations = int(self.max_iter_entry.get())
            
            if not func_str or not derivative_str:
                messagebox.showerror("Error", "Por favor ingrese la función y su derivada")
                return
            
            # Ejecutar método de Newton-Raphson
            result = newton_raphson_method(func_str, derivative_str, x0, tolerance, max_iterations)
            
            # Guardar resultado para gráficas
            self.last_result = result
            
            # Mostrar resultados
            self.display_results(result, func_str, derivative_str)
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error en los valores de entrada: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")
    
    def display_results(self, result, func_str, derivative_str):
        """Muestra los resultados del método"""
        self.results_text.delete(1.0, tk.END)
        
        # Encabezado
        self.results_text.insert(tk.END, "=" * 80 + "\n")
        self.results_text.insert(tk.END, "MÉTODO DE NEWTON-RAPHSON - RESULTADOS\n")
        self.results_text.insert(tk.END, "=" * 80 + "\n\n")
        
        self.results_text.insert(tk.END, f"Función: f(x) = {func_str}\n")
        self.results_text.insert(tk.END, f"Derivada: f'(x) = {derivative_str}\n")
        self.results_text.insert(tk.END, f"Valor inicial: x₀ = {self.x0_entry.get()}\n")
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
            self.results_text.insert(tk.END, "-" * 85 + "\n")
            self.results_text.insert(tk.END, f"{'Iter':<4} {'xₙ':<15} {'f(xₙ)':<15} {'f(xₙ)':<15} {'xₙ₊₁':<15} {'Error':<12}\n")
            self.results_text.insert(tk.END, "-" * 85 + "\n")
            
            for step in result['steps']:
                # Formatear sin notación científica
                error_str = f"{step['error']:.8f}" if step['error'] >= 0.0001 else f"{step['error']:.2e}"
                self.results_text.insert(tk.END, 
                    f"{step['iteration']:<4} "
                    f"{step['x']:<15.8f} "
                    f"{step['f_x']:<15.8f} "
                    f"{step['df_x']:<15.8f} "
                    f"{step['x_new']:<15.8f} "
                    f"{error_str:<12}\n")
            
            # Explicación del método
            self.results_text.insert(tk.END, "\n" + "=" * 80 + "\n")
            self.results_text.insert(tk.END, "EXPLICACIÓN DEL MÉTODO:\n")
            self.results_text.insert(tk.END, "=" * 80 + "\n")
            self.results_text.insert(tk.END, "El método de Newton-Raphson utiliza la fórmula:\n")
            self.results_text.insert(tk.END, "xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)\n\n")
            self.results_text.insert(tk.END, "Donde:\n")
            self.results_text.insert(tk.END, "• xₙ es la aproximación actual\n")
            self.results_text.insert(tk.END, "• f(xₙ) es el valor de la función en xₙ\n")
            self.results_text.insert(tk.END, "• f'(xₙ) es el valor de la derivada en xₙ\n")
            self.results_text.insert(tk.END, "• xₙ₊₁ es la nueva aproximación\n")
    
    def calculate_auto_derivative(self):
        """Calcula automáticamente la derivada de la función"""
        try:
            func_str = self.func_entry.get().strip()
            if not func_str:
                messagebox.showwarning("Advertencia", "Por favor ingrese una función primero")
                return
            
            derivative = calculate_derivative(func_str)
            formatted_derivative = format_derivative(derivative)
            
            self.derivative_entry.delete(0, tk.END)
            self.derivative_entry.insert(0, formatted_derivative)
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo calcular la derivada: {str(e)}")
    
    def show_plot(self):
        """Muestra la gráfica del método de Newton-Raphson"""
        if not is_matplotlib_available():
            messagebox.showerror("Error", "Matplotlib no está disponible. Instale matplotlib para ver gráficas.")
            return
        
        try:
            func_str = self.func_entry.get().strip()
            x0 = float(self.x0_entry.get())
            
            if not func_str:
                messagebox.showerror("Error", "Por favor ingrese una función")
                return
            
            # Obtener los resultados del último cálculo si están disponibles
            if hasattr(self, 'last_result') and self.last_result:
                 derivative_str = self.derivative_entry.get().strip()
                 
                 # Crear ventana para la gráfica
                 plot_window = tk.Toplevel(self.parent)
                 plot_window.title("Gráfica - Método de Newton-Raphson")
                 plot_window.geometry("900x700")
                 plot_window.configure(bg='#ecf0f1')
                 
                 # Crear frame para la gráfica
                 plot_frame = tk.Frame(plot_window, bg='#ecf0f1')
                 plot_frame.pack(fill='both', expand=True, padx=10, pady=10)
                 
                 # Crear gráfica
                 plot_widget = create_newton_raphson_plot(plot_frame, func_str, derivative_str, 
                                                         self.last_result['steps'], x0)
                 if plot_widget:
                     plot_widget.pack(fill='both', expand=True)
            else:
                messagebox.showinfo("Información", "Primero debe calcular el método para mostrar la gráfica")
                
        except ValueError:
            messagebox.showerror("Error", "Valor inicial inválido")
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