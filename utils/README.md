# 🧮 Utilidades de Matemáticas Financieras

Librería optimizada de funciones financieras para el Laboratorio TGAD (FCE-UBA).

---

## 📁 Contenido

```
utils/
├── matematicas_financieras.py      # Librería principal (refactorizada)
├── test_matematicas_financieras.py # Suite de pruebas
├── CHANGELOG_REFACTORIZACION.md    # Guía de migración detallada
└── README.md                        # Este archivo
```

---

## 🚀 Inicio Rápido

### Instalación
```python
# Las dependencias están en requirements.txt del proyecto principal
import numpy as np
import numpy_financial as npf
from utils.matematicas_financieras import *
```

### Ejemplo Básico
```python
# Evaluar un proyecto de inversión
cash_flows = [-100000, 30000, 40000, 50000]  # Inversión inicial negativa
tasa = 0.10  # 10% anual

# Valor Presente Neto
npv = net_present_value(tasa, cash_flows)
print(f"NPV: ${npv:,.2f}")

# Tasa Interna de Retorno
irr = internal_rate_of_return(cash_flows)
print(f"TIR: {irr:.2%}")

# Índice de Rentabilidad
pi = profitability_index(tasa, cash_flows)
print(f"PI: {pi:.3f}")
```

---

## 📚 Categorías de Funciones

### 1. Tasas de Interés
Conversiones entre tasas nominales, efectivas y anualizadas.

```python
# Tasa nominal a efectiva
tasa_mensual = nominal_to_effective_rate(0.12, 12)  # 1% mensual

# Tasa efectiva anual
tea = effective_annual_rate(0.12, 12)  # 12.68%

# Tasa anualizada
anual = annualized_rate(0.01, 12)  # 12.68%
```

---

### 2. Valor Temporal del Dinero
Cálculos de valor presente y futuro.

```python
# Valor presente de flujos futuros
pv = present_value(rate=0.01, nper=36, pmt=500)
# pv = -15044.39

# Anualidad anticipada (pagos al inicio)
pv_anticipada = present_value(rate=0.01, nper=36, pmt=500, when='begin')

# Valor futuro
fv = future_value(pv=10000, rate=0.005, nper=360)

# Vectorizado (múltiples escenarios)
tasas = np.array([0.08, 0.10, 0.12])
pvs = present_value(tasas, 10, 1000)
```

---

### 3. Anualidades
Cálculos especializados para pagos periódicos constantes.

```python
# Valor presente de anualidad
pv_annuity = present_value_annuity(C=1000, r=0.10, T=5, m=1)

# Valor futuro de anualidad
fv_annuity = future_value_annuity(C=1000, r=0.10, T=5, m=12)
```

---

### 4. Análisis de Préstamos
Cuotas, intereses y amortización.

```python
# Pago mensual de préstamo
pmt = payment_amount(rate=0.005, nper=360, pv=100000)
# pmt = 599.55

# Interés del primer pago
interest = payment_interest(rate=0.005, per=1, nper=360, pv=100000)

# Capital del primer pago
principal = payment_principal(rate=0.005, per=1, nper=360, pv=100000)

# Análisis completo de múltiples préstamos (vectorizado)
loans = np.array([100000, 150000, 200000])
pmts = payment_amount(rate=0.005, nper=360, pv=loans)
```

---

### 5. Evaluación de Inversiones ⭐

#### VPN (Valor Presente Neto)
```python
# Proyecto con inversión de $100k y flujos de $30k, $40k, $50k
cash_flows = [-100000, 30000, 40000, 50000]
npv = net_present_value(0.10, cash_flows)

# Con capitalización sub-anual
npv_mensual = net_present_value(0.12, cash_flows, periods_per_year=12)
```

#### TIR (Tasa Interna de Retorno)
```python
# Método numpy (rápido, recomendado)
irr = internal_rate_of_return(cash_flows)

# Método Newton-Raphson (didáctico)
irr_newton = internal_rate_of_return(cash_flows, method='newton')
```

#### TIRM (Tasa Interna de Retorno Modificada)
```python
# Considera tasas diferentes para financiamiento y reinversión
mirr = modified_internal_rate_of_return(
    cash_flows, 
    finance_rate=0.08,    # Costo de financiamiento
    reinvest_rate=0.12    # Tasa de reinversión
)
```

#### Índice de Rentabilidad
```python
pi = profitability_index(0.10, cash_flows)
# pi > 1: proyecto rentable
# pi < 1: proyecto no rentable
```

#### Período de Recuperación
```python
payback = payback_period(cash_flows)
# Retorna años hasta recuperar inversión inicial
```

---

### 6. Análisis Avanzado 🔬

#### Monte Carlo (Simulación de Riesgo)
```python
# Simular NPV con incertidumbre en flujos
results = monte_carlo_npv(
    initial_investment=100000,
    cash_flows_mean=[30000, 40000, 50000],
    cash_flows_std=[5000, 6000, 7000],
    discount_rate=0.10,
    simulations=10000
)

# Visualizar resultados
plot_monte_carlo_results(results)
```

#### Análisis de Sensibilidad
```python
# Ver cómo NPV varía con la tasa de descuento
rates = np.linspace(0.05, 0.20, 100)
npvs = sensitivity_analysis_npv(cash_flows, rates)

# Graficar
plt.plot(rates, npvs)
plt.xlabel('Tasa de Descuento')
plt.ylabel('NPV')
plt.grid(True)
```

---

## ✨ Características Principales

### 🎯 Priorización de numpy_financial
Todas las funciones principales usan `numpy_financial` bajo el capó para máxima precisión y compatibilidad con estándares financieros (Excel, Google Sheets).

### 🔢 Vectorización con NumPy
Soporta arrays para análisis de sensibilidad y evaluación de múltiples escenarios en paralelo.

```python
# Un solo cálculo
npv = net_present_value(0.10, [-10000, 3000, 4000, 5000])

# Múltiples escenarios simultáneos
tasas = np.array([0.08, 0.10, 0.12])
npvs = [net_present_value(r, [-10000, 3000, 4000, 5000]) for r in tasas]
```

### 📝 Documentación JSDoc
Todas las funciones incluyen:
- Descripción completa
- Parámetros tipados
- Ejemplos de uso
- Fórmulas matemáticas
- Notas importantes

### ✅ Validaciones Robustas
```python
# Mensaje de error claro si los datos son inválidos
try:
    npv = net_present_value(0.10, [3000])  # Faltan flujos
except ValueError as e:
    print(e)
    # "Se requieren al menos 2 flujos: inversión inicial y un flujo futuro"
```

### 🎓 Opciones Didácticas
```python
# Para enseñanza: usar Newton-Raphson explícito
irr = internal_rate_of_return(cash_flows, method='newton', max_iter=1000)

# Para producción: usar método optimizado
irr = internal_rate_of_return(cash_flows, method='numpy')
```

---

## 🧪 Testing

### Ejecutar Todas las Pruebas
```bash
# Desde la raíz del proyecto
python utils/test_matematicas_financieras.py
```

### Salida Esperada
```
==================================================
PRUEBAS DE TASAS DE INTERÉS
==================================================
Tasa nominal 12% anual, capitalización mensual → TEA: 1.00%
TEA con 12% nominal mensual: 12.68%

==================================================
PRUEBAS DE ANÁLISIS DE INVERSIONES
==================================================
NPV: $-210.37
IRR (método numpy): 8.90%
IRR (método Newton): 8.90%
MIRR: 9.82%
Índice de rentabilidad: 0.979

✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE
```

---

## 📖 Nomenclatura Estándar

Esta librería usa **nomenclatura en inglés** para las funciones (consistente con numpy_financial, Excel, Google Sheets), pero **documentación en español** para facilitar el aprendizaje.

| Español (Documentación) | Inglés (Nombre Función)      |
|-------------------------|------------------------------|
| Valor Presente Neto     | `net_present_value()`        |
| Tasa Interna de Retorno | `internal_rate_of_return()`  |
| Valor Presente          | `present_value()`            |
| Valor Futuro            | `future_value()`             |
| Pago                    | `payment_amount()`           |

---

## 🔄 Guía de Migración

Si estás actualizando código que usaba versiones anteriores de esta librería, consulta:

📄 **[CHANGELOG_REFACTORIZACION.md](CHANGELOG_REFACTORIZACION.md)**

Cambios principales:
- `npv_simple()` → `net_present_value()`
- `irr_simple()` → `internal_rate_of_return(method='numpy')`
- Firma de funciones de inversión consolidada: `cash_flows = [inversión_negativa, flujo1, ...]`

---

## 🐛 Problemas Comunes

### Error: "Se requieren al menos 2 flujos"
```python
# ❌ INCORRECTO
npv = net_present_value(0.10, [50000])

# ✅ CORRECTO
npv = net_present_value(0.10, [-10000, 50000])
```

### Error: "Tasa de descuento inválida"
```python
# ❌ INCORRECTO
npv = net_present_value(-1.5, cash_flows)  # Tasa < -100%

# ✅ CORRECTO
npv = net_present_value(0.10, cash_flows)
```

### Inversión inicial positiva
```python
# ❌ INCORRECTO
cash_flows = [10000, 3000, 4000]  # Inversión positiva

# ✅ CORRECTO
cash_flows = [-10000, 3000, 4000]  # Inversión negativa
```

---

## 📚 Referencias

- **numpy_financial**: https://numpy.org/numpy-financial/
- **Teoría financiera**: Brealey & Myers - Principles of Corporate Finance
- **Aplicaciones Excel**: Compatibilidad con NPV(), IRR(), PV(), FV(), PMT()

---

## 🤝 Contribuciones

Este es un proyecto académico para la Tecnicatura en Gestión y Análisis de Datos (FCE-UBA).

Para reportar bugs o sugerir mejoras:
1. Ejecutar `test_matematicas_financieras.py` para verificar el problema
2. Documentar el caso de uso específico
3. Contactar al equipo docente

---

## 📝 Licencia

Material académico de uso educativo para FCE-UBA.

---

## 🎓 Créditos

**Laboratorio TGAD - Facultad de Ciencias Económicas - Universidad de Buenos Aires**

Refactorización 2024: Priorización de numpy_financial y consolidación de funciones redundantes.
