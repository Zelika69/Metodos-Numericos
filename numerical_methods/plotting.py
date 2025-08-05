#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo para generar gráficas de métodos numéricos
"""

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import numpy as np
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Matplotlib no está disponible. Las gráficas no se mostrarán.")

import tkinter as tk
from tkinter import messagebox

def create_bisection_plot(parent_frame, func_str, steps, a_initial, b_initial):
    """
    Crea una gráfica para el método de bisección
    """
    if not MATPLOTLIB_AVAILABLE:
        return None
    
    try:
        # Crear figura
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_facecolor('#ecf0f1')
        
        # Definir función
        def f(x):
            return eval(func_str.replace('x', str(x)))
        
        # Crear rango de x
        x_range = np.linspace(a_initial - 1, b_initial + 1, 1000)
        y_range = [f(x) for x in x_range]
        
        # Graficar función
        ax.plot(x_range, y_range, 'b-', linewidth=2, label=f'f(x) = {func_str}')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Marcar puntos de bisección
        colors = plt.cm.viridis(np.linspace(0, 1, len(steps)))
        for i, step in enumerate(steps[:5]):  # Mostrar solo primeros 5 pasos
            ax.plot(step['c'], f(step['c']), 'o', color=colors[i], 
                   markersize=8, label=f'Iteración {step["iteration"]}')
            ax.axvline(x=step['c'], color=colors[i], linestyle='--', alpha=0.5)
        
        # Configurar gráfica
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Método de Bisección')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Crear canvas para Tkinter
        canvas = FigureCanvasTkAgg(fig, parent_frame)
        canvas.draw()
        return canvas.get_tk_widget()
        
    except Exception as e:
        messagebox.showerror("Error en gráfica", f"No se pudo generar la gráfica: {str(e)}")
        return None

def create_newton_raphson_plot(parent_frame, func_str, derivative_str, steps, x0):
    """
    Crea una gráfica para el método de Newton-Raphson
    """
    if not MATPLOTLIB_AVAILABLE:
        return None
    
    try:
        # Crear figura
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_facecolor('#ecf0f1')
        
        # Definir funciones
        def f(x):
            return eval(func_str.replace('x', str(x)))
        
        def df(x):
            return eval(derivative_str.replace('x', str(x)))
        
        # Crear rango de x
        x_min = min([step['x'] for step in steps] + [x0]) - 2
        x_max = max([step['x'] for step in steps] + [x0]) + 2
        x_range = np.linspace(x_min, x_max, 1000)
        y_range = [f(x) for x in x_range]
        
        # Graficar función
        ax.plot(x_range, y_range, 'b-', linewidth=2, label=f'f(x) = {func_str}')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Marcar iteraciones
        colors = plt.cm.plasma(np.linspace(0, 1, len(steps)))
        for i, step in enumerate(steps[:5]):  # Mostrar solo primeros 5 pasos
            x_curr = step['x']
            y_curr = f(x_curr)
            
            # Punto en la función
            ax.plot(x_curr, y_curr, 'o', color=colors[i], 
                   markersize=8, label=f'Iteración {step["iteration"]}')
            
            # Línea tangente
            if i < len(steps) - 1:
                slope = df(x_curr)
                x_tangent = np.linspace(x_curr - 1, x_curr + 1, 100)
                y_tangent = y_curr + slope * (x_tangent - x_curr)
                ax.plot(x_tangent, y_tangent, '--', color=colors[i], alpha=0.7)
        
        # Configurar gráfica
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Método de Newton-Raphson')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Crear canvas para Tkinter
        canvas = FigureCanvasTkAgg(fig, parent_frame)
        canvas.draw()
        return canvas.get_tk_widget()
        
    except Exception as e:
        messagebox.showerror("Error en gráfica", f"No se pudo generar la gráfica: {str(e)}")
        return None

def create_differential_equation_plot(parent_frame, func_str, steps, method_name):
    """
    Crea una gráfica para métodos de ecuaciones diferenciales
    """
    if not MATPLOTLIB_AVAILABLE:
        return None
    
    try:
        # Crear figura
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_facecolor('#ecf0f1')
        
        # Extraer datos de los pasos
        x_values = [step['x'] for step in steps]
        y_values = [step['y'] for step in steps]
        
        # Graficar solución numérica
        ax.plot(x_values, y_values, 'ro-', linewidth=2, markersize=6, 
               label=f'Solución {method_name}')
        
        # Marcar puntos importantes
        ax.plot(x_values[0], y_values[0], 'go', markersize=10, label='Punto inicial')
        ax.plot(x_values[-1], y_values[-1], 'bo', markersize=10, label='Punto final')
        
        # Configurar gráfica
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'{method_name} - Solución de dy/dx = {func_str}')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Crear canvas para Tkinter
        canvas = FigureCanvasTkAgg(fig, parent_frame)
        canvas.draw()
        return canvas.get_tk_widget()
        
    except Exception as e:
        messagebox.showerror("Error en gráfica", f"No se pudo generar la gráfica: {str(e)}")
        return None

def is_matplotlib_available():
    """
    Verifica si matplotlib está disponible
    """
    return MATPLOTLIB_AVAILABLE