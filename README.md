# 📊 Laboratorio TGAD (FCE - UBA)

> **Tecnicatura de Gestión y Análisis de Datos**  
> Facultad de Ciencias Económicas - Universidad de Buenos Aires

Repositorio académico con materiales, prácticas y recursos para el curso de análisis de datos aplicado a ciencias económicas.

---

## 📖 Descripción

Este repositorio contiene todo el material necesario para la **Tecnicatura de Gestión y Análisis de Datos (TGAD)** de la FCE-UBA. El enfoque está en la **aplicación práctica** de Python para:

- 📈 Manipulación y análisis de datos económicos
- 📊 Visualización de información empresarial
- 🧮 Modelización de funciones económicas
- 💹 Análisis de inversiones y finanzas
- 🔬 Optimización y programación lineal
- 📉 Cálculo diferencial e integral aplicado

---

## 🚀 Guía de Inicio Rápido

### Requisitos Previos

- **Python 3.10+** instalado
- **Git** para clonar el repositorio
- Editor de código (recomendado: **VS Code** o **Jupyter Lab**)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/alexballera/laboratorio-tgad-fce.git
cd laboratorio-tgad-fce
```

### Paso 2: Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar el entorno virtual
# En Linux/Mac:
source .venv/bin/activate

# En Windows:
.venv\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Iniciar Jupyter Lab

```bash
jupyter lab
```

¡Listo! Ya puedes empezar a trabajar con los notebooks del curso.

---

## 🆕 Novedades y Mejoras Recientes

### Noviembre 2024 - Refactorización del Módulo Financiero

Se realizó una **optimización completa** del módulo `utils/matematicas_financieras.py`:

#### ✨ Cambios Principales

- **Consolidación de funciones**: Eliminadas redundancias (~80 líneas de código)
- **Priorización de numpy_financial**: Todas las funciones usan `npf` como base
- **Mejoras de usabilidad**:
  - Interfaz consistente para funciones de inversión
  - Validaciones robustas con mensajes claros en español
  - Parámetros más descriptivos y documentados
- **Flexibilidad académica**: Método Newton-Raphson disponible como opción didáctica
- **Documentación expandida**:
  - Guía completa en [`utils/README.md`](./utils/README.md) con ejemplos
  - Changelog de migración en [`utils/CHANGELOG_REFACTORIZACION.md`](./utils/CHANGELOG_REFACTORIZACION.md)
  - Tests actualizados en `test_matematicas_financieras.py`

#### 📊 Impacto

| Métrica | Antes | Ahora | Mejora |
|---------|-------|-------|--------|
| Funciones redundantes | 4 pares | 0 | 100% |
| Líneas de código | ~1,175 | ~1,095 | -80 líneas |
| Cobertura de tests | Parcial | Completa | ✅ |
| Documentación | Básica | Extensa | 3x más |

**Ver detalles completos**: [`utils/CHANGELOG_REFACTORIZACION.md`](./utils/CHANGELOG_REFACTORIZACION.md)

---

## 📁 Estructura del Proyecto

```text
laboratorio-tgad-fce/
│
├── 📂 1er_parcial/                    # Primer Parcial (Sesiones 1-12)
│   ├── parcial/                       # Material del examen parcial
│   ├── sesion1_Introducción_a_python_para_el_manejo_de_datos_organizacional/
│   ├── sesion2_Manipulación_de_datos_organizacionales_y_visualización/
│   ├── sesion3_Modelización_de_funciones_económicas/
│   ├── sesion4_Puntos_de_equilibrio_y_sistemas_de_ecuaciones/
│   ├── sesion5_Matrices_y_Leontief/
│   ├── sesion6_Manipulación_de_datos_estructurados_y_Leontief/
│   ├── sesion7_Programación_lineal_en_Python/
│   ├── sesion9_Derivada_y_variaciones_de_funciones_Elasticidades/
│   ├── sesion11_Optimización_de_funciones_aplicado_a_la_gestion/
│   └── sesion12_Optimización_de_funciones_Duopolio/
│
├── 📂 2do_parcial/                    # Segundo Parcial (Sesiones 13-17)
│   ├── parcial/                       # Material del examen parcial
│   ├── simulacro/                     # Ejercicios de práctica
│   └── sesiones/
│       ├── sesion_13_14_15_integrales/    # Integrales (indefinidas, aplicaciones, definidas)
│       │   ├── 13_Integrales_Indefinidas.ipynb
│       │   ├── 14_Aplicacion_Integrales.ipynb
│       │   └── 15_Integrales_Definidas.ipynb
│       └── sesion_16_17_finanzas/         # Análisis de Inversiones
│           ├── 16_finanzas_1.ipynb
│           └── 17_finanzas_2.ipynb
│
├── 📂 actividades/                    # Actividades prácticas entregadas
│   ├── BalleraActividades1erParcial.pdf  # Compilación actividades 1er parcial
│   ├── actividad1/                    # Introducción a NumPy y Pandas
│   ├── actividad2/                    # Manipulación de datos (4 notebooks)
│   ├── actividad3/                    # Visualización con datasets
│   ├── actividad4/                    # Análisis exploratorio
│   ├── actividad9/                    # Derivadas y variaciones (YPF)
│   ├── actividad-semana9/             # Material complementario derivadas
│   ├── actividad13/                   # Aplicación de integrales
│   └── actividad16/                   # Análisis de inversiones
│
├── 📂 utils/                          # 🔧 Utilidades y bibliotecas reutilizables
│   ├── matematicas_financieras.py     # Librería financiera refactorizada
│   ├── test_matematicas_financieras.py # Suite de pruebas completa
│   ├── README.md                      # Documentación de utilidades
│   └── CHANGELOG_REFACTORIZACION.md   # Guía de migración de funciones
│
├── 📂 fuentes/                        # Material de referencia
│   └── Cronograma.xlsx                # Cronograma académico del curso
│
├── 📂 .github/                        # Configuración GitHub
│   ├── copilot-instructions.md        # Instrucciones para GitHub Copilot
│   └── student-code-style-guidelines.md # Guías de estilo académico
│
├── 📄 requirements.txt                # Dependencias del proyecto
├── 📄 AGENTS.md                       # 🤖 Instrucciones completas para IA
├── 📄 README_SETUP.md                 # Guía de configuración del entorno
└── 📄 LICENSE                         # Licencia MIT

```

---

## 🛠️ Tecnologías y Librerías

### Core de Análisis de Datos

- **NumPy** 2.3.2 - Computación numérica
- **Pandas** 2.3.2 - Manipulación de datos
- **Matplotlib** 3.10.5 - Visualización estática
- **Seaborn** 0.13.2 - Visualización estadística

### Análisis Científico y Estadístico

- **SciPy** 1.16.1 - Computación científica
- **Scikit-learn** 1.7.1 - Machine Learning
- **Statsmodels** 0.14.5 - Modelos estadísticos

### Finanzas y Optimización

- **numpy-financial** 1.0.0 - Cálculos financieros
- **yfinance** 0.2.40 - Datos financieros en tiempo real
- **PuLP** 2.8.0 - Programación lineal
- **mplfinance** 0.12.10b0 - Gráficos financieros

### Visualización Avanzada

- **Plotly** 6.3.0 - Gráficos interactivos
- **Panel** 1.5.4 - Dashboards
- **WordCloud** 1.9.3 - Nubes de palabras

### Entorno de Desarrollo

- **Jupyter Lab** 4.4.6 - Ambiente de notebooks
- **IPyKernel** 6.30.1 - Kernel de Python
- **IPyWidgets** 8.1.7 - Widgets interactivos

---

## 📚 Contenido del Curso

### 🎯 Primer Parcial (Sesiones 1-12)

| Sesión | Tema | Conceptos Clave |
|--------|------|-----------------|
| **1** | Introducción a Python | NumPy, arrays, operaciones básicas |
| **2** | Manipulación de datos | Pandas, DataFrames, limpieza de datos |
| **3** | Modelización de funciones | Funciones económicas, oferta y demanda |
| **4** | Puntos de equilibrio | Sistemas de ecuaciones, break-even |
| **5** | Matrices y Leontief | Álgebra matricial, modelo input-output |
| **6** | Datos estructurados | Joins, merge, groupby avanzado |
| **7** | Programación lineal | Optimización con PuLP, problemas de asignación |
| **9** | Derivadas y elasticidades | Cálculo diferencial, análisis marginal |
| **11** | Optimización | Máximos y mínimos, funciones de varias variables |
| **12** | Duopolio | Teoría de juegos, equilibrio de Nash |

### 🎯 Segundo Parcial (Sesiones 13-17)

| Sesión | Tema | Conceptos Clave |
|--------|------|-----------------|
| **13** | Integrales Indefinidas | Primitivas, técnicas de integración, familias de funciones |
| **14** | Aplicación de Integrales | Costos totales, funciones acumuladas, problemas empresariales |
| **15** | Integrales Definidas | Áreas bajo la curva, excedentes del consumidor y productor, DWL |
| **16** | Análisis de inversiones I | VAN, TIR, TIRM, flujos de caja descontados |
| **17** | Análisis de inversiones II | Evaluación de proyectos, índice de rentabilidad, numpy-financial |

---

## 🔧 Utilidades Disponibles

### Módulo `utils/matematicas_financieras.py` ⭐ (Refactorizado 2024)

Biblioteca completa de funciones financieras optimizada con **numpy_financial**:

```python
from utils.matematicas_financieras import (
    # Valor temporal del dinero
    present_value,           # Valor presente (PV)
    future_value,            # Valor futuro (FV)
    
    # Evaluación de inversiones
    net_present_value,       # Valor actual neto (VAN/NPV)
    internal_rate_of_return, # Tasa interna de retorno (TIR/IRR)
    modified_internal_rate_of_return,  # TIRM/MIRR
    profitability_index,     # Índice de rentabilidad
    payback_period,          # Período de recuperación
    
    # Análisis de préstamos
    payment_amount,          # Cuota de préstamo (PMT)
    payment_interest,        # Interés del pago (IPMT)
    payment_principal,       # Capital del pago (PPMT)
    
    # Tasas de interés
    nominal_to_effective_rate,  # Conversión tasa nominal
    effective_annual_rate,      # Tasa efectiva anual
    
    # Análisis avanzado
    monte_carlo_npv,         # Simulación de riesgo
    sensitivity_analysis_npv, # Análisis de sensibilidad
)
```

**Características principales:**

- ✅ Prioriza **numpy_financial** para máxima precisión
- ✅ Funciones consolidadas (código limpio, sin redundancias)
- ✅ Validaciones robustas con mensajes en español
- ✅ Soporta vectorización con NumPy arrays
- ✅ Método Newton-Raphson disponible para enseñanza
- ✅ Documentación JSDoc completa con ejemplos
- ✅ Suite de tests incluida (`test_matematicas_financieras.py`)

**Documentación completa:** Ver [`utils/README.md`](./utils/README.md)

**Guía de migración:** Ver [`utils/CHANGELOG_REFACTORIZACION.md`](./utils/CHANGELOG_REFACTORIZACION.md)

### Script `utils/check_uncommitted_changes.py`

Verificador de cambios sin commitear para operaciones seguras en la nube:

```bash
# Verificación básica
python utils/check_uncommitted_changes.py

# Modo estricto (incluye archivos no rastreados)
python utils/check_uncommitted_changes.py --strict
```

**Características:**

- ✅ Detecta archivos modificados sin commitear
- ✅ Detecta cambios en staging sin commit
- ✅ Modo estricto para archivos no rastreados
- ✅ Integrado con GitHub Actions
- ✅ Mensajes descriptivos en español
- ✅ Tests unitarios incluidos

Ver documentación completa en [`utils/README.md`](./utils/README.md)

---

## 📝 Flujo de Trabajo Recomendado

### Para Cada Sesión

1. **Revisar materiales** en las carpetas `1er_parcial/` o `2do_parcial/sesiones/`
2. **Seguir los notebooks** con ejemplos paso a paso
3. **Completar actividades** en la carpeta `actividades/`
4. **Consultar `utils/`** para funciones financieras reutilizables
5. **Revisar documentación** de utilidades antes de implementar cálculos

### Estructura de Organización

```text
📚 Sesiones (Teoría + Práctica)
    ↓
📝 Actividades (Aplicación)
    ↓
🔧 Utils (Herramientas reutilizables)
    ↓
📊 Parciales (Evaluación)
```

### Convenciones de Código

```python
# Bloque de importación estándar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de visualización
plt.figure(figsize=(8, 5))
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
```

---

## 🤝 Para Estudiantes

### ¿Cómo usar este repositorio?

1. **Clonar y configurar** siguiendo la Guía de Inicio Rápido
2. **Navegar por sesiones** en `1er_parcial/` y `2do_parcial/sesiones/`
3. **Practicar con actividades** para reforzar conceptos
4. **Usar `utils/matematicas_financieras.py`** en tus análisis financieros
5. **Consultar documentación** en `utils/README.md` para funciones disponibles

### Actualizaciones Recientes 🆕

- **Noviembre 2024**: Refactorización completa del módulo financiero
  - Consolidación de funciones redundantes
  - Priorización de numpy_financial
  - Documentación expandida con ejemplos
  - Suite de tests actualizada
  - Guía de migración disponible

### Consejos

- 💡 Los comentarios están en **español** para facilitar el aprendizaje
- 📖 Cada notebook incluye **objetivos de aprendizaje** claros
- 🎓 Los ejemplos tienen **contexto económico y empresarial real**
- 🔍 Usa los tests en `utils/` como referencia de buenas prácticas
- 🧮 Revisa [`utils/README.md`](./utils/README.md) antes de implementar cálculos financieros

---

## 📖 Documentación Adicional

- **[AGENTS.md](./AGENTS.md)** - 🤖 Instrucciones completas para asistentes de IA y estándares del proyecto
- **[README_SETUP.md](./README_SETUP.md)** - Guía detallada de configuración del entorno
- **[utils/README.md](./utils/README.md)** - 🔧 Documentación completa del módulo de matemáticas financieras
- **[utils/CHANGELOG_REFACTORIZACION.md](./utils/CHANGELOG_REFACTORIZACION.md)** - Guía de migración de funciones
- **[.github/copilot-instructions.md](./.github/copilot-instructions.md)** - Instrucciones para GitHub Copilot
- **[.github/student-code-style-guidelines.md](./.github/student-code-style-guidelines.md)** - Guías de estilo académico
- **[LICENSE](./LICENSE)** - Licencia MIT del proyecto

---

## 🤖 Trabajo con Asistentes de IA

Este proyecto incluye instrucciones específicas para trabajar con GitHub Copilot y otros asistentes de IA. Consulta **[AGENTS.md](./AGENTS.md)** para:

- Estándares de código académico
- Convenciones de notebooks
- Guías de estilo para estudiantes
- Flujos de trabajo didácticos

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver archivo [LICENSE](./LICENSE) para más detalles.

---

## 👥 Autor

**Alex Ballera**  
Estudiante FCE-UBA  
📧 Contacto: [GitHub](https://github.com/alexballera)

---

## 🌟 Contribuciones

Este es un repositorio académico personal. Si tienes sugerencias o mejoras:

1. Abre un **Issue** para discutir cambios
2. Haz un **Fork** del repositorio
3. Envía un **Pull Request** con tus mejoras

---

**¡Éxitos en tu aprendizaje de análisis de datos aplicado a economía!** 📊🎓
