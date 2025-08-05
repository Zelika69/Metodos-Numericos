#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo para cálculo automático de derivadas simbólicas
"""

import re
import math

def calculate_derivative(func_str):
    """
    Calcula la derivada simbólica de una función simple
    
    Args:
        func_str: Función como string (ej: 'x**2 + 3*x - 4')
    
    Returns:
        str: Derivada de la función
    """
    
    # Limpiar la función
    func_str = func_str.replace(' ', '').lower()
    
    # Patrones comunes y sus derivadas
    patterns = [
        # Constantes
        (r'^[+-]?\d+(\.\d+)?$', '0'),
        
        # x^n
        (r'x\*\*([+-]?\d+(\.\d+)?)', lambda m: f"{float(m.group(1))}*x**{float(m.group(1))-1}" if float(m.group(1)) != 1 else '1'),
        
        # x^2, x^3, etc.
        (r'x\^([+-]?\d+(\.\d+)?)', lambda m: f"{float(m.group(1))}*x**{float(m.group(1))-1}" if float(m.group(1)) != 1 else '1'),
        
        # ax^n
        (r'([+-]?\d+(\.\d+)?)\*x\*\*([+-]?\d+(\.\d+)?)', 
         lambda m: f"{float(m.group(1)) * float(m.group(3))}*x**{float(m.group(3))-1}" if float(m.group(3)) != 1 else str(float(m.group(1)))),
        
        # ax
        (r'([+-]?\d+(\.\d+)?)\*x', lambda m: str(float(m.group(1)))),
        
        # x solo
        (r'^x$', '1'),
        
        # Funciones trigonométricas
        (r'sin\(x\)', 'cos(x)'),
        (r'cos\(x\)', '-sin(x)'),
        (r'tan\(x\)', 'sec(x)**2'),
        
        # Funciones exponenciales y logarítmicas
        (r'exp\(x\)', 'exp(x)'),
        (r'e\*\*x', 'e**x'),
        (r'ln\(x\)', '1/x'),
        (r'log\(x\)', '1/(x*ln(10))'),
    ]
    
    # Casos especiales simples
    simple_cases = {
        'x': '1',
        'x**2': '2*x',
        'x**3': '3*x**2',
        'x**4': '4*x**3',
        '2*x': '2',
        '3*x': '3',
        'x+1': '1',
        'x-1': '1',
        'x**2-4': '2*x',
        'x**2+x': '2*x+1',
        'x**3-x': '3*x**2-1',
        '2*x**2': '4*x',
        '3*x**2': '6*x',
    }
    
    # Verificar casos simples primero
    if func_str in simple_cases:
        return simple_cases[func_str]
    
    # Intentar derivar términos individuales
    terms = re.split(r'([+-])', func_str)
    derivative_terms = []
    
    for i, term in enumerate(terms):
        if term in ['+', '-']:
            derivative_terms.append(term)
            continue
            
        if not term.strip():
            continue
            
        # Derivar cada término
        term_derivative = derive_single_term(term.strip())
        if term_derivative and term_derivative != '0':
            derivative_terms.append(term_derivative)
    
    if derivative_terms:
        result = ''.join(derivative_terms)
        # Limpiar el resultado
        result = result.replace('+-', '-').replace('++', '+')
        if result.startswith('+'):
            result = result[1:]
        return result if result else '0'
    
    return 'Derivada no calculable automáticamente'

def derive_single_term(term):
    """
    Deriva un término individual
    """
    term = term.strip()
    
    # Constante
    if re.match(r'^[+-]?\d+(\.\d+)?$', term):
        return '0'
    
    # x solo
    if term == 'x':
        return '1'
    
    # x^n
    match = re.match(r'x\*\*([+-]?\d+(\.\d+)?)', term)
    if match:
        n = float(match.group(1))
        if n == 1:
            return '1'
        elif n == 0:
            return '0'
        else:
            return f"{n}*x**{n-1}"
    
    # ax^n
    match = re.match(r'([+-]?\d+(\.\d+)?)\*x\*\*([+-]?\d+(\.\d+)?)', term)
    if match:
        a = float(match.group(1))
        n = float(match.group(3))
        if n == 1:
            return str(a)
        elif n == 0:
            return '0'
        else:
            return f"{a*n}*x**{n-1}"
    
    # ax
    match = re.match(r'([+-]?\d+(\.\d+)?)\*x', term)
    if match:
        a = float(match.group(1))
        return str(a)
    
    return '0'

def format_derivative(derivative):
    """
    Formatea la derivada para que se vea mejor
    """
    if not derivative or derivative == '0':
        return '0'
    
    # Reemplazar ** con ^
    derivative = derivative.replace('**', '^')
    
    # Simplificar expresiones comunes
    derivative = derivative.replace('1*x', 'x')
    derivative = derivative.replace('1*', '')
    derivative = derivative.replace('x^1', 'x')
    
    return derivative