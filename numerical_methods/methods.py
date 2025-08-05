#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementaciones de métodos numéricos
Lógica matemática separada de la interfaz gráfica
"""

import math

def bisection_method(func_str, a, b, tolerance=1e-6, max_iterations=100):
    """
    Método de Bisección para encontrar raíces de ecuaciones
    
    Args:
        func_str: Función como string (ej: 'x**2 - 4')
        a: Límite inferior del intervalo
        b: Límite superior del intervalo
        tolerance: Tolerancia para el error
        max_iterations: Número máximo de iteraciones
    
    Returns:
        dict: Resultados del método incluyendo pasos y resultado final
    """
    
    # Convertir string a función
    def f(x):
        return eval(func_str.replace('x', str(x)))
    
    steps = []
    iteration = 0
    
    # Verificar que hay cambio de signo
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        return {
            'success': False,
            'error': 'No hay cambio de signo en el intervalo dado',
            'steps': [],
            'result': None
        }
    
    while iteration < max_iterations:
        c = (a + b) / 2
        fc = f(c)
        
        step = {
            'iteration': iteration + 1,
            'a': a,
            'b': b,
            'c': c,
            'f_a': fa,
            'f_b': fb,
            'f_c': fc,
            'error': abs(b - a) / 2
        }
        steps.append(step)
        
        if abs(fc) < tolerance or abs(b - a) / 2 < tolerance:
            return {
                'success': True,
                'root': c,
                'iterations': iteration + 1,
                'final_error': abs(b - a) / 2,
                'steps': steps
            }
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iteration += 1
    
    return {
        'success': False,
        'error': 'Máximo número de iteraciones alcanzado',
        'steps': steps,
        'result': (a + b) / 2
    }

def newton_raphson_method(func_str, derivative_str, x0, tolerance=1e-6, max_iterations=100):
    """
    Método de Newton-Raphson para encontrar raíces
    
    Args:
        func_str: Función como string
        derivative_str: Derivada de la función como string
        x0: Valor inicial
        tolerance: Tolerancia para el error
        max_iterations: Número máximo de iteraciones
    
    Returns:
        dict: Resultados del método
    """
    
    def f(x):
        return eval(func_str.replace('x', str(x)))
    
    def df(x):
        return eval(derivative_str.replace('x', str(x)))
    
    steps = []
    x = x0
    
    for iteration in range(max_iterations):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-12:
            return {
                'success': False,
                'error': 'Derivada muy pequeña, posible división por cero',
                'steps': steps
            }
        
        x_new = x - fx / dfx
        error = abs(x_new - x)
        
        step = {
            'iteration': iteration + 1,
            'x': x,
            'f_x': fx,
            'df_x': dfx,
            'x_new': x_new,
            'error': error
        }
        steps.append(step)
        
        if error < tolerance:
            return {
                'success': True,
                'root': x_new,
                'iterations': iteration + 1,
                'final_error': error,
                'steps': steps
            }
        
        x = x_new
    
    return {
        'success': False,
        'error': 'Máximo número de iteraciones alcanzado',
        'steps': steps,
        'result': x
    }

def euler_method(func_str, x0, y0, h, x_final):
    """
    Método de Euler para resolver ecuaciones diferenciales
    
    Args:
        func_str: Función f(x,y) como string (ej: 'x + y')
        x0: Valor inicial de x
        y0: Valor inicial de y
        h: Tamaño del paso
        x_final: Valor final de x
    
    Returns:
        dict: Resultados del método
    """
    
    def f(x, y):
        # Reemplazar x e y en la función
        expr = func_str.replace('x', str(x)).replace('y', str(y))
        return eval(expr)
    
    steps = []
    x = x0
    y = y0
    
    step = {
        'iteration': 0,
        'x': x,
        'y': y,
        'f_xy': f(x, y),
        'y_new': y
    }
    steps.append(step)
    
    iteration = 1
    while x < x_final:
        if x + h > x_final:
            h = x_final - x
        
        fxy = f(x, y)
        y_new = y + h * fxy
        x_new = x + h
        
        step = {
            'iteration': iteration,
            'x': x,
            'y': y,
            'f_xy': fxy,
            'y_new': y_new
        }
        steps.append(step)
        
        x = x_new
        y = y_new
        iteration += 1
    
    return {
        'success': True,
        'final_x': x,
        'final_y': y,
        'steps': steps
    }

def runge_kutta_method(func_str, x0, y0, h, x_final):
    """
    Método de Runge-Kutta de cuarto orden (RK4)
    
    Args:
        func_str: Función f(x,y) como string
        x0: Valor inicial de x
        y0: Valor inicial de y
        h: Tamaño del paso
        x_final: Valor final de x
    
    Returns:
        dict: Resultados del método
    """
    
    def f(x, y):
        expr = func_str.replace('x', str(x)).replace('y', str(y))
        return eval(expr)
    
    steps = []
    x = x0
    y = y0
    
    step = {
        'iteration': 0,
        'x': x,
        'y': y,
        'k1': 0,
        'k2': 0,
        'k3': 0,
        'k4': 0,
        'y_new': y
    }
    steps.append(step)
    
    iteration = 1
    while x < x_final:
        if x + h > x_final:
            h = x_final - x
        
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_new = x + h
        
        step = {
            'iteration': iteration,
            'x': x,
            'y': y,
            'k1': k1,
            'k2': k2,
            'k3': k3,
            'k4': k4,
            'y_new': y_new
        }
        steps.append(step)
        
        x = x_new
        y = y_new
        iteration += 1
    
    return {
        'success': True,
        'final_x': x,
        'final_y': y,
        'steps': steps
    }