# GitHub Copilot Instructions - Laboratorio de Datos FCE-UBA

## Project Overview
Educational repository for "Data Lab" course at Buenos Aires University Economics Faculty. Focus on data manipulation, analysis, and visualization for economic applications using Python and Jupyter notebooks.

## Architecture & Structure
```
sesiones/sesionN/           # Session-based learning modules
├── plan-de-estudio-*.md    # Learning objectives and structure
├── practica/               # Jupyter notebooks with exercises
├── lecturas/               # Reading materials
├── cuestionarios/          # Assessment questions
└── resumen/                # Session summaries
fuentes/                    # Reference materials and datasets
```

## Key Development Patterns

### Notebook Structure Convention
- **Header**: Always start with course title and session number in markdown
- **Step-by-step approach**: Use ✅ emoji markers for sequential steps
- **Bilingual comments**: Spanish explanations with English variable names
- **Import block**: Standard imports at the beginning:
  ```python
  import numpy as np           # para hacer operaciones matemáticas
  import pandas as pd          # para manejo de archivos de datos
  import matplotlib.pyplot as plt  # para hacer gráficos
  import seaborn as sns        # para hacer gráficos
  ```

### Data Analysis Workflow
1. **Matrix creation** → **DataFrame conversion** → **Visualization**
2. Use `np.array()` for initial data structures, then convert to pandas DataFrames with proper labels
3. Always include business context in variable names (`matriz_produccion`, `ventas_trimestrales`)
4. Follow pattern: create data → analyze → visualize → interpret economically

### Economic Modeling Approach
- **Function definition**: Start with mathematical formula in markdown
- **Parameter exploration**: Use variables for coefficients to demonstrate effects
- **Visual validation**: Every function must have corresponding plot
- **Real-world application**: Connect mathematical concepts to business scenarios (demand, cost, revenue, profit)

### Visualization Standards
- Use `plt.figure(figsize=(8,5))` for consistent sizing
- Include grid with `plt.grid(True)`
- Add axis lines: `plt.axhline(0, color='black', linewidth=0.5)`
- Spanish labels and titles for all plots
- Legend with function formula when applicable

### Data Sources
- Local CSV files in `practica/` directories (e.g., `datos.csv`)
- Web datasets via pandas (Carseats dataset pattern)
- Synthetic organizational data (production matrices, sales data)

## Academic Context Guidelines
- **Language**: All content in Latin American Spanish, comments explain concepts didactically
- **AI Response Language**: Always respond in Spanish when working on this codebase
- **Progression**: Build from basic matrix operations to complex economic modeling
- **Assessment integration**: Code should support 60+ question quizzes covering material
- **Practical focus**: Every mathematical concept needs organizational/business application

## File Naming Conventions
- Session plans: `plan-de-estudio-unidadN.md`
- Notebooks: `N_Descriptive_topic_name.ipynb` (numbered sequence)
- Data files: descriptive names in Spanish or English (`datos.csv`)

## Key Integration Points
- Notebooks reference datasets within same session directory
- Cross-session concepts build upon each other (session1 → session3)
- External data sources loaded via pandas with error handling
- Matplotlib/seaborn integration for consistent visualization themes

When working on this codebase:
- Maintain educational progression and Spanish explanations
- Follow the step-by-step methodology with emoji markers
- Ensure all mathematical concepts have economic interpretations
- Include both synthetic examples and real datasets
- Preserve the academic rigor while keeping practical applicability
