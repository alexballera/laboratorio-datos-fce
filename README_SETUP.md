# Laboratorio de Datos FCE-UBA

Este es el repositorio educativo para el curso "Laboratorio de Datos" de la Facultad de Ciencias Económicas de la Universidad de Buenos Aires. El proyecto se enfoca en la manipulación, análisis y visualización de datos para aplicaciones económicas usando Python y Jupyter notebooks.

## Estructura del Proyecto

```
laboratorio-datos-fce/
├── sesiones/                    # Módulos de aprendizaje por sesión
│   ├── sesion1/                 # Introducción a Python para datos organizacionales
│   │   ├── plan-de-estudio-*.md
│   │   └── practica/            # Notebooks con ejercicios
│   ├── sesion2/                 # Manipulación y visualización de datos
│   │   ├── practica/
│   │   └── datos.csv           # Datos de ejemplo
│   └── sesion3/                 # Modelización de funciones económicas
├── fuentes/                     # Materiales de referencia y datasets
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                  # Archivos ignorados por git
└── README.md                   # Este archivo
```

## Tecnologías Utilizadas

- **Python 3.12+**: Lenguaje principal
- **NumPy**: Operaciones matemáticas y matriciales
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib**: Visualización básica
- **Seaborn**: Visualizaciones estadísticas avanzadas
- **Jupyter Lab/Notebook**: Entorno de desarrollo interactivo
- **SciPy**: Cálculos científicos
- **Scikit-learn**: Aprendizaje automático
- **Statsmodels**: Modelado estadístico

## Configuración del Entorno de Desarrollo

### Requisitos Previos

- Python 3.12 o superior
- Git

### Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd laboratorio-datos-fce
   ```

2. **Crear y activar el entorno virtual**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Linux/macOS
   # o en Windows: .venv\Scripts\activate
   ```

3. **Instalar las dependencias**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configurar Jupyter**:

   ```bash
   # Registrar el kernel del entorno virtual
   python -m ipykernel install --user --name=laboratorio-datos --display-name="Lab Datos FCE"
   ```

### Ejecutar Jupyter Lab

```bash
# Asegurarse de que el entorno virtual esté activado
source .venv/bin/activate
jupyter lab
```

## Metodología de Trabajo

### Convenciones de Notebooks

- **Estructura estándar**: Cada notebook comienza con título del curso y número de sesión
- **Progresión paso a paso**: Se usa el emoji ✅ para marcar pasos secuenciales
- **Comentarios bilingües**: Explicaciones en español con nombres de variables en inglés
- **Bloque de importaciones**: Imports estándar al inicio:

  ```python
  import numpy as np           # para operaciones matemáticas
  import pandas as pd          # para manejo de datos
  import matplotlib.pyplot as plt  # para gráficos
  import seaborn as sns        # para visualizaciones
  ```

### Flujo de Análisis de Datos

1. **Creación de matrices** → **Conversión a DataFrames** → **Visualización**
2. Usar `np.array()` para estructuras iniciales, luego convertir a pandas DataFrames
3. Incluir contexto económico en nombres de variables (`matriz_produccion`, `ventas_trimestrales`)
4. Patrón: crear datos → analizar → visualizar → interpretar económicamente

### Modelado Económico

- **Definición de funciones**: Comenzar con fórmula matemática en markdown
- **Exploración de parámetros**: Variables para coeficientes que demuestren efectos
- **Validación visual**: Cada función debe tener gráfico correspondiente
- **Aplicación práctica**: Conectar conceptos matemáticos con escenarios de negocio

## Estándares de Visualización

- Usar `plt.figure(figsize=(8,5))` para tamaño consistente
- Incluir grilla con `plt.grid(True)`
- Líneas de eje: `plt.axhline(0, color='black', linewidth=0.5)`
- Etiquetas y títulos en español
- Leyenda con fórmula de función cuando corresponda

## Fuentes de Datos

- Archivos CSV locales en directorios `practica/`
- Datasets web via pandas (patrón dataset Carseats)
- Datos organizacionales sintéticos (matrices de producción, datos de ventas)

## Contribuir

Este proyecto sigue las convenciones académicas:

- **Idioma**: Todo el contenido en español latinoamericano
- **Progresión**: Construcción desde operaciones matriciales básicas hasta modelado económico complejo
- **Enfoque práctico**: Cada concepto matemático necesita aplicación organizacional/empresarial

## Comandos Útiles

```bash
# Activar entorno virtual
source .venv/bin/activate

# Iniciar Jupyter Lab
jupyter lab

# Formatear código Python
black .

# Verificar estilo de código
flake8 .

# Desactivar entorno virtual
deactivate
```

## Archivos de Configuración

- `.gitignore`: Configurado para proyectos de ciencia de datos con Python
- `requirements.txt`: Todas las dependencias necesarias con versiones específicas
- `.venv/`: Entorno virtual (ignorado por git)

## Soporte

Para preguntas sobre el contenido académico o problemas técnicos, revisar:

1. Los notebooks de ejemplo en cada sesión
2. Los planes de estudio en formato markdown
3. Los datos de ejemplo incluidos

---

**Universidad de Buenos Aires - Facultad de Ciencias Económicas**
*Laboratorio de Datos*
