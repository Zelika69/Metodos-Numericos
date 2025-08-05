# 📚 GUÍA COMPLETA DE USO - SOLUCIONADOR DE MÉTODOS NUMÉRICOS

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar la Aplicación
```bash
python main.py
```

## 📖 Guía de Entrada de Funciones

### 🔢 Sintaxis General
Todas las funciones deben escribirse usando la sintaxis de Python:

| Operación | Símbolo | Ejemplo |
|-----------|---------|----------|
| Suma | `+` | `x + 3` |
| Resta | `-` | `x - 2` |
| Multiplicación | `*` | `2*x` o `3*x**2` |
| División | `/` | `x/2` |
| Potencia | `**` | `x**2`, `x**3` |
| Raíz cuadrada | `sqrt(x)` | `sqrt(x)` |
| Exponencial | `exp(x)` | `exp(x)` |
| Logaritmo natural | `log(x)` | `log(x)` |
| Seno | `sin(x)` | `sin(x)` |
| Coseno | `cos(x)` | `cos(x)` |
| Tangente | `tan(x)` | `tan(x)` |

### ✅ Ejemplos de Funciones Válidas

#### Polinomios
- `x**2 - 4` (parábola)
- `x**3 - 2*x - 5` (cúbica)
- `2*x**2 + 3*x - 1` (cuadrática)
- `x**4 - x**2 + 1` (cuártica)

#### Funciones Trigonométricas
- `sin(x) - 0.5`
- `cos(x) + x`
- `tan(x) - x`

#### Funciones Exponenciales y Logarítmicas
- `exp(x) - 2`
- `log(x) - 1`
- `x*exp(-x)`

#### Funciones Mixtas
- `x**2 + sin(x)`
- `exp(x) - x**2`
- `log(x) + x**2 - 3`

### ❌ Errores Comunes a Evitar

| ❌ Incorrecto | ✅ Correcto | Explicación |
|---------------|-------------|-------------|
| `2x` | `2*x` | Siempre usar `*` para multiplicación |
| `x^2` | `x**2` | Usar `**` para potencias |
| `ln(x)` | `log(x)` | En Python, `log()` es logaritmo natural |
| `√x` | `sqrt(x)` | Usar función `sqrt()` |
| `e^x` | `exp(x)` | Usar función `exp()` |

## 🎯 MÉTODOS NUMÉRICOS - GUÍA ESPECÍFICA

### 1. 🔍 MÉTODO DE BISECCIÓN

**Propósito:** Encontrar raíces de ecuaciones f(x) = 0

#### Parámetros de Entrada:
- **Función f(x):** La ecuación cuya raíz buscas
- **Intervalo [a, b]:** Valores donde f(a) y f(b) tienen signos opuestos
- **Tolerancia:** Precisión deseada (ej: 0.001)
- **Iteraciones máximas:** Límite de cálculos (ej: 100)

#### Ejemplo Práctico:
```
Función: x**2 - 4
Intervalo: a = 1, b = 3
Tolerancia: 0.001
```
**Resultado:** Encuentra x ≈ 2 (raíz de x² - 4 = 0)

#### Consejos:
- Verifica que f(a) y f(b) tengan signos diferentes
- Usa gráficas para visualizar el comportamiento
- Tolerancia típica: 0.001 a 0.0001

### 2. 🎯 MÉTODO DE NEWTON-RAPHSON

**Propósito:** Encontrar raíces usando derivadas (convergencia rápida)

#### Parámetros de Entrada:
- **Función f(x):** La ecuación cuya raíz buscas
- **Derivada f'(x):** Se calcula automáticamente o puedes ingresarla manualmente
- **Valor inicial x₀:** Punto de partida cerca de la raíz
- **Tolerancia:** Precisión deseada
- **Iteraciones máximas:** Límite de cálculos

#### Cálculo Automático de Derivadas:
1. Ingresa tu función
2. Haz clic en el botón **"Auto"** junto al campo de derivada
3. La derivada se calculará automáticamente

#### Ejemplos de Derivadas Automáticas:
| Función | Derivada Automática |
|---------|--------------------|
| `x**2` | `2*x` |
| `x**3 - x` | `3*x**2 - 1` |
| `2*x**2 + 3*x` | `4*x + 3` |
| `sin(x)` | `cos(x)` |
| `exp(x)` | `exp(x)` |

#### Ejemplo Práctico:
```
Función: x**2 - 4
Derivada: 2*x (automática)
Valor inicial: x₀ = 1.5
Tolerancia: 0.001
```

#### Consejos:
- Elige x₀ cerca de la raíz esperada
- Si no converge, prueba otro valor inicial
- Usa la gráfica para elegir mejor x₀

### 3. 📈 MÉTODO DE EULER

**Propósito:** Resolver ecuaciones diferenciales dy/dx = f(x,y)

#### Parámetros de Entrada:
- **Función f(x,y):** Lado derecho de la ecuación diferencial
- **Valor inicial x₀:** Punto de partida en x
- **Valor inicial y₀:** Valor de y en x₀
- **Tamaño de paso h:** Incremento en x (más pequeño = más preciso)
- **Valor final de x:** Hasta dónde calcular

#### Ejemplos de Funciones f(x,y):
| Ecuación Diferencial | Función f(x,y) |
|---------------------|----------------|
| dy/dx = y | `y` |
| dy/dx = x + y | `x + y` |
| dy/dx = x² + y² | `x**2 + y**2` |
| dy/dx = -y + x | `-y + x` |
| dy/dx = sin(x) + y | `sin(x) + y` |

#### Ejemplo Práctico:
```
Función: y
Valor inicial x₀: 0
Valor inicial y₀: 1
Tamaño de paso h: 0.1
Valor final de x: 2
```
**Resultado:** Aproxima la solución de dy/dx = y con y(0) = 1

#### Consejos:
- Paso más pequeño (h) = mayor precisión
- h típico: 0.01 a 0.1
- Usa gráficas para visualizar la solución

### 4. 🎯 MÉTODO DE RUNGE-KUTTA (RK4)

**Propósito:** Resolver ecuaciones diferenciales con mayor precisión que Euler

#### Parámetros de Entrada:
- **Función f(x,y):** Lado derecho de la ecuación diferencial
- **Valor inicial x₀:** Punto de partida en x
- **Valor inicial y₀:** Valor de y en x₀
- **Tamaño de paso h:** Incremento en x
- **Valor final de x:** Hasta dónde calcular

#### Ejemplo Práctico:
```
Función: -y + x
Valor inicial x₀: 0
Valor inicial y₀: 1
Tamaño de paso h: 0.2
Valor final de x: 2
```

#### Ventajas sobre Euler:
- Mayor precisión con el mismo paso
- Mejor estabilidad numérica
- Permite pasos más grandes

## 📊 USO DE GRÁFICAS

### Activar Gráficas
1. Realiza un cálculo con cualquier método
2. Haz clic en el botón **"GRÁFICA"**
3. Se abrirá una ventana con la visualización

### Tipos de Gráficas:

#### Bisección y Newton-Raphson:
- Muestra la función y las iteraciones
- Visualiza la convergencia hacia la raíz
- Ayuda a entender el comportamiento del método

#### Euler y Runge-Kutta:
- Muestra la curva solución
- Marca puntos inicial y final
- Permite comparar diferentes métodos

### Requisitos para Gráficas:
- Matplotlib debe estar instalado
- Si no está disponible, aparecerá un mensaje de error

## 🛠️ SOLUCIÓN DE PROBLEMAS

### Errores Comunes y Soluciones:

#### "Error de sintaxis en la función"
- **Causa:** Función mal escrita
- **Solución:** Revisa la sintaxis (usar `*` para multiplicar, `**` para potencias)

#### "La función no cambia de signo en el intervalo"
- **Causa:** En bisección, f(a) y f(b) tienen el mismo signo
- **Solución:** Cambia el intervalo [a,b]

#### "El método no converge"
- **Causa:** Valor inicial inadecuado o función problemática
- **Solución:** Cambia el valor inicial o verifica la función

#### "Matplotlib no disponible"
- **Causa:** Biblioteca no instalada
- **Solución:** Ejecuta `pip install matplotlib`

#### "División por cero"
- **Causa:** Derivada cero en Newton-Raphson
- **Solución:** Cambia el valor inicial

### Consejos Generales:
1. **Siempre verifica tu función** antes de calcular
2. **Usa valores iniciales razonables**
3. **Ajusta la tolerancia** según la precisión necesaria
4. **Experimenta con diferentes parámetros**
5. **Usa las gráficas** para entender mejor los resultados

## 📝 EJEMPLOS COMPLETOS

### Ejemplo 1: Encontrar √2
**Método:** Bisección
```
Función: x**2 - 2
Intervalo: a = 1, b = 2
Tolerancia: 0.001
```
**Resultado:** x ≈ 1.414

### Ejemplo 2: Resolver dy/dx = -y, y(0) = 1
**Método:** Runge-Kutta
```
Función: -y
x₀ = 0, y₀ = 1
h = 0.1, x_final = 2
```
**Resultado:** Aproxima y = e^(-x)

### Ejemplo 3: Raíz de ecuación cúbica
**Método:** Newton-Raphson
```
Función: x**3 - 2*x - 5
Derivada: 3*x**2 - 2 (automática)
x₀ = 2
Tolerancia: 0.0001
```

¡Experimenta con diferentes funciones y parámetros para dominar cada método! 🎓