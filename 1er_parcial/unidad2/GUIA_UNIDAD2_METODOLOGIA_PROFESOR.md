# GUÍA UNIDAD 2 - METODOLOGÍA EXACTA DEL PROFESOR

**📋 ESTA ES LA GUÍA DE REFERENCIA OBLIGATORIA**

Contiene SOLO los métodos enseñados por el profesor en las sesiones 5, 6 y 7 del curso.

---

## 📚 TEMAS DE UNIDAD 2

1. **Matrices y Modelo Insumo-Producto de Leontief** (Sesión 5)
2. **Manipulación de Datos Estructurados y Leontief** (Sesión 6)
3. **Programación Lineal en Python** (Sesión 7)

---

## ✅ MÉTODOS PERMITIDOS EN UNIDAD 2

### 🔵 **TEMA 1: MODELO INSUMO-PRODUCTO DE LEONTIEF**

#### **Paso a Paso del Modelo de Leontief:**

**1. Crear la matriz de flujos intermedios (matriz sectorial)**
```python
# Matriz Z: flujos entre sectores (en millones de moneda)
matriz_sectorial = np.array([
    [90, 20, 80],     # Sector 1 vende a: Sector1, Sector2, Sector3
    [200, 500, 400],  # Sector 2 vende a: Sector1, Sector2, Sector3
    [180, 280, 1000]  # Sector 3 vende a: Sector1, Sector2, Sector3
])
```

**2. Definir vectores de demanda final y valor agregado**
```python
demanda_final = np.array([580, 300, 1000])  # Vector H
valor_agregado = np.array([300, 600, 980])  # Vector V.A.
```

**3. Calcular el producto total (X) - MÉTODO 1: Por filas**
```python
# X_i = suma de flujos intermedios + demanda final
# X_i = Σ(Z_ij) + H_i
producto_total = matriz_sectorial.sum(axis=1) + demanda_final
```

**4. Calcular el producto total (X) - MÉTODO 2: Por columnas (verificación)**
```python
# X_j = suma de flujos intermedios + valor agregado
# X_j = Σ(Z_ij) + V.A._j
verificacion_X = matriz_sectorial.sum(axis=0) + valor_agregado
```

**5. Calcular la matriz de coeficientes técnicos (A)**
```python
# Coeficiente técnico: a_ij = Z_ij / X_j
# Cuánto del sector i necesita el sector j para producir 1 unidad
coeficientes_tecnicos = matriz_sectorial / producto_total.reshape(1, -1)

# ALTERNATIVA usando broadcasting:
coeficientes_tecnicos = matriz_sectorial / producto_total
```

**6. Crear DataFrame para visualizar la tabla completa**
```python
sectores = ['Sector1', 'Sector2', 'Sector3']

# DataFrame con matriz sectorial
df_insumo_producto = pd.DataFrame(
    matriz_sectorial, 
    index=sectores,
    columns=sectores
)

# Agregar columnas de demanda final y producto total
df_insumo_producto['Demanda Final (H)'] = demanda_final
df_insumo_producto['Producto Total (X)'] = producto_total

# Agregar filas de valor agregado y producto total
df_insumo_producto.loc['Valor Agregado (V.A.)'] = list(valor_agregado) + [np.nan, np.nan]
df_insumo_producto.loc['Producto Total (X)'] = list(verificacion_X) + [np.nan, np.nan]
```

**7. Aplicar el modelo de Leontief: X = (I - A)^(-1) × H**
```python
# Paso 1: Crear matriz identidad
matriz_identidad = np.eye(3)  # Matriz identidad de 3x3

# Paso 2: Calcular (I - A)
matriz_I_menos_A = matriz_identidad - coeficientes_tecnicos

# Paso 3: Calcular la inversa de Leontief (I - A)^(-1)
matriz_leontief = np.linalg.inv(matriz_I_menos_A)

# Paso 4: Calcular producción total: X = (I - A)^(-1) × H
producto_total_leontief = matriz_leontief @ demanda_final
# ALTERNATIVA: producto_total_leontief = np.dot(matriz_leontief, demanda_final)
```

**8. Análisis de cambios en demanda final**
```python
# Calcular nueva demanda con cambios porcentuales
demanda_final_nueva = demanda_final * np.array([0.95, 0.60, 0.10])  # Reducciones

# Aplicar modelo de Leontief con nueva demanda
producto_total_nuevo = matriz_leontief @ demanda_final_nueva

# Calcular cambios
cambio_absoluto = producto_total_nuevo - producto_total
cambio_porcentual = (cambio_absoluto / producto_total) * 100
```

**9. Cálculo del nuevo valor agregado**
```python
# V.A. = X - Σ(insumos intermedios que compra cada sector)
# V.A._j = X_j - Σ_i(Z_ij)

# Los insumos que compra cada sector son las columnas de la matriz sectorial
# Con coeficientes técnicos: suma(a_ij) × X_j
insumos_intermedios_nuevos = coeficientes_tecnicos.T @ producto_total_nuevo

valor_agregado_nuevo = producto_total_nuevo - insumos_intermedios_nuevos
```

**10. Verificación de dimensiones y validez del modelo**
```python
# Verificar compatibilidad de dimensiones
print(f"Matriz A: {coeficientes_tecnicos.shape}")
print(f"Vector H: {demanda_final.shape}")

# Calcular determinante de (I - A)
determinante = np.linalg.det(matriz_I_menos_A)
print(f"Determinante de (I - A): {determinante:.4f}")
# Si det = 0, la matriz NO es invertible y el modelo NO funciona

# Calcular rango de (I - A)
rango = np.linalg.matrix_rank(matriz_I_menos_A)
print(f"Rango de (I - A): {rango}")

# Verificar la identidad fundamental: X - A×X = H
verificacion_identidad = producto_total - (coeficientes_tecnicos @ producto_total)
print(f"X - A×X = {verificacion_identidad}")
print(f"H = {demanda_final}")
# Deben ser iguales (con tolerancia numérica)
```

---

### 🔵 **TEMA 2: MANIPULACIÓN DE DATOS Y LEONTIEF**

**Métodos permitidos en Sesión 6:**

```python
# Lectura de datos
df = pd.read_csv('archivo.csv')

# Creación de DataFrame desde diccionario
df = pd.DataFrame({
    'columna1': [valores],
    'columna2': [valores]
})

# Conversión de fechas
df['fecha'] = pd.to_datetime(df['fecha'])

# Extracción de período mensual
df['periodo'] = df['fecha'].dt.to_period('M')

# Agrupación y suma (PERMITIDO en Sesión 6)
df_agrupado = df.groupby('categoria')['ventas'].sum()

# Aplicación de funciones personalizadas
df['nueva_columna'] = df.apply(lambda row: funcion(row['col1'], row['col2']), axis=1)

# Selección condicional
df_filtrado = df[df['columna'] > valor]

# Estadísticas básicas
df['columna'].mean()
df['columna'].sum()
df['columna'].min()
df['columna'].max()
```

---

### 🔵 **TEMA 3: PROGRAMACIÓN LINEAL**

#### **MÉTODO 1: SciPy linprog (básico)**

```python
from scipy.optimize import linprog

# ESTRUCTURA GENERAL:
# Minimizar: c^T × x
# Sujeto a: A_ub × x ≤ b_ub (restricciones de desigualdad)
#           A_eq × x = b_eq (restricciones de igualdad)
#           bounds: límites de variables

# Para MAXIMIZAR, convertimos a minimizar multiplicando por -1
```

**Ejemplo: Maximizar beneficio**
```python
# Función objetivo: MAXIMIZAR Z = 5x_A + 10x_C + 9x_H
# Convertimos a minimizar: -Z = -5x_A - 10x_C - 9x_H
c = np.array([-5, -10, -9])  # Coeficientes NEGATIVOS para maximizar

# Restricciones de desigualdad (≤)
# x_A + x_C + x_H ≤ 1200  (capacidad)
# 2x_A + 3x_C + 4x_H ≤ 1500  (presupuesto)
A_ub = np.array([
    [1, 1, 1],      # Restricción 1
    [2, 3, 4]       # Restricción 2
])
b_ub = np.array([1200, 1500])

# Límites de variables (no negatividad)
x_bounds = [(0, None), (0, None), (0, None)]  # x_A ≥ 0, x_C ≥ 0, x_H ≥ 0

# Resolver
resultado = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')

# Extraer resultados
if resultado.success:
    x_optimo = resultado.x  # Valores óptimos de las variables
    z_maximo = -resultado.fun  # Valor óptimo (negativo porque minimizamos -Z)
```

**Conversión de restricciones ≥ a ≤**
```python
# Si tenemos: x_A + x_C ≥ 50
# Convertimos a: -x_A - x_C ≤ -50
# Multiplicamos TODA la restricción por -1
```

---

#### **MÉTODO 2: PuLP (recomendado por el profesor)**

```python
import pulp

# PASO 1: Crear el problema
prob = pulp.LpProblem("Nombre_Problema", pulp.LpMaximize)
# Alternativas: pulp.LpMinimize

# PASO 2: Definir variables de decisión
x_A = pulp.LpVariable('x_A', lowBound=0)  # x_A ≥ 0
x_C = pulp.LpVariable('x_C', lowBound=0)  # x_C ≥ 0
x_H = pulp.LpVariable('x_H', lowBound=0)  # x_H ≥ 0

# Con límites superior e inferior
x = pulp.LpVariable('x', lowBound=4, upBound=100)  # 4 ≤ x ≤ 100

# PASO 3: Definir función objetivo
prob += 5*x_A + 10*x_C + 9*x_H, "Funcion_Objetivo"

# PASO 4: Agregar restricciones
prob += x_A + x_C + x_H <= 1200, "Capacidad_Almacenamiento"
prob += 2*x_A + 3*x_C + 4*x_H <= 1500, "Restriccion_Presupuesto"
prob += x_A >= 4, "Minimo_Acero"  # Restricción de mínimo

# PASO 5: Resolver el problema
# Opción 1: Con mensajes
prob.solve()

# Opción 2: Sin mensajes (recomendado para notebooks)
solver = pulp.PULP_CBC_CMD(msg=0)
prob.solve(solver)

# PASO 6: Verificar si se encontró solución
if prob.status == pulp.LpStatusOptimal:
    print("✅ Solución óptima encontrada")
    
    # Extraer valores de las variables
    x_A_optimo = pulp.value(x_A)
    x_C_optimo = pulp.value(x_C)
    x_H_optimo = pulp.value(x_H)
    
    # Extraer valor de la función objetivo
    z_optimo = pulp.value(prob.objective)
    
    print(f"x_A = {x_A_optimo:.2f}")
    print(f"x_C = {x_C_optimo:.2f}")
    print(f"x_H = {x_H_optimo:.2f}")
    print(f"Z máximo = {z_optimo:.2f}")
else:
    print("❌ No se encontró solución óptima")
```

**Restricciones relativas en PuLP:**
```python
# Si P ≥ 0.3 × L (P debe ser al menos 30% de L)
prob += P >= 0.3 * L, "Cota_Relativa_P"

# Si C ≥ 0.2 × L (C debe ser al menos 20% de L)
prob += C >= 0.2 * L, "Cota_Relativa_C"
```

**Problema de minimización de costos:**
```python
# Minimizar presupuesto
prob_min = pulp.LpProblem("Minimizar_Costos", pulp.LpMinimize)

# Variables
x_A = pulp.LpVariable('x_A', lowBound=4)  # Mínimo 4 toneladas
x_C = pulp.LpVariable('x_C', lowBound=2)  # Mínimo 2 toneladas
x_H = pulp.LpVariable('x_H', lowBound=8)  # Mínimo 8 toneladas

# Función objetivo: minimizar costos
prob_min += 3.8*x_A + 4.8*x_C + 6*x_H, "Costo_Total"

# Restricción de capacidad
prob_min += x_A + x_C + x_H <= 800, "Capacidad_Reducida"

# Resolver
solver = pulp.PULP_CBC_CMD(msg=0)
prob_min.solve(solver)
```

---

### 🔵 **VISUALIZACIONES EN UNIDAD 2**

**1. Gráfico comparativo de barras (antes vs después)**
```python
productos = ['Producto1', 'Producto2', 'Producto3']
x_pos = np.arange(len(productos))
ancho_barras = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

barras_antes = ax.bar(x_pos - ancho_barras/2, valores_antes, ancho_barras, 
                     label='Antes', color=['brown', 'gold', 'blue'], alpha=0.7)
barras_despues = ax.bar(x_pos + ancho_barras/2, valores_despues, ancho_barras, 
                       label='Después', color=['darkred', 'orange', 'navy'], alpha=0.7)

# Etiquetas con valores
for i, (antes, despues) in enumerate(zip(valores_antes, valores_despues)):
    ax.text(i - ancho_barras/2, antes + 10, f'{antes:.0f}', ha='center', va='bottom', fontweight='bold')
    ax.text(i + ancho_barras/2, despues + 10, f'{despues:.0f}', ha='center', va='bottom', fontweight='bold')

ax.set_title('Comparación Antes vs Después')
ax.set_xlabel('Productos')
ax.set_ylabel('Valores')
ax.set_xticks(x_pos)
ax.set_xticklabels(productos)
ax.legend()
ax.grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

**2. Gráfico de barras simple**
```python
productos = ['Acero', 'Cobre', 'Hierro']
cantidades = [100, 200, 150]
colores = ['gray', 'orange', 'brown']

plt.figure(figsize=(8, 5))
barras = plt.bar(productos, cantidades, color=colores, alpha=0.7)

# Etiquetas con valores
for i, valor in enumerate(cantidades):
    plt.text(i, valor + 5, f'{valor:.1f}\nton', ha='center', va='bottom', fontweight='bold')

plt.title('Producción Óptima por Producto')
plt.xlabel('Productos')
plt.ylabel('Cantidad (Toneladas)')
plt.grid(True, axis='y', alpha=0.3)
plt.ylim(0, max(cantidades) + 50)

plt.tight_layout()
plt.show()
```

**3. Gráfico de torta (distribución porcentual)**
```python
productos = ['Acero', 'Cobre', 'Hierro']
cantidades = [100, 200, 150]
colores = ['gray', 'orange', 'brown']

# Calcular porcentajes
total = sum(cantidades)
porcentajes = [(c/total)*100 for c in cantidades]

plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(porcentajes, 
                                  labels=productos,
                                  colors=colores,
                                  autopct='%1.1f%%',
                                  startangle=90,
                                  explode=[0.05, 0.05, 0.05])

plt.title('Distribución Porcentual de la Producción', fontsize=14)

# Mejorar formato del texto
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.axis('equal')  # Para que el círculo sea perfecto
plt.tight_layout()
plt.show()
```

**4. Región factible (programación lineal - 2D simplificado)**
```python
# Para visualizar, asumimos solo 2 variables (x1, x2)
x1_valores = np.linspace(0, 300, 100)

# Restricción 1: x1 + x2 ≤ 200
x2_restriccion1 = 200 - x1_valores

# Restricción 2: 2x1 + 3x2 ≤ 500
x2_restriccion2 = (500 - 2*x1_valores) / 3

plt.figure(figsize=(10, 7))

# Líneas de restricción
plt.plot(x1_valores, x2_restriccion1, 'b-', linewidth=2, label='x1 + x2 ≤ 200')
plt.plot(x1_valores, x2_restriccion2, 'r-', linewidth=2, label='2x1 + 3x2 ≤ 500')

# Región factible (sombreado)
x1_mesh, x2_mesh = np.meshgrid(np.linspace(0, 250, 200), np.linspace(0, 200, 200))
region_factible = ((x2_mesh <= 200 - x1_mesh) & 
                   (x2_mesh <= (500 - 2*x1_mesh) / 3) & 
                   (x1_mesh >= 0) & (x2_mesh >= 0))

plt.contourf(x1_mesh, x2_mesh, region_factible.astype(int), 
            levels=[0.5, 1.5], colors=['lightblue'], alpha=0.5)

# Punto óptimo
plt.plot(x1_optimo, x2_optimo, 'r*', markersize=15, label='Solución óptima')

plt.xlim(0, 250)
plt.ylim(0, 200)
plt.xlabel('x1', fontsize=12)
plt.ylabel('x2', fontsize=12)
plt.title('Espacio de Soluciones Factibles', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
```

---

## ❌ MÉTODOS PROHIBIDOS EN UNIDAD 2

**NO usar estos métodos en ejercicios básicos:**
- `.pivot()` o `.pivot_table()` (avanzado)
- `.merge()` o `.join()` (no enseñado aún)
- `.stack()` o `.unstack()` (transformaciones complejas)
- Métodos de optimización avanzados de scipy más allá de `linprog`
- `cvxpy` u otras librerías de optimización no enseñadas
- Álgebra lineal compleja más allá de `np.linalg.inv()`, `np.linalg.det()`, `np.linalg.matrix_rank()`

---

## 🎯 ESTRUCTURA DE RESOLUCIÓN PARA EXAMEN

### **EJERCICIO TIPO: MODELO INSUMO-PRODUCTO**

**Consigna:** Dada una matriz de coeficientes técnicos A y un vector de demanda final H, aplicar el modelo de Leontief.

**Resolución paso a paso:**

```python
# 1. Representar matriz A y vector H
A = np.array([
    [0.12, 0.41, 0.22],
    [0.27, 0.52, 0.86],
    [0.14, 0.22, 0.15]
])

H = np.array([40, 25, 35])

# 2. Verificar dimensiones
print(f"Matriz A: {A.shape}")
print(f"Vector H: {H.shape}")
print("✅ Dimensiones compatibles para el modelo de Leontief")

# 3. Aplicar modelo de Leontief
I = np.eye(3)
I_menos_A = I - A
matriz_leontief = np.linalg.inv(I_menos_A)
X = matriz_leontief @ H

print(f"Vector de producción total X: {X}")

# 4. Validación del modelo
det = np.linalg.det(I_menos_A)
rango = np.linalg.matrix_rank(I_menos_A)

print(f"Determinante de (I-A): {det:.4f}")
print(f"Rango de (I-A): {rango}")

if det != 0:
    print("✅ El modelo es viable (determinante ≠ 0)")

# 5. Verificar identidad X - A×X = H
verificacion = X - (A @ X)
print(f"X - A×X = {verificacion.round(2)}")
print(f"H = {H}")
```

---

### **EJERCICIO TIPO: PROGRAMACIÓN LINEAL CON PULP**

**Consigna:** Maximizar Z = P + L + C sujeto a 7P + 5L + 6C ≤ 1500, P,L,C ≥ 0.

**Resolución paso a paso:**

```python
import pulp

# 1. Crear el problema
prob = pulp.LpProblem("Maximizar_Produccion", pulp.LpMaximize)

# 2. Definir variables
P = pulp.LpVariable('P', lowBound=0)
L = pulp.LpVariable('L', lowBound=0)
C = pulp.LpVariable('C', lowBound=0)

# 3. Función objetivo
prob += P + L + C, "Produccion_Total"

# 4. Restricciones
prob += 7*P + 5*L + 6*C <= 1500, "Restriccion_Presupuesto"

# 5. Resolver
solver = pulp.PULP_CBC_CMD(msg=0)
prob.solve(solver)

# 6. Resultados
if prob.status == pulp.LpStatusOptimal:
    print("✅ Solución óptima encontrada:")
    print(f"P = {pulp.value(P):.2f}")
    print(f"L = {pulp.value(L):.2f}")
    print(f"C = {pulp.value(C):.2f}")
    print(f"Z máximo = {pulp.value(prob.objective):.2f}")
    
    # Verificar restricción
    presupuesto_usado = 7*pulp.value(P) + 5*pulp.value(L) + 6*pulp.value(C)
    print(f"\nPresupuesto usado: ${presupuesto_usado:.2f} / $1500")
else:
    print("❌ No se encontró solución")
```

---

## 📊 INTERPRETACIÓN ECONÓMICA

### **Modelo de Leontief:**
- **Coeficiente técnico a_ij**: Cantidad de insumo del sector i que necesita el sector j para producir 1 unidad
- **Matriz inversa de Leontief (I-A)^(-1)**: Muestra los efectos directos e indirectos en toda la economía ante cambios en demanda final
- **Identidad X - A×X = H**: El producto total menos lo que se consume internamente es igual a la demanda final
- **Si det(I-A) = 0**: El sistema NO tiene solución única, el modelo NO es viable

### **Programación Lineal:**
- **Función objetivo**: Lo que queremos maximizar o minimizar
- **Restricciones**: Limitaciones de recursos o condiciones que deben cumplirse
- **Región factible**: Conjunto de todas las combinaciones que cumplen las restricciones
- **Solución óptima**: El punto de la región factible que maximiza/minimiza la función objetivo
- **Recursos activos**: Restricciones que se cumplen con igualdad en la solución óptima (se usa todo el recurso)

---

## ⚠️ ERRORES COMUNES A EVITAR

1. **Confundir matriz sectorial (Z) con matriz de coeficientes (A)**
   - Z = flujos absolutos entre sectores
   - A = coeficientes técnicos (Z / X)

2. **Olvidar reshape al dividir para calcular coeficientes técnicos**
   ```python
   # ❌ INCORRECTO:
   A = matriz_sectorial / producto_total
   
   # ✅ CORRECTO:
   A = matriz_sectorial / producto_total.reshape(1, -1)
   ```

3. **No convertir maximización a minimización en linprog**
   ```python
   # Para MAXIMIZAR Z = 5x + 10y
   # ❌ INCORRECTO:
   c = [5, 10]
   
   # ✅ CORRECTO:
   c = [-5, -10]  # Negativo para maximizar
   z_maximo = -resultado.fun  # Negativo para obtener el máximo
   ```

4. **Usar método='simplex' en lugar de method='highs'**
   ```python
   # ❌ DESACTUALIZADO:
   resultado = linprog(c, A_ub, b_ub, method='simplex')
   
   # ✅ ACTUAL:
   resultado = linprog(c, A_ub, b_ub, method='highs')
   ```

5. **Olvidar verificar resultado.success o prob.status**
   ```python
   # ✅ SIEMPRE verificar:
   if resultado.success:  # Para linprog
       # procesar resultados
   
   if prob.status == pulp.LpStatusOptimal:  # Para PuLP
       # procesar resultados
   ```

---

## 🎓 CONSEJOS PARA EL EXAMEN

1. **Lee TODO el enunciado antes de empezar a programar**
2. **Identifica qué tipo de ejercicio es** (Leontief, PuLP, manipulación de datos)
3. **Sigue el orden exacto de pasos** mostrado en esta guía
4. **Usa nombres de variables descriptivos** (demanda_final, producto_total, no x, y)
5. **Comenta tu código** para mostrar que entiendes qué estás haciendo
6. **Verifica dimensiones** antes de hacer operaciones matriciales
7. **Imprime resultados intermedios** para validar tus cálculos
8. **Incluye interpretación económica** cuando se pida
9. **Si usas PuLP, desactiva mensajes** con `msg=0` para output limpio
10. **Revisa que tus gráficos tengan títulos y etiquetas en español**

---

**📌 ESTA ES LA ÚNICA METODOLOGÍA ACEPTADA POR EL PROFESOR**

Si usas métodos no enseñados, perderás puntos aunque la respuesta sea correcta.
