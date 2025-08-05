# Solucionador de Métodos Numéricos

## Descripción

Herramienta educativa desarrollada en Python con interfaz gráfica Tkinter para resolver problemas de métodos numéricos. Diseñada especialmente para estudiantes de ingeniería que necesitan comprender y aplicar métodos numéricos fundamentales.

## Características

### Métodos Implementados

1. **Método de Bisección**
   - Encuentra raíces de ecuaciones en intervalos dados
   - Muestra pasos detallados del proceso iterativo
   - Calcula error en cada iteración

2. **Método de Newton-Raphson**
   - Método iterativo para encontrar raíces
   - Requiere función y su derivada
   - Convergencia rápida cuando es aplicable

3. **Método de Euler**
   - Resolución numérica de ecuaciones diferenciales
   - Implementación del método de primer orden
   - Visualización paso a paso del proceso

4. **Método de Runge-Kutta (RK4)**
   - Método de cuarto orden para ecuaciones diferenciales
   - Mayor precisión que el método de Euler
   - Muestra cálculo de k₁, k₂, k₃, k₄ en cada paso

### Interfaz de Usuario

- **Pantalla de Bienvenida**: Estilo calculadora científica retro
- **Menú Principal**: Selección visual de métodos numéricos
- **Ventanas Específicas**: Cada método tiene su propia interfaz optimizada
- **Resultados Detallados**: Visualización paso a paso de los cálculos
- **Navegación Intuitiva**: Fácil navegación entre pantallas

## Estructura del Proyecto

```
Monroy/
│
├── main.py                     # Archivo principal de la aplicación
├── requirements.txt            # Dependencias del proyecto
├── README.md                  # Documentación
│
├── gui/                       # Módulo de interfaz gráfica
│   ├── __init__.py
│   ├── main_window.py         # Ventana principal y navegación
│   ├── welcome_screen.py      # Pantalla de bienvenida
│   ├── methods_menu.py        # Menú de selección de métodos
│   ├── bisection_window.py    # Interfaz para método de bisección
│   ├── newton_raphson_window.py # Interfaz para Newton-Raphson
│   ├── euler_window.py        # Interfaz para método de Euler
│   └── runge_kutta_window.py  # Interfaz para Runge-Kutta
│
└── numerical_methods/         # Módulo de métodos numéricos
    ├── __init__.py
    └── methods.py             # Implementaciones matemáticas
```

## Instalación y Uso

### Requisitos

- Python 3.7 o superior
- Tkinter (incluido en la mayoría de instalaciones de Python)

### Ejecución

1. Clona o descarga el proyecto
2. Navega al directorio del proyecto
3. Ejecuta el archivo principal:

```bash
python main.py
```

### Uso de la Aplicación

1. **Inicio**: La aplicación muestra una pantalla de bienvenida con estilo retro
2. **Selección**: Haz clic en "INICIO" para acceder al menú principal
3. **Método**: Selecciona el método numérico que deseas utilizar
4. **Parámetros**: Ingresa los parámetros requeridos en los campos correspondientes
5. **Cálculo**: Haz clic en "CALCULAR" para ejecutar el método
6. **Resultados**: Revisa los resultados paso a paso en el área de resultados

## Ejemplos de Uso

### Método de Bisección
- **Función**: `x**2 - 4`
- **Intervalo**: [0, 3]
- **Tolerancia**: 0.000001
- **Resultado**: Encuentra la raíz x = 2

### Newton-Raphson
- **Función**: `x**2 - 4`
- **Derivada**: `2*x`
- **Valor inicial**: 3
- **Resultado**: Converge rápidamente a x = 2

### Método de Euler
- **Ecuación**: `dy/dx = x + y`
- **Condiciones iniciales**: x₀ = 0, y₀ = 1
- **Paso**: h = 0.1
- **Intervalo**: [0, 1]

### Runge-Kutta (RK4)
- **Ecuación**: `dy/dx = x + y`
- **Condiciones iniciales**: x₀ = 0, y₀ = 1
- **Paso**: h = 0.1
- **Intervalo**: [0, 1]

## Características Técnicas

### Arquitectura
- **Separación de responsabilidades**: Lógica matemática separada de la interfaz
- **Modularidad**: Cada método tiene su propia ventana y lógica
- **Extensibilidad**: Fácil agregar nuevos métodos numéricos

### Interfaz
- **Responsive**: Se adapta a diferentes tamaños de ventana
- **Intuitiva**: Navegación clara y botones descriptivos
- **Educativa**: Muestra pasos detallados y explicaciones

### Validación
- **Entrada de datos**: Validación básica de tipos de datos
- **Errores matemáticos**: Manejo de divisiones por cero y convergencia
- **Mensajes informativos**: Retroalimentación clara al usuario

## Futuras Mejoras

- [ ] Integración con matplotlib para gráficas
- [ ] Más métodos numéricos (Secante, Punto fijo, etc.)
- [ ] Exportación de resultados a archivos
- [ ] Validación avanzada de entrada
- [ ] Temas personalizables de interfaz
- [ ] Calculadora de derivadas automática

## Contribuciones

Este proyecto está diseñado con fines educativos. Las contribuciones son bienvenidas, especialmente:

- Nuevos métodos numéricos
- Mejoras en la interfaz de usuario
- Optimizaciones de rendimiento
- Documentación adicional
- Casos de prueba

## Licencia

Proyecto educativo de código abierto. Libre para uso académico y educativo.

## Contacto

Desarrollado como herramienta educativa para estudiantes de ingeniería.