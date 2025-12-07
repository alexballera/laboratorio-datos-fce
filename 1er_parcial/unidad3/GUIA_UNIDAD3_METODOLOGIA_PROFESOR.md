# GUÍA UNIDAD 3 - METODOLOGÍA EXACTA DEL PROFESOR

**📋 ESTA ES LA GUÍA DE REFERENCIA OBLIGATORIA**

Contiene SOLO los métodos enseñados por el profesor en las sesiones 9, 11 y 12 del curso.

---

## 📚 TEMAS DE UNIDAD 3

1. **Derivadas y Variaciones de Funciones** (Sesión 9)
2. **Elasticidad Precio de la Demanda** (Sesión 9)
3. **Optimización de Funciones - Monopolio** (Sesión 11)
4. **Optimización - Duopolio y Equilibrio de Nash** (Sesión 12)

---

## ✅ MÉTODOS PERMITIDOS EN UNIDAD 3

### 🔵 **TEMA 1: DERIVADAS SIMBÓLICAS CON SYMPY**

#### **Paso a Paso para Calcular Derivadas:**

**1. Importar librerías y definir variables simbólicas**
```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir variables simbólicas
x = sp.Symbol('x')
# O múltiples variables:
x, y, p, q = sp.symbols('x y p q')
```

**2. Definir funciones simbólicas**
```python
# Función simple
f = x**2 + 3*x - 5

# Función compleja
g = 15*x**6 - 8*x**4 + 27*x**3 - 5*x**2 + 11

# Función con raíces
h = x**(sp.Rational(1,2))  # √x (mejor que x**0.5)

# Función trigonométrica
t = 10*sp.sin(x) + 4*x**3
```

**3. Calcular derivadas**
```python
# Primera derivada
df_dx = sp.diff(f, x)

# Segunda derivada - MÉTODO 1
d2f_dx2 = sp.diff(f, x, 2)

# Segunda derivada - MÉTODO 2 (equivalente)
d2f_dx2 = sp.diff(df_dx, x)

# Tercera derivada
d3f_dx3 = sp.diff(f, x, 3)

# N-ésima derivada
dnf_dxn = sp.diff(f, x, n)  # donde n es un número
```

**4. Evaluar derivadas en un punto específico**
```python
# Evaluar en x = 6
valor_en_6 = df_dx.subs([(x, 6)]).evalf()

# Evaluar en múltiples puntos
punto_x = 2
punto_y = 3
valor = df_dx.subs([(x, punto_x), (y, punto_y)]).evalf()

# ALTERNATIVA sin evalf (devuelve expresión simbólica):
valor_simbolico = df_dx.subs(x, 6)
```

**5. Convertir función simbólica a función numérica (lambdify)**
```python
# Convertir para graficar o evaluar en rangos
f_numerica = sp.lambdify(x, f, 'numpy')
df_numerica = sp.lambdify(x, df_dx, 'numpy')

# Crear rango de valores
x_vals = np.linspace(-2, 2, 1000)

# Evaluar función en todo el rango
y_vals = f_numerica(x_vals)
dy_vals = df_numerica(x_vals)
```

**6. Graficar función y sus derivadas**
```python
plt.figure(figsize=(12, 8))

# Subplot 1: Función original
plt.subplot(2, 1, 1)
plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)')
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función Original')
plt.legend()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# Subplot 2: Derivada
plt.subplot(2, 1, 2)
plt.plot(x_vals, dy_vals, 'r-', linewidth=2, label="f'(x)")
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title('Derivada de la Función')
plt.legend()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()
```

---

### 🔵 **TEMA 2: OPTIMIZACIÓN DE FUNCIONES**

#### **Paso a Paso para Encontrar Máximos y Mínimos:**

**1. Encontrar puntos críticos (primera derivada = 0)**
```python
# Definir función
f = x**3 - 6*x**2 + 9*x + 15

# Primera derivada
df_dx = sp.diff(f, x)

# Resolver f'(x) = 0
puntos_criticos = sp.solve(df_dx, x)
print(f"Puntos críticos: {puntos_criticos}")
```

**2. Clasificar puntos críticos (segunda derivada)**
```python
# Calcular segunda derivada
d2f_dx2 = sp.diff(f, x, 2)

# Evaluar segunda derivada en cada punto crítico
for punto in puntos_criticos:
    segunda_derivada_valor = d2f_dx2.subs(x, punto).evalf()
    
    if segunda_derivada_valor > 0:
        tipo = "MÍNIMO local"
    elif segunda_derivada_valor < 0:
        tipo = "MÁXIMO local"
    else:
        tipo = "PUNTO DE INFLEXIÓN (indeterminado)"
    
    # Evaluar función en el punto
    f_valor = f.subs(x, punto).evalf()
    
    print(f"x = {punto}: f(x) = {f_valor:.4f} → {tipo}")
    print(f"  f''(x) = {segunda_derivada_valor:.4f}")
```

**3. Método numérico para encontrar óptimos (alternativa)**
```python
from scipy.optimize import fsolve

# Convertir a función numérica
df_numerica = sp.lambdify(x, df_dx, 'numpy')

# Buscar raíces de la derivada (puntos críticos)
x_inicial = [-5, 0, 5]  # Varios puntos de inicio
puntos_criticos_numericos = []

for xi in x_inicial:
    try:
        raiz = fsolve(df_numerica, xi)[0]
        if abs(df_numerica(raiz)) < 1e-6:
            puntos_criticos_numericos.append(raiz)
    except:
        continue

print(f"Puntos críticos (método numérico): {puntos_criticos_numericos}")
```

---

### 🔵 **TEMA 3: ELASTICIDAD PRECIO DE LA DEMANDA**

#### **Fórmulas de Elasticidad:**

**Elasticidad Precio Continua (con derivadas):**
```
ε = (dQd/dp) × (p/Qd)
```

**Elasticidad Precio Discreta (método del punto medio):**
```
ε = (ΔQ/Q_promedio) / (Δp/p_promedio)

donde:
Q_promedio = (Q1 + Q2) / 2
p_promedio = (p1 + p2) / 2
```

#### **Paso a Paso para Calcular Elasticidad Continua:**

**1. Definir función de demanda**
```python
# Variable simbólica
p = sp.Symbol('p')

# Función de demanda: Qd(p)
Qd = 180 - p**2 - 3*p

print(f"Función de demanda: Qd(p) = {Qd}")
```

**2. Calcular derivada de la demanda**
```python
# dQd/dp
dQd_dp = sp.diff(Qd, p)
print(f"Derivada: dQd/dp = {dQd_dp}")
```

**3. Definir fórmula de elasticidad**
```python
# Elasticidad: ε = (dQd/dp) × (p/Qd)
elasticidad = (dQd_dp * p) / Qd

# Simplificar
elasticidad_simplificada = sp.simplify(elasticidad)
print(f"Elasticidad: ε = {elasticidad_simplificada}")
```

**4. Evaluar elasticidad en precios específicos**
```python
# Función numérica para facilitar cálculos
def calcular_elasticidad(precio):
    cantidad = float(Qd.subs(p, precio))
    if cantidad <= 0:
        return float('inf')
    derivada = float(dQd_dp.subs(p, precio))
    return (derivada * precio) / cantidad

# Evaluar en varios precios
precios = [1, 5, 10]
for precio in precios:
    elasticidad_val = calcular_elasticidad(precio)
    cantidad = float(Qd.subs(p, precio))
    
    # Clasificar tipo de elasticidad
    if abs(elasticidad_val) > 1:
        tipo = "Elástica"
    elif abs(elasticidad_val) == 1:
        tipo = "Unitaria"
    else:
        tipo = "Inelástica"
    
    print(f"p = ${precio}: Qd = {cantidad:.1f}, ε = {elasticidad_val:.3f} ({tipo})")
```

**5. Interpretar resultados**
```python
# Interpretación de elasticidad
def interpretar_elasticidad(epsilon):
    if epsilon > 0:
        return "⚠️ ANOMALÍA: Bien Giffen o Veblen (precio sube, demanda sube)"
    elif epsilon < -1:
        return "Demanda ELÁSTICA: Sensible al precio (precio sube 1%, demanda baja más de 1%)"
    elif epsilon == -1:
        return "Demanda UNITARIA: Cambio proporcional (precio sube 1%, demanda baja 1%)"
    else:  # -1 < epsilon < 0
        return "Demanda INELÁSTICA: Poco sensible al precio (precio sube 1%, demanda baja menos de 1%)"
```

#### **Paso a Paso para Calcular Elasticidad Discreta:**

```python
# Dos puntos de observación
p1, p2 = 4, 6
Q1 = float(Qd.subs(p, p1))
Q2 = float(Qd.subs(p, p2))

# Método del punto medio
delta_Q = Q2 - Q1
delta_p = p2 - p1
Q_promedio = (Q1 + Q2) / 2
p_promedio = (p1 + p2) / 2

# Elasticidad discreta
elasticidad_discreta = (delta_Q / Q_promedio) / (delta_p / p_promedio)

print(f"Elasticidad discreta entre p=${p1} y p=${p2}: {elasticidad_discreta:.3f}")

# Comparar con elasticidad continua en el punto medio
elasticidad_continua = calcular_elasticidad(p_promedio)
print(f"Elasticidad continua en p=${p_promedio}: {elasticidad_continua:.3f}")
```

---

### 🔵 **TEMA 4: OPTIMIZACIÓN EN MONOPOLIO**

#### **Paso a Paso para Maximizar Beneficio de Monopolio:**

**1. Definir funciones del monopolio**
```python
# Variables simbólicas
q = sp.Symbol('q', positive=True)  # Cantidad (siempre positiva)
p = sp.Symbol('p', positive=True)  # Precio

# Función de demanda inversa: p(q)
p_demanda = 500 - 2*q - 0.5*q**2

# Función de costo total: C(q)
C = 100 + 2*q

print(f"Demanda inversa: p(q) = {p_demanda}")
print(f"Costo total: C(q) = {C}")
```

**2. Definir ingreso total y beneficio**
```python
# Ingreso Total: IT = p × q
IT = p_demanda * q

# Beneficio (Π): Π = IT - CT
beneficio = IT - C

print(f"Ingreso Total: IT = {sp.expand(IT)}")
print(f"Beneficio: Π = {sp.expand(beneficio)}")
```

**3. Encontrar condición de primer orden (CPO)**
```python
# Derivada del beneficio respecto a q
d_beneficio_dq = sp.diff(beneficio, q)

print(f"Condición de primer orden:")
print(f"dΠ/dq = {d_beneficio_dq}")

# Igualar a cero y resolver
q_optimo_simbolico = sp.solve(d_beneficio_dq, q)
print(f"Cantidad óptima: q* = {q_optimo_simbolico}")
```

**4. Verificar condición de segundo orden (CSO)**
```python
# Segunda derivada del beneficio
d2_beneficio_dq2 = sp.diff(beneficio, q, 2)

print(f"Condición de segundo orden:")
print(f"d²Π/dq² = {d2_beneficio_dq2}")

# Evaluar en el punto óptimo
for q_opt in q_optimo_simbolico:
    if q_opt.is_real and q_opt > 0:
        cso_valor = d2_beneficio_dq2.subs(q, q_opt)
        
        if cso_valor < 0:
            print(f"✓ q* = {q_opt} es un MÁXIMO (CSO < 0)")
            q_final = q_opt
        elif cso_valor > 0:
            print(f"✗ q* = {q_opt} es un MÍNIMO (CSO > 0)")
        else:
            print(f"? q* = {q_opt} indeterminado (CSO = 0)")
```

**5. Calcular resultados en el óptimo**
```python
# Evaluar todas las variables en el óptimo
q_optimo = float(q_final)
p_optimo = float(p_demanda.subs(q, q_final))
IT_optimo = float(IT.subs(q, q_final))
C_optimo = float(C.subs(q, q_final))
beneficio_optimo = float(beneficio.subs(q, q_final))

print(f"\n📊 RESULTADOS ÓPTIMOS DEL MONOPOLIO:")
print(f"   Cantidad: q* = {q_optimo:.2f} unidades")
print(f"   Precio: p* = ${p_optimo:.2f}")
print(f"   Ingreso Total: IT* = ${IT_optimo:.2f}")
print(f"   Costo Total: C* = ${C_optimo:.2f}")
print(f"   Beneficio: Π* = ${beneficio_optimo:.2f}")
```

**6. Calcular Ingreso Marginal y Costo Marginal**
```python
# Ingreso Marginal
IM = sp.diff(IT, q)
IM_optimo = IM.subs(q, q_final)

# Costo Marginal
CM = sp.diff(C, q)
CM_optimo = CM.subs(q, q_final)

print(f"\nVerificación de equilibrio:")
print(f"   Ingreso Marginal: IM = {IM_optimo:.2f}")
print(f"   Costo Marginal: CM = {CM_optimo:.2f}")
print(f"   ¿IM = CM? {abs(float(IM_optimo - CM_optimo)) < 0.01}")
```

**7. Visualización gráfica**
```python
# Crear funciones numéricas
IT_func = sp.lambdify(q, IT, 'numpy')
C_func = sp.lambdify(q, C, 'numpy')
beneficio_func = sp.lambdify(q, beneficio, 'numpy')

# Rango de cantidades
q_vals = np.linspace(0, 200, 500)

plt.figure(figsize=(12, 8))

# Subplot 1: IT, CT, Beneficio
plt.subplot(2, 1, 1)
plt.plot(q_vals, IT_func(q_vals), 'b-', linewidth=2, label='Ingreso Total (IT)')
plt.plot(q_vals, C_func(q_vals), 'r-', linewidth=2, label='Costo Total (CT)')
plt.plot(q_vals, beneficio_func(q_vals), 'g-', linewidth=2, label='Beneficio (Π)')
plt.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
plt.axvline(x=q_optimo, color='orange', linewidth=2, linestyle='--', label=f'q* = {q_optimo:.1f}')
plt.plot(q_optimo, beneficio_optimo, 'ro', markersize=10, label=f'Π* = {beneficio_optimo:.2f}')
plt.xlabel('Cantidad (q)')
plt.ylabel('Valor ($)')
plt.title('Maximización de Beneficio del Monopolio')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 2: IM y CM
IM_func = sp.lambdify(q, IM, 'numpy')
CM_func = sp.lambdify(q, CM, 'numpy')

plt.subplot(2, 1, 2)
plt.plot(q_vals, IM_func(q_vals), 'b-', linewidth=2, label='Ingreso Marginal (IM)')
plt.plot(q_vals, CM_func(q_vals), 'r-', linewidth=2, label='Costo Marginal (CM)')
plt.axvline(x=q_optimo, color='orange', linewidth=2, linestyle='--', label=f'q* = {q_optimo:.1f}')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.xlabel('Cantidad (q)')
plt.ylabel('Costo/Ingreso Marginal ($)')
plt.title('Condición de Equilibrio: IM = CM')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

### 🔵 **TEMA 5: DERIVADAS PARCIALES**

**Para funciones de dos o más variables:**

```python
# Definir variables
x, y = sp.symbols('x y')

# Función de producción
q = x**(sp.Rational(1,2)) * y**(sp.Rational(1,2))

# Derivadas parciales
dq_dx = sp.diff(q, x)  # Derivada respecto a x
dq_dy = sp.diff(q, y)  # Derivada respecto a y

# Evaluar en un punto
punto = (2, 2)
dq_dx_punto = dq_dx.subs([(x, punto[0]), (y, punto[1])])
dq_dy_punto = dq_dy.subs([(x, punto[0]), (y, punto[1])])

print(f"∂q/∂x en {punto} = {dq_dx_punto}")
print(f"∂q/∂y en {punto} = {dq_dy_punto}")
```

---

## ❌ MÉTODOS PROHIBIDOS EN UNIDAD 3

**NO usar estos métodos en ejercicios básicos:**
- Métodos de optimización numérica complejos de `scipy.optimize` más allá de `fsolve`
- Derivadas numéricas con `np.gradient()` (usar sympy)
- Métodos de diferenciación automática (autograd, JAX)
- Resolución de sistemas no lineales complejos
- Cálculo variacional o control óptimo

---

## 🎯 ESTRUCTURA DE RESOLUCIÓN PARA EXAMEN

### **EJERCICIO TIPO: OPTIMIZACIÓN DE MONOPOLIO**

**Consigna:** Una empresa enfrenta demanda inversa p(q) = 500 - 0.5q y costo C(q) = 300 + 8q. Hallar cantidad que maximiza beneficio.

**Resolución paso a paso:**

```python
import sympy as sp

# 1. Definir variables y funciones
q = sp.Symbol('q', positive=True)
p = 500 - 0.5*q
C = 300 + 8*q

# 2. Definir ingreso y beneficio
IT = p * q
beneficio = IT - C

print("Ingreso Total:", sp.expand(IT))
print("Beneficio:", sp.expand(beneficio))

# 3. Condición de primer orden
d_beneficio = sp.diff(beneficio, q)
q_optimo = sp.solve(d_beneficio, q)

print(f"CPO: dΠ/dq = {d_beneficio} = 0")
print(f"Cantidad óptima: q* = {q_optimo}")

# 4. Verificar CSO
d2_beneficio = sp.diff(beneficio, q, 2)
cso_valor = d2_beneficio.subs(q, q_optimo[0])

print(f"CSO: d²Π/dq² = {d2_beneficio}")
print(f"En q*: {cso_valor}")

if cso_valor < 0:
    print("✓ Es un máximo")
    
# 5. Resultados finales
q_opt = float(q_optimo[0])
p_opt = float(p.subs(q, q_opt))
beneficio_opt = float(beneficio.subs(q, q_opt))

print(f"\nRespuesta:")
print(f"q* = {q_opt:.2f} unidades")
print(f"p* = ${p_opt:.2f}")
print(f"Π* = ${beneficio_opt:.2f}")
```

---

### **EJERCICIO TIPO: ELASTICIDAD**

**Consigna:** Calcular elasticidad precio de demanda Qd = 180 - p² - 3p para p = 5.

**Resolución paso a paso:**

```python
import sympy as sp

# 1. Definir función de demanda
p = sp.Symbol('p')
Qd = 180 - p**2 - 3*p

# 2. Calcular derivada
dQd_dp = sp.diff(Qd, p)
print(f"dQd/dp = {dQd_dp}")

# 3. Fórmula de elasticidad
elasticidad = (dQd_dp * p) / Qd
print(f"ε = {sp.simplify(elasticidad)}")

# 4. Evaluar en p = 5
precio = 5
cantidad = float(Qd.subs(p, precio))
epsilon = float(elasticidad.subs(p, precio))

print(f"\nPara p = ${precio}:")
print(f"Cantidad: {cantidad:.1f}")
print(f"Elasticidad: {epsilon:.3f}")

# 5. Clasificar
if abs(epsilon) > 1:
    tipo = "Elástica"
elif abs(epsilon) == 1:
    tipo = "Unitaria"
else:
    tipo = "Inelástica"

print(f"Tipo: {tipo}")
```

---

## 📊 INTERPRETACIÓN ECONÓMICA

### **Derivadas:**
- **Primera derivada**: Tasa de cambio, pendiente, crecimiento/decrecimiento
- **Segunda derivada**: Concavidad, aceleración del cambio
- **f'(x) = 0**: Punto crítico (posible máximo/mínimo)
- **f''(x) < 0**: Función cóncava (máximo)
- **f''(x) > 0**: Función convexa (mínimo)

### **Elasticidad:**
- **|ε| > 1**: Demanda elástica (sensible al precio)
- **|ε| = 1**: Demanda unitaria (proporcional)
- **|ε| < 1**: Demanda inelástica (poco sensible)
- **ε > 0**: Bien Giffen/Veblen (anómalo)
- **ε < 0**: Comportamiento normal

### **Monopolio:**
- **IM = CM**: Condición de maximización
- **IM > CM**: Producir más aumenta beneficio
- **IM < CM**: Producir menos aumenta beneficio
- **Poder de mercado**: Precio > Costo Marginal

---

## ⚠️ ERRORES COMUNES A EVITAR

1. **Confundir demanda directa con inversa**
   - Directa: Q(p) - cantidad en función de precio
   - Inversa: p(Q) - precio en función de cantidad
   - Para monopolio necesitamos INVERSA

2. **Olvidar usar sp.Rational para fracciones**
   ```python
   # ❌ INCORRECTO:
   q = x**0.5
   
   # ✅ CORRECTO:
   q = x**(sp.Rational(1,2))
   ```

3. **No verificar condición de segundo orden**
   - Siempre calcular f''(x) para confirmar máximo/mínimo

4. **Confundir signo de elasticidad**
   - Elasticidad es NEGATIVA para bienes normales
   - Reportar en valor absoluto: |ε| = 1.5

5. **No usar .evalf() al evaluar**
   ```python
   # ❌ Da resultado simbólico:
   resultado = f.subs(x, 5)
   
   # ✅ Da resultado numérico:
   resultado = f.subs(x, 5).evalf()
   ```

---

## 🎓 CONSEJOS PARA EL EXAMEN

1. **Define todas las variables simbólicas** al inicio
2. **Usa nombres descriptivos**: `beneficio`, `elasticidad`, no `y`, `e`
3. **Muestra el desarrollo**: CPO, CSO, sustitución
4. **Verifica resultados**: ¿tiene sentido económico?
5. **Incluye interpretación económica** siempre
6. **Grafica cuando sea posible** para validar visualmente
7. **Usa sp.simplify()** para expresiones complejas
8. **Reporta con decimales apropiados**: .2f para dinero, .3f para elasticidad
9. **Verifica signos**: ¿beneficio positivo? ¿elasticidad negativa?
10. **Comenta tu código** para mostrar comprensión

---

**📌 ESTA ES LA ÚNICA METODOLOGÍA ACEPTADA POR EL PROFESOR**

Si usas métodos no enseñados, perderás puntos aunque la respuesta sea correcta.
