# 📘 GUÍA DE ESTUDIO - UNIDAD 1 (Sesiones 1-4)
## Metodología Exacta del Profesor - Arrays, DataFrames y Funciones Económicas

> ⚠️ **IMPORTANTE**: Esta guía usa **EXCLUSIVAMENTE** los métodos y herramientas que el profesor enseñó en clase. No hay métodos avanzados ni rebuscados. Si lo usas así, obtendrás mejor nota.

---

## 📌 ESTRUCTURA DE LA UNIDAD 1

**Sesión 1**: Introducción a Python - Vectores y Arrays  
**Sesión 2**: Manipulación de datos y visualización con pandas  
**Sesión 3**: Modelización de funciones económicas  
**Sesión 4**: Puntos de equilibrio y sistemas de ecuaciones  

---

## 🔧 HERRAMIENTAS Y MÉTODOS DEL PROFESOR

### Bloque de Importación Estándar (SIEMPRE igual)
```python
import numpy as np           # para hacer operaciones matemáticas
import pandas as pd          # para manejo de archivos de datos
import matplotlib.pyplot as plt  # para hacer gráficos
import seaborn as sns        # para hacer gráficos
```

### Funciones NumPy que SÍ usa el profesor
```python
np.array([...])              # Crear array
np.random.seed(numero)       # Fijar semilla aleatoria
np.random.randint(min, max, size=(filas, cols))  # Enteros aleatorios
np.random.uniform(min, max, size=(filas, cols))  # Flotantes aleatorios
np.arange(inicio, fin)       # Secuencia de números
np.linspace(inicio, fin, cantidad)  # Puntos espaciados uniformemente
np.dot(vector1, vector2)     # Producto punto (SUMAPRODUCTO)
np.concatenate((arr1, arr2), axis=1)  # Unir arrays
array.T                      # Transponer
array.mean()                 # Promedio
array.std()                  # Desvío estándar
array.sum()                  # Suma
array.min()                  # Mínimo
array.max()                  # Máximo
```

### Funciones Pandas que SÍ usa el profesor
```python
pd.DataFrame(data, index=..., columns=...)  # Crear DataFrame
df.head()                    # Primeras filas
df.tail()                    # Últimas filas
df.describe()                # Estadísticas descriptivas
df.sum(axis=1)               # Suma por filas
df.sum(axis=0)               # Suma por columnas
df.mean()                    # Promedio
df['columna'].sum()          # Suma de una columna
df.isnull().sum()            # Contar valores nulos
df.loc[fila, columna]        # Seleccionar por etiqueta
df.iloc[posicion]            # Seleccionar por posición
df[df['col'] > valor]        # Filtrar filas
df['nueva_col'] = ...        # Agregar columna
df.apply(lambda x: ...)      # Aplicar función
pd.concat([df1, df2], axis=1)  # Unir DataFrames horizontalmente
df.div(df['col'], axis=0)    # Dividir
```

### Visualizaciones que SÍ usa el profesor
```python
plt.figure(figsize=(ancho, alto))  # Tamaño del gráfico
plt.plot(x, y, label='...', color='...', linewidth=2)  # Gráfico de líneas
plt.bar(x, height, color='...')    # Gráfico de barras
plt.scatter(x, y, color='...')     # Dispersión
plt.pie(valores, labels=..., autopct='%1.1f%%')  # Torta
plt.title('Título')                # Título
plt.xlabel('Etiqueta X')           # Etiqueta eje X
plt.ylabel('Etiqueta Y')           # Etiqueta eje Y
plt.legend()                       # Leyenda
plt.grid(True)                     # Grilla
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical
plt.xticks(rotation=45)            # Rotar etiquetas X
plt.show()                         # Mostrar gráfico
```

### SymPy que SÍ usa el profesor (Sesión 4)
```python
import sympy as sp
x, p = sp.symbols('x p')     # Definir variables simbólicas
eq1 = sp.Eq(expresion1, expresion2)  # Crear ecuación
sp.solve((eq1, eq2), (x, p))  # Resolver sistema
```

---

## 📊 TIPO DE EJERCICIO: ANÁLISIS DE VENTAS/PRODUCCIÓN

Este es el **patrón típico del parcial** para la Unidad 1.

### ✅ PASO 1: SIMULACIÓN DE DATOS CON NUMPY

**Objetivo**: Generar datos aleatorios que simulen un escenario empresarial.

**Código exacto del profesor**:
```python
# Fijar semilla para reproducibilidad
np.random.seed(42)  # El número puede cambiar

# Array de cantidades (enteros)
# Tamaño: 18 semanas × 6 productos
q = np.random.randint(50, 200, size=(18, 6))

# Array de precios (flotantes)
# Misma forma que cantidades
p = np.random.uniform(10.0, 50.0, size=(18, 6))

# Array de semanas
semanas = np.arange(1, 19)  # Del 1 al 18

print("Array de cantidades (q):")
print(q[:5])  # Mostrar primeras 5 filas

print("\nArray de precios (p):")
print(p[:5])

print("\nArray de semanas:")
print(semanas)
```

**Qué observar**:
- Usa `np.random.randint()` para enteros
- Usa `np.random.uniform()` para decimales
- `size=(filas, columnas)` define la forma del array
- `np.arange(inicio, fin)` crea secuencia (el fin NO se incluye)

---

### ✅ PASO 2: CONSTRUCCIÓN DE DATAFRAME

**Objetivo**: Convertir arrays en tabla estructurada con pandas.

**Código exacto del profesor**:
```python
# Usar slicing para extraer solo los primeros 3 productos (A, B, C)
cantidades_abc = q[:, 0:3]  # Todas las filas, columnas 0, 1, 2
precios_abc = p[:, 0:3]

# Construir DataFrame
df = pd.DataFrame({
    'semana': semanas,
    'producto_A': cantidades_abc[:, 0],
    'producto_B': cantidades_abc[:, 1],
    'producto_C': cantidades_abc[:, 2],
    'precio_A': precios_abc[:, 0],
    'precio_B': precios_abc[:, 1],
    'precio_C': precios_abc[:, 2]
})

print("DataFrame creado:")
print(df.head())
```

**Qué observar**:
- Slicing de arrays: `[:, 0:3]` = todas las filas, columnas 0 a 2
- Diccionario para crear DataFrame: `{'columna': datos}`
- Acceso a columnas de array: `array[:, numero_columna]`

---

### ✅ PASO 3: VALIDACIÓN Y DESCRIPCIÓN ESTADÍSTICA

**Objetivo**: Verificar que no haya errores y entender los datos.

**Código exacto del profesor**:
```python
# Verificar valores nulos
print("Valores nulos por columna:")
print(df.isnull().sum())

print(f"\nTotal de valores nulos: {df.isnull().sum().sum()}")

# Descripción estadística de cantidades
cantidades_cols = ['producto_A', 'producto_B', 'producto_C']
print("\nEstadísticas de CANTIDADES:")
print(df[cantidades_cols].describe())

# Descripción estadística de precios
precios_cols = ['precio_A', 'precio_B', 'precio_C']
print("\nEstadísticas de PRECIOS:")
print(df[precios_cols].describe())
```

**Qué observar**:
- `isnull().sum()` cuenta nulls por columna
- `isnull().sum().sum()` cuenta total de nulls
- `describe()` da estadísticas automáticas
- Se puede hacer `describe()` sobre un subset de columnas

---

### ✅ PASO 4: OPERACIONES VECTORIZADAS (CÁLCULOS)

**Objetivo**: Calcular ingresos y totales usando operaciones con pandas.

**Código exacto del profesor**:
```python
# Calcular ingresos por producto (cantidad × precio)
df['ingreso_A'] = df['producto_A'] * df['precio_A']
df['ingreso_B'] = df['producto_B'] * df['precio_B']
df['ingreso_C'] = df['producto_C'] * df['precio_C']

# Calcular totales por semana
df['ingreso_total'] = df['ingreso_A'] + df['ingreso_B'] + df['ingreso_C']
df['cantidad_total'] = df['producto_A'] + df['producto_B'] + df['producto_C']

print("DataFrame con columnas agregadas:")
print(df.head())
```

**Qué observar**:
- Multiplicación de columnas: `df['col1'] * df['col2']`
- Suma de columnas: `df['col1'] + df['col2'] + df['col3']`
- Crear nueva columna: `df['nueva'] = cálculo`

---

### ✅ PASO 5: CÁLCULOS GLOBALES Y POR PERÍODO

**Objetivo**: Calcular totales acumulados y por períodos específicos.

**Código exacto del profesor**:
```python
# 1. Ingreso total por producto (todo el período)
ingreso_total_A = df['ingreso_A'].sum()
ingreso_total_B = df['ingreso_B'].sum()
ingreso_total_C = df['ingreso_C'].sum()

print("INGRESO TOTAL POR PRODUCTO (18 semanas):")
print(f"   Producto A: ${ingreso_total_A:,.2f}")
print(f"   Producto B: ${ingreso_total_B:,.2f}")
print(f"   Producto C: ${ingreso_total_C:,.2f}")

# 2. Ingreso en los primeros 6 semanas
primeros_6 = df.iloc[:6]  # Seleccionar filas 0 a 5
ingreso_6_A = primeros_6['ingreso_A'].sum()
ingreso_6_B = primeros_6['ingreso_B'].sum()
ingreso_6_C = primeros_6['ingreso_C'].sum()

print("\nINGRESO TOTAL POR PRODUCTO (primeras 6 semanas):")
print(f"   Producto A: ${ingreso_6_A:,.2f}")
print(f"   Producto B: ${ingreso_6_B:,.2f}")
print(f"   Producto C: ${ingreso_6_C:,.2f}")

# 3. Ingreso total de la empresa
ingreso_total_empresa = df['ingreso_total'].sum()

print(f"\nINGRESO TOTAL EMPRESA: ${ingreso_total_empresa:,.2f}")
```

**Qué observar**:
- `.sum()` suma todos los valores de una columna
- `.iloc[:6]` selecciona las primeras 6 filas (0 a 5)
- Formateo: `{valor:,.2f}` → separador de miles y 2 decimales

---

### ✅ PASO 6: ANÁLISIS DE PARTICIPACIONES

**Objetivo**: Calcular qué porcentaje representa cada producto del total.

**Código exacto del profesor**:
```python
# Calcular participaciones (%)
participacion_A = (ingreso_total_A / ingreso_total_empresa) * 100
participacion_B = (ingreso_total_B / ingreso_total_empresa) * 100
participacion_C = (ingreso_total_C / ingreso_total_empresa) * 100

print("PARTICIPACIÓN EN EL INGRESO TOTAL:")
print(f"Producto A: {participacion_A:.2f}%")
print(f"Producto B: {participacion_B:.2f}%")
print(f"Producto C: {participacion_C:.2f}%")

# Validar que sume 100%
total_participacion = participacion_A + participacion_B + participacion_C
print(f"\nValidación (debe ser 100%): {total_participacion:.2f}%")

# Encontrar el producto con mayor ingreso
ingresos_productos = {
    'A': ingreso_total_A,
    'B': ingreso_total_B,
    'C': ingreso_total_C
}

producto_max = max(ingresos_productos, key=ingresos_productos.get)
ingreso_max = ingresos_productos[producto_max]
participacion_max = (ingreso_max / ingreso_total_empresa) * 100

print(f"\nPRODUCTO CON MAYOR INGRESO: {producto_max}")
print(f"   Ingreso: ${ingreso_max:,.2f}")
print(f"   Participación: {participacion_max:.2f}%")
```

**Qué observar**:
- Fórmula participación: `(parte / total) * 100`
- Usar diccionario para agrupar datos relacionados
- `max(dict, key=dict.get)` encuentra la clave con valor máximo

---

### ✅ PASO 7: PROYECCIONES CON CAMBIOS PORCENTUALES

**Objetivo**: Calcular escenarios futuros aplicando porcentajes de cambio.

**Código exacto del profesor**:
```python
# Calcular promedios históricos (semanas 1-18)
promedio_A = df['producto_A'].mean()
promedio_B = df['producto_B'].mean()
promedio_C = df['producto_C'].mean()

print("PROMEDIOS HISTÓRICOS:")
print(f"   Producto A: {promedio_A:.2f} unidades")
print(f"   Producto B: {promedio_B:.2f} unidades")
print(f"   Producto C: {promedio_C:.2f} unidades")

# Aplicar cambios proyectados
# A aumenta 10%, B cae 5%, C aumenta 20%
cantidad_A_s19 = promedio_A * 1.10  # +10% = multiplicar por 1.10
cantidad_B_s19 = promedio_B * 0.95  # -5% = multiplicar por 0.95
cantidad_C_s19 = promedio_C * 1.20  # +20% = multiplicar por 1.20

print("\nCANTIDADES PROYECTADAS SEMANA 19:")
print(f"   Producto A: {cantidad_A_s19:.2f} unidades (+10%)")
print(f"   Producto B: {cantidad_B_s19:.2f} unidades (-5%)")
print(f"   Producto C: {cantidad_C_s19:.2f} unidades (+20%)")

# Precios se mantienen (usar promedio)
precio_A_s19 = df['precio_A'].mean()
precio_B_s19 = df['precio_B'].mean()
precio_C_s19 = df['precio_C'].mean()

# Calcular ingresos proyectados
ingreso_A_s19 = cantidad_A_s19 * precio_A_s19
ingreso_B_s19 = cantidad_B_s19 * precio_B_s19
ingreso_C_s19 = cantidad_C_s19 * precio_C_s19
ingreso_total_s19 = ingreso_A_s19 + ingreso_B_s19 + ingreso_C_s19

print(f"\nINGRESO TOTAL PROYECTADO SEMANA 19: ${ingreso_total_s19:,.2f}")

# Comparar con promedio histórico
promedio_ingreso_historico = df['ingreso_total'].mean()
diferencia_abs = ingreso_total_s19 - promedio_ingreso_historico
diferencia_pct = ((ingreso_total_s19 - promedio_ingreso_historico) / promedio_ingreso_historico) * 100

print(f"\nCOMPARACIÓN CON PROMEDIO HISTÓRICO:")
print(f"   Promedio histórico: ${promedio_ingreso_historico:,.2f}")
print(f"   Diferencia absoluta: ${diferencia_abs:,.2f}")
print(f"   Diferencia porcentual: {diferencia_pct:+.2f}%")
```

**Qué observar**:
- **Aumento X%**: multiplicar por `(1 + X/100)` → +10% = `×1.10`
- **Disminución X%**: multiplicar por `(1 - X/100)` → -5% = `×0.95`
- **Diferencia porcentual**: `((nuevo - viejo) / viejo) * 100`
- `.mean()` calcula promedio de una columna

---

### ✅ PASO 8: VISUALIZACIÓN - GRÁFICO DE LÍNEAS

**Objetivo**: Mostrar evolución temporal de cantidades.

**Código exacto del profesor**:
```python
plt.figure(figsize=(10, 6))

# Graficar cada producto
plt.plot(df['semana'], df['producto_A'], 
         marker='o', label='Producto A', linewidth=2)
plt.plot(df['semana'], df['producto_B'], 
         marker='s', label='Producto B', linewidth=2)
plt.plot(df['semana'], df['producto_C'], 
         marker='^', label='Producto C', linewidth=2)

# Configuración
plt.title('Evolución de Cantidades Vendidas por Producto', fontsize=14)
plt.xlabel('Semana', fontsize=12)
plt.ylabel('Cantidades Vendidas (unidades)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='best')
plt.axhline(0, color='black', linewidth=0.5)

plt.show()
```

**Qué observar**:
- `plt.plot(x, y, marker='...', label='...', linewidth=...)` 
- Marcadores: `'o'` círculo, `'s'` cuadrado, `'^'` triángulo
- `plt.legend(loc='best')` coloca leyenda automáticamente
- `alpha=0.3` hace la grilla semitransparente

---

### ✅ PASO 9: VISUALIZACIÓN - GRÁFICO DE BARRAS

**Objetivo**: Comparar participaciones porcentuales.

**Código exacto del profesor**:
```python
plt.figure(figsize=(8, 6))

# Datos
productos = ['Producto A', 'Producto B', 'Producto C']
participaciones = [participacion_A, participacion_B, participacion_C]
colores = ['skyblue', 'lightgreen', 'lightcoral']

# Crear gráfico de barras
barras = plt.bar(productos, participaciones, color=colores, alpha=0.8)

# Agregar valores sobre las barras
for i, barra in enumerate(barras):
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, altura + 0.5,
             f'{participaciones[i]:.1f}%', 
             ha='center', va='bottom', fontweight='bold')

# Configuración
plt.title('Participación en el Ingreso Total por Producto', fontsize=14)
plt.xlabel('Productos', fontsize=12)
plt.ylabel('Participación (%)', fontsize=12)
plt.grid(True, axis='y', alpha=0.3)

plt.show()
```

**Qué observar**:
- `plt.bar(x, height, color=..., alpha=...)` crea barras
- `enumerate()` para iterar con índice
- `barra.get_height()` obtiene la altura de cada barra
- `plt.text(x, y, texto)` agrega texto en posición específica
- `ha='center', va='bottom'` alinea el texto

---

### ✅ PASO 10: DEFINICIÓN DE FUNCIÓN DE CLASIFICACIÓN

**Objetivo**: Crear función personalizada para clasificar datos.

**Código exacto del profesor**:
```python
def clasificar_semana(df):
    """
    Clasifica semanas según ingreso total.
    """
    # Calcular promedio
    promedio_ingreso = df['ingreso_total'].mean()
    
    # Umbral: 110% del promedio
    umbral = promedio_ingreso * 1.10
    
    # Clasificar usando apply con lambda
    df['clasificacion'] = df['ingreso_total'].apply(
        lambda x: "buena semana" if x > umbral else "normal"
    )
    
    return df

# Aplicar la función
df = clasificar_semana(df)

print("CLASIFICACIÓN DE SEMANAS:")
print(df['clasificacion'].value_counts())

print("\nMUESTRA DEL DATAFRAME CON CLASIFICACIÓN:")
print(df[['semana', 'ingreso_total', 'clasificacion']].head(10))
```

**Qué observar**:
- Estructura básica de función con `def nombre(parametros):`
- `df['col'].apply(lambda x: ...)` aplica función a cada valor
- `lambda x: valor_si_true if condicion else valor_si_false`
- `value_counts()` cuenta ocurrencias de cada valor

---

### ✅ PASO 11: FUNCIÓN QUE DEVUELVE DICCIONARIO

**Objetivo**: Crear función que devuelve diccionario con clasificación.

**Código exacto del profesor**:
```python
def clasificar_producto(df):
    """
    Clasifica productos según participación en ingreso total.
    Devuelve diccionario con información de cada producto.
    """
    # Calcular ingresos totales
    ingreso_A = df['ingreso_A'].sum()
    ingreso_B = df['ingreso_B'].sum()
    ingreso_C = df['ingreso_C'].sum()
    ingreso_total = ingreso_A + ingreso_B + ingreso_C
    
    # Calcular participaciones
    participacion_A = (ingreso_A / ingreso_total) * 100
    participacion_B = (ingreso_B / ingreso_total) * 100
    participacion_C = (ingreso_C / ingreso_total) * 100
    
    # Crear diccionario de resultados
    resultados = {}
    
    # Clasificar Producto A
    if participacion_A >= 30:
        clasificacion_A = "estrella"
    else:
        clasificacion_A = "secundario"
    
    resultados['Producto A'] = {
        'ingreso': ingreso_A,
        'participacion': participacion_A,
        'clasificacion': clasificacion_A
    }
    
    # Clasificar Producto B
    if participacion_B >= 30:
        clasificacion_B = "estrella"
    else:
        clasificacion_B = "secundario"
    
    resultados['Producto B'] = {
        'ingreso': ingreso_B,
        'participacion': participacion_B,
        'clasificacion': clasificacion_B
    }
    
    # Clasificar Producto C
    if participacion_C >= 30:
        clasificacion_C = "estrella"
    else:
        clasificacion_C = "secundario"
    
    resultados['Producto C'] = {
        'ingreso': ingreso_C,
        'participacion': participacion_C,
        'clasificacion': clasificacion_C
    }
    
    return resultados

# Aplicar la función
clasificacion = clasificar_producto(df)

print("CLASIFICACIÓN DE PRODUCTOS:")
for producto, info in clasificacion.items():
    print(f"\n{producto}:")
    print(f"  Ingreso: ${info['ingreso']:,.2f}")
    print(f"  Participación: {info['participacion']:.2f}%")
    print(f"  Clasificación: {info['clasificacion'].upper()}")
```

**Qué observar**:
- Diccionarios anidados: `dict = {'key': {'subkey': valor}}`
- `if condicion:` para clasificar
- `.items()` para iterar diccionario: `for key, value in dict.items()`
- Acceso a valores: `dict['key']['subkey']`

---

## 📊 TIPO DE EJERCICIO: FUNCIONES ECONÓMICAS Y EQUILIBRIO

Este es el patrón de la **Sesión 3 y 4** que puede aparecer en el parcial.

### ✅ GRAFICAR FUNCIONES ECONÓMICAS

**Código exacto del profesor (Sesión 3)**:
```python
import matplotlib.pyplot as plt
import numpy as np

# Función lineal: y = mx + b
m = 2
b = 6

x = np.linspace(-5, 5, 100)
y = m * x + b

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f'y = {m}x + {b}')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Función Lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
```

**Qué observar**:
- `np.linspace(inicio, fin, puntos)` crea valores espaciados
- `plt.axhline(0)` dibuja eje horizontal
- `plt.axvline(0)` dibuja eje vertical

---

### ✅ RESOLVER SISTEMA DE ECUACIONES (EQUILIBRIO)

**Código exacto del profesor (Sesión 4)**:
```python
import sympy as sp

# Paso 1: Definir funciones de oferta y demanda
def demanda(x):
    return -1/3*x + 5

def oferta(x):
    return 1/2*x + 3/2

# Paso 2: Crear variables simbólicas
x, p = sp.symbols('x p')

# Paso 3: Definir ecuaciones
eq1 = sp.Eq(p, demanda(x))  # Demanda
eq2 = sp.Eq(p, oferta(x))   # Oferta

# Paso 4: Resolver el sistema
solucion = sp.solve((eq1, eq2), (x, p))
x_eq = solucion[x]
p_eq = solucion[p]

print(f"Punto de equilibrio: x = {x_eq:.2f}, p = {p_eq:.2f}")

# Paso 5: Graficar
valores_x = np.linspace(0, 10, 100)

plt.figure(figsize=(8, 6))
plt.plot(valores_x, demanda(valores_x), 'blue', label='Demanda: $p = -1/3x + 5$')
plt.plot(valores_x, oferta(valores_x), 'red', label='Oferta: $p = 1/2x + 3/2$')
plt.scatter(x_eq, p_eq, color='green', s=100, 
            label=f'Equilibrio (x={x_eq:.2f}, p={p_eq:.2f})')

plt.ylabel('Precio (p)')
plt.xlabel('Cantidad (x)')
plt.legend()
plt.grid(True)
plt.title('Equilibrio de Mercado')
plt.show()
```

**Qué observar**:
- Definir funciones normales de Python: `def nombre(parametro):`
- Variables simbólicas: `sp.symbols('x p')`
- Crear ecuación: `sp.Eq(lado_izq, lado_der)`
- Resolver: `sp.solve((ec1, ec2), (var1, var2))`
- `plt.scatter()` para marcar un punto específico

---

## 🎯 CHECKLIST DEL PARCIAL - UNIDAD 1

### Antes de Empezar
- [ ] Importar librerías en el orden del profesor
- [ ] Leer TODAS las consignas antes de codear
- [ ] Identificar qué tipo de ejercicio es (ventas/producción o funciones económicas)

### Durante el Ejercicio
- [ ] **Paso 1**: Generar arrays con `np.random.randint()` y `np.random.uniform()`
- [ ] **Paso 2**: Construir DataFrame con diccionario
- [ ] **Paso 3**: Verificar nulls con `isnull().sum()` y hacer `describe()`
- [ ] **Paso 4**: Calcular ingresos y totales creando nuevas columnas
- [ ] **Paso 5**: Usar `.sum()` y `.mean()` para totales y promedios
- [ ] **Paso 6**: Calcular participaciones con fórmula `(parte/total)*100`
- [ ] **Paso 7**: Aplicar cambios porcentuales con multiplicación
- [ ] **Paso 8**: Graficar evolución con `plt.plot()`
- [ ] **Paso 9**: Graficar participaciones con `plt.bar()`
- [ ] **Paso 10**: Definir función de clasificación con `apply(lambda)`
- [ ] **Paso 11**: Definir función que devuelva diccionario

### Revisión Final
- [ ] Todas las celdas ejecutan sin errores
- [ ] Los gráficos tienen título, ejes y leyenda
- [ ] Los prints tienen formato claro (`:,.2f` para dinero)
- [ ] Las funciones devuelven lo que piden (DataFrame o diccionario)

---

## ⚠️ ERRORES COMUNES A EVITAR

### ❌ NO usar estos métodos (no los enseñó el profesor):
```python
# NO USAR:
df.groupby()        # No se enseñó
df.pivot()          # No se enseñó
df.melt()           # No se enseñó
df.query()          # No se enseñó
pd.cut()            # No se enseñó
df.agg()            # No se enseñó
```

### ✅ SÍ usar estos métodos (los enseñó el profesor):
```python
# SÍ USAR:
df['col'].sum()     # Lo usa siempre
df['col'].mean()    # Lo usa siempre
df.apply(lambda)    # Lo usa para clasificar
for loop simple     # Lo usa en funciones
if/else simple      # Lo usa en funciones
diccionarios {}     # Lo usa para agrupar
```

---

## 📝 EJERCICIO RESUELTO COMPLETO

**Basado en el parcial real de ballera-919064.ipynb**

```python
# ============================================
# EJERCICIO COMPLETO - ANÁLISIS DE VENTAS
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PASO 1: SIMULACIÓN
np.random.seed(42)
q = np.random.randint(50, 200, size=(18, 6))
p = np.random.uniform(10.0, 50.0, size=(18, 6))
semanas = np.arange(1, 19)

# PASO 2: DATAFRAME
df = pd.DataFrame({
    'semana': semanas,
    'producto_A': q[:, 0],
    'producto_B': q[:, 1],
    'producto_C': q[:, 2],
    'precio_A': p[:, 0],
    'precio_B': p[:, 1],
    'precio_C': p[:, 2]
})

# PASO 3: VALIDACIÓN
print("Valores nulos:")
print(df.isnull().sum())
print("\nEstadísticas:")
print(df.describe())

# PASO 4: OPERACIONES VECTORIZADAS
df['ingreso_A'] = df['producto_A'] * df['precio_A']
df['ingreso_B'] = df['producto_B'] * df['precio_B']
df['ingreso_C'] = df['producto_C'] * df['precio_C']
df['ingreso_total'] = df['ingreso_A'] + df['ingreso_B'] + df['ingreso_C']
df['cantidad_total'] = df['producto_A'] + df['producto_B'] + df['producto_C']

# PASO 5: TOTALES
ingreso_total_A = df['ingreso_A'].sum()
ingreso_total_B = df['ingreso_B'].sum()
ingreso_total_C = df['ingreso_C'].sum()
ingreso_empresa = df['ingreso_total'].sum()

print(f"\nIngreso Producto A: ${ingreso_total_A:,.2f}")
print(f"Ingreso Producto B: ${ingreso_total_B:,.2f}")
print(f"Ingreso Producto C: ${ingreso_total_C:,.2f}")
print(f"Ingreso Total Empresa: ${ingreso_empresa:,.2f}")

# PASO 6: PARTICIPACIONES
participacion_A = (ingreso_total_A / ingreso_empresa) * 100
participacion_B = (ingreso_total_B / ingreso_empresa) * 100
participacion_C = (ingreso_total_C / ingreso_empresa) * 100

print(f"\nParticipación A: {participacion_A:.2f}%")
print(f"Participación B: {participacion_B:.2f}%")
print(f"Participación C: {participacion_C:.2f}%")

# Producto con mayor ingreso
ingresos = {'A': ingreso_total_A, 'B': ingreso_total_B, 'C': ingreso_total_C}
producto_max = max(ingresos, key=ingresos.get)
print(f"\nProducto con mayor ingreso: {producto_max}")

# PASO 7: PROYECCIÓN
promedio_A = df['producto_A'].mean()
promedio_B = df['producto_B'].mean()
promedio_C = df['producto_C'].mean()

cantidad_A_s19 = promedio_A * 1.10
cantidad_B_s19 = promedio_B * 0.95
cantidad_C_s19 = promedio_C * 1.20

precio_A_s19 = df['precio_A'].mean()
precio_B_s19 = df['precio_B'].mean()
precio_C_s19 = df['precio_C'].mean()

ingreso_s19 = (cantidad_A_s19 * precio_A_s19 + 
               cantidad_B_s19 * precio_B_s19 + 
               cantidad_C_s19 * precio_C_s19)

promedio_historico = df['ingreso_total'].mean()
diferencia_pct = ((ingreso_s19 - promedio_historico) / promedio_historico) * 100

print(f"\nIngreso proyectado semana 19: ${ingreso_s19:,.2f}")
print(f"Diferencia vs promedio: {diferencia_pct:+.2f}%")

# PASO 8: GRÁFICO DE LÍNEAS
plt.figure(figsize=(10, 6))
plt.plot(df['semana'], df['producto_A'], marker='o', label='Producto A', linewidth=2)
plt.plot(df['semana'], df['producto_B'], marker='s', label='Producto B', linewidth=2)
plt.plot(df['semana'], df['producto_C'], marker='^', label='Producto C', linewidth=2)
plt.title('Evolución de Cantidades Vendidas')
plt.xlabel('Semana')
plt.ylabel('Cantidades')
plt.legend()
plt.grid(True)
plt.show()

# PASO 9: GRÁFICO DE BARRAS
plt.figure(figsize=(8, 6))
productos = ['Producto A', 'Producto B', 'Producto C']
participaciones = [participacion_A, participacion_B, participacion_C]
barras = plt.bar(productos, participaciones, color=['skyblue', 'lightgreen', 'lightcoral'])

for i, barra in enumerate(barras):
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, altura + 0.5,
             f'{participaciones[i]:.1f}%', ha='center', va='bottom')

plt.title('Participación en Ingreso Total')
plt.ylabel('Participación (%)')
plt.grid(True, axis='y')
plt.show()

# PASO 10: FUNCIÓN CLASIFICAR_SEMANA
def clasificar_semana(df):
    promedio_ingreso = df['ingreso_total'].mean()
    umbral = promedio_ingreso * 1.10
    df['clasificacion'] = df['ingreso_total'].apply(
        lambda x: "buena semana" if x > umbral else "normal"
    )
    return df

df = clasificar_semana(df)
print("\nClasificación de semanas:")
print(df['clasificacion'].value_counts())

# PASO 11: FUNCIÓN CLASIFICAR_PRODUCTO
def clasificar_producto(df):
    ingreso_A = df['ingreso_A'].sum()
    ingreso_B = df['ingreso_B'].sum()
    ingreso_C = df['ingreso_C'].sum()
    ingreso_total = ingreso_A + ingreso_B + ingreso_C
    
    participacion_A = (ingreso_A / ingreso_total) * 100
    participacion_B = (ingreso_B / ingreso_total) * 100
    participacion_C = (ingreso_C / ingreso_total) * 100
    
    resultados = {}
    
    if participacion_A >= 30:
        clasificacion_A = "estrella"
    else:
        clasificacion_A = "secundario"
    
    resultados['Producto A'] = {
        'ingreso': ingreso_A,
        'participacion': participacion_A,
        'clasificacion': clasificacion_A
    }
    
    if participacion_B >= 30:
        clasificacion_B = "estrella"
    else:
        clasificacion_B = "secundario"
    
    resultados['Producto B'] = {
        'ingreso': ingreso_B,
        'participacion': participacion_B,
        'clasificacion': clasificacion_B
    }
    
    if participacion_C >= 30:
        clasificacion_C = "estrella"
    else:
        clasificacion_C = "secundario"
    
    resultados['Producto C'] = {
        'ingreso': ingreso_C,
        'participacion': participacion_C,
        'clasificacion': clasificacion_C
    }
    
    return resultados

clasificacion = clasificar_producto(df)
print("\nClasificación de productos:")
for producto, info in clasificacion.items():
    print(f"\n{producto}:")
    print(f"  Ingreso: ${info['ingreso']:,.2f}")
    print(f"  Participación: {info['participacion']:.2f}%")
    print(f"  Clasificación: {info['clasificacion']}")
```

---

## 🎓 CONSEJOS FINALES PARA EL EXAMEN

1. **Usa EXACTAMENTE la metodología del profesor**
   - No inventes métodos nuevos
   - Sigue la estructura paso a paso
   - Usa los mismos nombres de variables cuando sea posible

2. **Comentarios claros pero simples**
   - "# Calcular ingresos por producto"
   - "# Graficar evolución de cantidades"
   - No hace falta comentar cada línea

3. **Formato de prints profesional**
   - Usa `{variable:,.2f}` para dinero
   - Usa `{variable:.2f}` para porcentajes
   - Incluye unidades: "unidades", "$", "%"

4. **Validaciones básicas**
   - Verifica que participaciones sumen 100%
   - Verifica que no haya nulls
   - Muestra primeras filas del DataFrame

5. **Gráficos completos**
   - Siempre incluye título, ejes y leyenda
   - Usa `plt.grid(True)` para mejor lectura
   - Agrega líneas de referencia con `axhline()` cuando corresponda

---

**Éxito en el examen! 🚀 Si sigues esta guía al pie de la letra, usando SOLO estos métodos, tu código será evaluado positivamente porque es exactamente lo que el profesor espera.**
