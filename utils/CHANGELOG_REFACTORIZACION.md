# Changelog - Refactorización Matemáticas Financieras

## 📅 Fecha: 2024
## 🎯 Objetivo: Consolidar funciones redundantes priorizando numpy_financial

---

## ✨ Cambios Principales

### 1. **Función `net_present_value()` - CONSOLIDADA** ✅

#### Antes (2 funciones):
```python
# Versión manual
net_present_value(initial_investment, cash_flows, r, T, m)

# Versión simple
npv_simple(rate, cash_flows)
```

#### Ahora (1 función):
```python
net_present_value(rate, cash_flows, periods_per_year=1)
```

**Cambios de firma:**
- ✗ Eliminado: `initial_investment` como parámetro separado
- ✓ Nuevo: Primera posición del array `cash_flows` debe ser inversión inicial negativa
- ✓ Mejorado: `periods_per_year` reemplaza a `m` (más descriptivo)
- ✓ Añadido: Validaciones de entrada con mensajes de error claros
- ✓ Base: Usa `npf.npv()` internamente

**Ejemplos de migración:**
```python
# ANTES
npv = net_present_value(10000, [3000, 4000, 5000], 0.10, 3, 1)
npv = npv_simple(0.10, [-10000, 3000, 4000, 5000])

# AHORA
npv = net_present_value(0.10, [-10000, 3000, 4000, 5000])
npv = net_present_value(0.10, [-10000, 3000, 4000, 5000], periods_per_year=12)
```

---

### 2. **Función `internal_rate_of_return()` - CONSOLIDADA** ✅

#### Antes (2 funciones):
```python
# Versión manual (Newton-Raphson)
internal_rate_of_return(initial_investment, cash_flows, max_iter, precision)

# Versión simple
irr_simple(cash_flows)
```

#### Ahora (1 función con método seleccionable):
```python
internal_rate_of_return(cash_flows, method='numpy', max_iter=1000, precision=1e-6)
```

**Cambios de firma:**
- ✗ Eliminado: `initial_investment` como parámetro separado
- ✓ Nuevo: `method='numpy'` (default, rápido) o `method='newton'` (didáctico)
- ✓ Mejorado: Validaciones y manejo de errores robusto
- ✓ Flexible: Mantiene Newton-Raphson como opción para enseñanza

**Ejemplos de migración:**
```python
# ANTES
irr = internal_rate_of_return(10000, [3000, 4000, 5000])
irr = irr_simple([-10000, 3000, 4000, 5000])

# AHORA
irr = internal_rate_of_return([-10000, 3000, 4000, 5000])
irr = internal_rate_of_return([-10000, 3000, 4000, 5000], method='numpy')
irr = internal_rate_of_return([-10000, 3000, 4000, 5000], method='newton')
```

---

### 3. **Función `present_value()` - MEJORADA** ✅

#### Antes:
```python
present_value(rate, nper, pmt, fv=0)
```

#### Ahora:
```python
present_value(rate, nper, pmt, fv=0, when='end')
```

**Cambios:**
- ✓ Añadido: Parámetro `when='end'` o `when='begin'`
- ✓ Nuevo: Soporta anualidades ordinarias (pagos al final) y anticipadas (pagos al inicio)

**Ejemplos:**
```python
# Anualidad ordinaria (default)
pv = present_value(0.01, 36, 500)

# Anualidad anticipada
pv = present_value(0.01, 36, 500, when='begin')
```

---

### 4. **Función `profitability_index()` - ACTUALIZADA** ✅

#### Antes:
```python
profitability_index(initial_investment, cash_flows, r, T, m)
```

#### Ahora:
```python
profitability_index(rate, cash_flows, periods_per_year=1)
```

**Cambios:**
- ✓ Usa `net_present_value()` internamente (elimina código duplicado)
- ✓ Misma firma simplificada que NPV

---

### 5. **Función `payback_period()` - ACTUALIZADA** ✅

#### Antes:
```python
payback_period(initial_investment, cash_flows)
```

#### Ahora:
```python
payback_period(cash_flows)
```

**Cambios:**
- ✓ Extrae inversión inicial de `cash_flows[0]` (consistente con otras funciones)

---

## 🗑️ Funciones Eliminadas

### `npv_simple()` ❌
**Razón:** Redundante con `net_present_value()`

**Migración:**
```python
# ANTES
npv = npv_simple(0.10, [-10000, 3000, 4000, 5000])

# AHORA
npv = net_present_value(0.10, [-10000, 3000, 4000, 5000])
```

---

### `irr_simple()` ❌
**Razón:** Redundante con `internal_rate_of_return(method='numpy')`

**Migración:**
```python
# ANTES
irr = irr_simple([-10000, 3000, 4000, 5000])

# AHORA
irr = internal_rate_of_return([-10000, 3000, 4000, 5000])
# O explícitamente:
irr = internal_rate_of_return([-10000, 3000, 4000, 5000], method='numpy')
```

---

## 📊 Resumen de Cambios

| Función                      | Estado      | Cambios Principales                                    |
|------------------------------|-------------|--------------------------------------------------------|
| `net_present_value()`        | ✅ Refactorizada | Consolidada, usa numpy_financial, validaciones         |
| `npv_simple()`               | ❌ Eliminada | Usar `net_present_value()`                             |
| `internal_rate_of_return()`  | ✅ Refactorizada | Consolidada, método seleccionable, validaciones        |
| `irr_simple()`               | ❌ Eliminada | Usar `internal_rate_of_return(method='numpy')`         |
| `present_value()`            | ✅ Mejorada  | Añadido parámetro `when` para anualidades              |
| `profitability_index()`      | ✅ Actualizada | Usa NPV internamente                                   |
| `payback_period()`           | ✅ Actualizada | Firma simplificada                                     |

---

## 🎓 Beneficios Académicos

### Para Estudiantes:
1. **Interfaz consistente**: Todas las funciones de inversión usan formato `[inversión_negativa, flujo1, flujo2, ...]`
2. **Mejor documentación**: JSDoc completo con ejemplos
3. **Validaciones claras**: Mensajes de error descriptivos en español
4. **Flexibilidad didáctica**: Método Newton-Raphson disponible para aprendizaje

### Para Profesores:
1. **Código más limpio**: Menos redundancia, más mantenible
2. **numpy_financial como base**: Prioriza librerías estándar y bien probadas
3. **Opciones pedagógicas**: `method='newton'` para enseñar algoritmos iterativos
4. **Testing incluido**: `test_matematicas_financieras.py` actualizado

---

## 🔧 Cómo Actualizar Tu Código

### Paso 1: Buscar funciones eliminadas
```bash
# En VS Code: Buscar en todo el proyecto
Ctrl+Shift+F
Buscar: npv_simple|irr_simple
```

### Paso 2: Reemplazar con nuevas firmas
Ver ejemplos de migración arriba para cada función.

### Paso 3: Verificar tests
```bash
python utils/test_matematicas_financieras.py
```

---

## 📝 Notas de Compatibilidad

### ⚠️ Breaking Changes:
1. **`net_present_value()`**: Orden de parámetros cambió completamente
2. **`internal_rate_of_return()`**: Orden de parámetros cambió completamente
3. **Funciones eliminadas**: `npv_simple()`, `irr_simple()` ya no existen

### ✅ Compatibilidad mantenida:
- Todas las funciones de tasas de interés
- Funciones de valor futuro
- Funciones de pagos
- Función MIRR (sin cambios)
- Análisis Monte Carlo (sin cambios)

---

## 🚀 Próximas Mejoras (Futuro)

1. **Monte Carlo mejorado**:
   - Añadir distribuciones lognormal y triangular
   - Calcular VaR y CVaR automáticamente

2. **Análisis de sensibilidad mejorado**:
   - Vectorización completa
   - Gráficos interactivos

3. **Tests unitarios**:
   - Migrar a pytest
   - Cobertura de código al 100%

---

## 📚 Referencias

- **numpy_financial**: https://numpy.org/numpy-financial/
- **Convenciones financieras**: Excel/Google Sheets compatibility
- **Documentación**: Ver docstrings en `matematicas_financieras.py`

---

## ✍️ Autor
Refactorización realizada siguiendo principios DRY (Don't Repeat Yourself) y priorizando numpy_financial como base para cálculos financieros estándar.
