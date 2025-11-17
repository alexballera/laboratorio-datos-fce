# %% [markdown]
# # Funciones de Matemáticas Financieras
# Nomenclatura estándar en inglés para cálculos financieros

# %% Importaciones
import numpy as np
import numpy_financial as npf
from typing import Optional, Union

# %% Funciones de Tasas de Interés

def nominal_to_effective_rate(r: float, m: int) -> float:
    """
    Convierte tasa nominal a tasa efectiva por período.
    
    @param {float} r - Tasa nominal anual
    @param {int} m - Períodos de capitalización por año
    @returns {float} Tasa efectiva por período
    
    @example
    >>> nominal_to_effective_rate(0.12, 12)  # 12% anual capitalización mensual
    0.01  # 1% mensual
    
    @formula
    Tasa efectiva = r / m
    
    @note
    - Convierte tasa anual a tasa por período de capitalización
    - Para 12% anual mensual: 0.12/12 = 0.01 (1% mensual)
    """
    return r / m

# %%

def effective_annual_rate(r: float, m: int) -> float:
    """
    Calcula la tasa efectiva anual a partir de la tasa nominal.
    
    @param {float} r - Tasa nominal anual
    @param {int} m - Períodos de capitalización por año
    @returns {float} Tasa efectiva anual
    
    @example
    >>> effective_annual_rate(0.12, 12)  # 12% anual capitalización mensual
    0.1268  # 12.68% efectiva anual
    
    @formula
    TEA = (1 + r/m)^m - 1
    
    @note
    - Considera el efecto de capitalización compuesta
    - Mayor frecuencia de capitalización = mayor TEA
    """
    return (1 + r / m) ** m - 1

# %%

def annualized_rate(r: float, m: int) -> float:
    """
    Convierte tasa periódica a tasa anualizada.
    
    @param {float} r - Tasa por período
    @param {int} m - Períodos por año
    @returns {float} Tasa anualizada
    
    @example
    >>> annualized_rate(0.02, 12)  # 2% mensual
    0.2682  # 26.82% anual
    
    @formula
    Tasa anualizada = (1 + r)^m - 1
    
    @note
    - Convierte tasa periódica a equivalente anual
    - Considera capitalización compuesta
    """
    return (1 + r) ** m - 1

# %% Funciones de Valor Presente y Futuro

def present_value(rate: Union[float, np.ndarray], 
                  nper: Union[int, np.ndarray], 
                  pmt: Union[float, np.ndarray], 
                  fv: Union[int, np.ndarray] = 0,
                  when: str = 'end') -> Union[float, np.ndarray]:
    """
    Calcula el valor presente usando numpy_financial.
    Soporta arrays para cálculos vectorizados.
    
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[int, np.ndarray]} nper - Número total de períodos
    @param {Union[float, np.ndarray]} pmt - Pago por período
    @param {Union[float, np.ndarray]} fv - Valor futuro (default 0)
    @param {str} when - 'end' (ordinaria) o 'begin' (anticipada)
    @returns {Union[float, np.ndarray]} Valor presente (negativo = salida de efectivo)
    
    @example
    >>> # Valor presente de 36 pagos de $500 al 1% mensual
    >>> pv = present_value(0.01, 36, 500)
    >>> pv
    -15044.39
    
    @example
    >>> # Anualidad anticipada (pagos al inicio)
    >>> pv_anticipada = present_value(0.01, 36, 500, when='begin')
    
    @example
    >>> # Vectorizado: múltiples tasas
    >>> rates = np.array([0.08, 0.10, 0.12])
    >>> pvs = present_value(rates, 10, 1000)
    >>> pvs
    array([-6710.08, -6144.57, -5650.22])
    
    @formula
    PV = npf.pv(rate, nper, pmt, fv, when)
    
    @note
    - Usa numpy_financial internamente para máxima precisión
    - Soporta arrays para análisis de sensibilidad
    - when='end' para anualidades ordinarias (pagos al final)
    - when='begin' para anualidades anticipadas (pagos al inicio)
    """
    when_code = 1 if when == 'begin' else 0
    result = -npf.pv(rate, nper, pmt, fv, when=when_code)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if np.isscalar(fv) and np.isscalar(rate) and np.isscalar(nper) and np.isscalar(pmt):
        return float(result)
    return result

# %%

def future_value(pv: Union[float, np.ndarray], rate: Union[float, np.ndarray], 
                nper: Union[float, np.ndarray] = 1, pmt: Union[float, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula el valor futuro de flujos presentes usando numpy_financial.
    
    @param {Union[float, np.ndarray]} pv - Valor presente o cash flows presentes
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[float, np.ndarray]} nper - Número de períodos de capitalización
    @param {Union[float, np.ndarray]} pmt - Pago periódico (por defecto 0)
    @returns {Union[float, np.ndarray]} Valor futuro
    
    @example
    >>> future_value(1000, 0.05, 10)  # $1000 a 10 períodos al 5%
    1628.89
    >>> future_value(1000, 0.08, 12)  # $1000 con capitalización mensual
    1083.00
    
    @formula
    FV = npf.fv(rate, nper, pmt, pv)
    
    @note
    - Usa numpy_financial internamente para máxima precisión
    - Soporta arrays para análisis de sensibilidad
    - Para capitalización personalizada usar rate = tasa_anual/períodos_por_año
    - Para ON usar nper = 12 (capitalización mensual en 1 año)
    """
    result = -npf.fv(rate, nper, pmt, -pv)
    
    # Si todos los inputs son escalares, retorna escalar
    if np.isscalar(pv) and np.isscalar(rate) and np.isscalar(nper) and np.isscalar(pmt):
        return float(result)
    return result

# %%

def present_value_annuity(C: float, r: float, T: Union[int, float], m: int = 1) -> float:
    """
    Calcula el valor presente de una anualidad con capitalización.
    
    @param {float} C - Cash flow periódico
    @param {float} r - Tasa de interés anual
    @param {Union[int, float]} T - Tiempo en años
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {float} Valor presente de la anualidad
    
    @example
    >>> present_value_annuity(100, 0.05, 10, 1)  # $100 anuales por 10 años al 5%
    772.17
    >>> present_value_annuity(100, 0.05, 10, 12)  # $100 mensuales por 10 años al 5%
    9420.45
    
    @formula
    PV = C * [1 - (1 + r/m)^(-m*T)] / (r/m)
    
    @note
    - Para anualidades ordinarias (pagos al final del período)
    - m=1 para capitalización anual, m=12 para mensual
    - Si r/m=0, usa fórmula simplificada PV = C * m * T
    """
    rate_per_period = r / m
    total_periods = m * T
    if rate_per_period == 0:
        return C * total_periods
    return C * (1 - (1 + rate_per_period) ** (-total_periods)) / rate_per_period

# %%

def future_value_annuity(C: float, r: float, T: Union[int, float], m: int = 1) -> float:
    """
    Calcula el valor futuro de una anualidad con capitalización.
    
    @param {float} C - Cash flow periódico
    @param {float} r - Tasa de interés anual
    @param {Union[int, float]} T - Tiempo en años
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {float} Valor futuro de la anualidad
    
    @example
    >>> future_value_annuity(100, 0.05, 10, 1)  # $100 anuales por 10 años al 5%
    1257.79
    >>> future_value_annuity(100, 0.05, 10, 12)  # $100 mensuales por 10 años al 5%
    15528.23
    
    @formula
    FV = C * [((1 + r/m)^(m*T) - 1) / (r/m)]
    
    @note
    - Para anualidades ordinarias (pagos al final del período)
    - m=1 para capitalización anual, m=12 para mensual
    - Si r/m=0, usa fórmula simplificada FV = C * m * T
    """
    rate_per_period = r / m
    total_periods = m * T
    if rate_per_period == 0:
        return C * total_periods
    return C * (((1 + rate_per_period) ** total_periods - 1) / rate_per_period)

# %% Funciones de Pagos

def payment_amount(rate: Union[float, np.ndarray], nper: Union[int, np.ndarray], 
                   pv: Union[float, np.ndarray], fv: Union[int, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula el monto del pago para un préstamo usando numpy_financial.
    
    @param {Union[float, np.ndarray]} pv - Monto del préstamo (valor presente)
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[int, np.ndarray]} nper - Número de períodos
    @param {Union[float, np.ndarray]} fv - Valor futuro (por defecto 0)
    @returns {Union[float, np.ndarray]} Monto del pago periódico
    
    @example
    >>> payment_amount(100000, 0.005, 360)  # Préstamo $100k a 30 años
    599.55  # Pago mensual
    >>> payment_amount([100000, 200000], [0.005, 0.006], [360, 240])  # Arrays
    array([599.55, 1438.06])  # Pagos para múltiples escenarios
    
    @formula
    PMT = npf.pmt(rate, nper, pv, fv)
    
    @note
    - Usa numpy_financial para cálculos de préstamos estándar
    - Soporta arrays para análisis comparativo de préstamos
    - Retorna valor positivo (pago que se hace)
    """
    result = -npf.pmt(rate, nper, pv, fv)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if np.isscalar(pv) and np.isscalar(rate) and np.isscalar(nper) and np.isscalar(fv):
        return float(result)
    return result

# %%

def payment_interest(rate: Union[float, np.ndarray], per: Union[int, np.ndarray], 
                    nper: Union[int, np.ndarray], pv: Union[float, np.ndarray], 
                    fv: Union[int, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula la porción de interés de un pago específico usando numpy_financial.
    
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[int, np.ndarray]} per - Período específico para calcular interés
    @param {Union[int, np.ndarray]} nper - Número total de períodos
    @param {Union[float, np.ndarray]} pv - Valor presente (monto del préstamo)
    @param {Union[float, np.ndarray]} fv - Valor futuro (por defecto 0)
    @returns {Union[float, np.ndarray]} Porción de interés del pago
    
    @example
    >>> payment_interest(0.005, 1, 360, 100000)  # Interés del primer pago
    500.00
    >>> payment_interest(0.005, [1, 2, 3], 360, 100000)  # Múltiples períodos
    array([500.00, 499.50, 499.00])
    
    @formula
    IPMT = npf.ipmt(rate, per, nper, pv, fv)
    
    @note
    - Usa numpy_financial para cálculos precisos de interés
    - Soporta arrays para análisis de amortización
    - Retorna valor positivo (interés que se paga)
    """
    result = -npf.ipmt(rate, per, nper, pv, fv)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(rate) and np.isscalar(per) and 
        np.isscalar(nper) and np.isscalar(pv) and np.isscalar(fv)):
        return float(result)
    return result

# %%

def payment_principal(rate: Union[float, np.ndarray], per: Union[int, np.ndarray], 
                     nper: Union[int, np.ndarray], pv: Union[float, np.ndarray], 
                     fv: Union[int, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula la porción de capital de un pago específico usando numpy_financial.
    
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[int, np.ndarray]} per - Período específico para calcular capital
    @param {Union[int, np.ndarray]} nper - Número total de períodos
    @param {Union[float, np.ndarray]} pv - Valor presente (monto del préstamo)
    @param {Union[float, np.ndarray]} fv - Valor futuro (por defecto 0)
    @returns {Union[float, np.ndarray]} Porción de capital del pago
    
    @example
    >>> payment_principal(0.005, 1, 360, 100000)  # Capital del primer pago
    233.33
    >>> payment_principal(0.005, [1, 2, 3], 360, 100000)  # Múltiples períodos
    array([233.33, 234.50, 235.67])
    
    @formula
    PPMT = npf.ppmt(rate, per, nper, pv, fv)
    
    @note
    - Usa numpy_financial para cálculos precisos de capital
    - Soporta arrays para análisis de amortización
    - Retorna valor positivo (capital que se paga)
    """
    result = -npf.ppmt(rate, per, nper, pv, fv)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(rate) and np.isscalar(per) and 
        np.isscalar(nper) and np.isscalar(pv) and np.isscalar(fv)):
        return float(result)
    return result# %% Funciones de Análisis de Inversiones

def net_present_value(rate: float, cash_flows: list, periods_per_year: int = 1) -> float:
    """
    Calcula el Valor Presente Neto (VPN) usando numpy_financial.
    
    @param {float} rate - Tasa de descuento anual
    @param {list} cash_flows - [inversión_inicial_negativa, flujo1, flujo2, ...]
    @param {int} periods_per_year - Períodos de capitalización por año (default 1)
    @returns {float} VPN de la inversión
    
    @example
    >>> # Inversión de $10,000 con flujos de $3,000, $4,000, $5,000
    >>> npv = net_present_value(0.10, [-10000, 3000, 4000, 5000])
    >>> npv
    -199.21
    
    @example
    >>> # Con capitalización mensual
    >>> npv = net_present_value(0.12, [-5000, 2000, 3000], periods_per_year=12)
    
    @formula
    NPV = npf.npv(rate, cash_flows)
    
    @note
    - Usa numpy_financial internamente para máxima precisión
    - Si periods_per_year > 1, ajusta la tasa efectiva por período
    - Primer flujo debe ser negativo (inversión inicial)
    """
    # Validaciones
    if not cash_flows or len(cash_flows) < 2:
        raise ValueError("Se requieren al menos 2 flujos: inversión inicial y un flujo futuro")
    
    if rate <= -1:
        raise ValueError(f"Tasa de descuento inválida: {rate}. Debe ser > -1 (o > -100%)")
    
    # Ajustar tasa si hay capitalización sub-anual
    if periods_per_year > 1:
        rate_per_period = rate / periods_per_year
        return npf.npv(rate_per_period, cash_flows)
    
    return npf.npv(rate, cash_flows)

# %%

def internal_rate_of_return(cash_flows: list, 
                           method: str = 'numpy',
                           max_iter: int = 1000,
                           precision: float = 1e-6) -> float:
    """
    Calcula la Tasa Interna de Retorno (TIR).
    
    @param {list} cash_flows - [inversión_inicial_negativa, flujo1, flujo2, ...]
    @param {str} method - 'numpy' (rápido, recomendado) o 'newton' (didáctico)
    @param {int} max_iter - Iteraciones máximas para método Newton (default 1000)
    @param {float} precision - Precisión para método Newton (default 1e-6)
    @returns {float} TIR de la inversión
    
    @example
    >>> # Método numpy (recomendado)
    >>> irr = internal_rate_of_return([-10000, 3000, 4000, 5000])
    >>> irr
    0.0634  # 6.34%
    
    @example
    >>> # Método Newton-Raphson (didáctico)
    >>> irr = internal_rate_of_return([-10000, 3000, 4000, 5000], method='newton')
    
    @formula
    Encuentra r donde NPV = Σ[CF_t / (1 + r)^t] = 0
    
    @note
    - El método 'numpy' usa scipy.optimize bajo el capó (más robusto)
    - El método 'newton' implementa Newton-Raphson explícito (académico)
    - IRR > tasa de descuento: inversión viable
    """
    # Validaciones
    if not cash_flows or len(cash_flows) < 2:
        raise ValueError("Se requieren al menos 2 flujos para calcular TIR")
    
    if method == 'numpy':
        return npf.irr(cash_flows)
    
    elif method == 'newton':
        # Método Newton-Raphson (implementación didáctica)
        initial_investment = abs(cash_flows[0])
        future_flows = cash_flows[1:]
        rate = 0.1  # Estimación inicial
        
        for _ in range(max_iter):
            npv = -initial_investment
            npv_derivative = 0
            
            for i, cf in enumerate(future_flows, 1):
                npv += cf / (1 + rate) ** i
                npv_derivative -= cf * i / (1 + rate) ** (i + 1)
            
            if abs(npv) < precision:
                return rate
            
            if npv_derivative == 0:
                raise ValueError("Derivada cero: no se puede continuar con Newton-Raphson")
            
            rate = rate - npv / npv_derivative
        
        raise ValueError(f"No convergió después de {max_iter} iteraciones")
    
    else:
        raise ValueError(f"Método '{method}' no soportado. Use 'numpy' o 'newton'")

# %%

def modified_internal_rate_of_return(cash_flows: list, finance_rate: float, reinvest_rate: float) -> float:
    """
    Calcula la Tasa Interna de Retorno Modificada (MIRR) usando numpy_financial.
    
    @param {list} cash_flows - Lista de flujos de caja (incluyendo inversión inicial negativa)
    @param {float} finance_rate - Tasa de financiamiento para flujos negativos
    @param {float} reinvest_rate - Tasa de reinversión para flujos positivos
    @returns {float} Tasa interna de retorno modificada
    
    @example
    >>> modified_internal_rate_of_return([-1000, 300, 400, 500], 0.10, 0.12)
    0.1013  # MIRR del 10.13%
    
    @formula
    MIRR = npf.mirr(cash_flows, finance_rate, reinvest_rate)
    
    @note
    - Usa numpy_financial para cálculos precisos
    - Considera diferentes tasas para financiamiento y reinversión
    - Más realista que IRR tradicional para proyectos complejos
    """
    return npf.mirr(cash_flows, finance_rate, reinvest_rate)

# %%

# Función eliminada: usar net_present_value() con periods_per_year=1

# %%

# Función eliminada: usar internal_rate_of_return() con method='numpy'

# %%

def profitability_index(rate: float, cash_flows: list, periods_per_year: int = 1) -> float:
    """
    Calcula el índice de rentabilidad (PI) usando NPV.
    
    @param {float} rate - Tasa de descuento anual
    @param {list} cash_flows - [inversión_inicial_negativa, flujo1, flujo2, ...]
    @param {int} periods_per_year - Períodos de capitalización por año (default 1)
    @returns {float} Índice de rentabilidad
    
    @example
    >>> profitability_index(0.10, [-10000, 3500, 4500, 5500])
    1.106  # PI > 1, proyecto viable
    >>> profitability_index(0.10, [-10000, 2500, 3000, 3500])
    0.751  # PI < 1, proyecto no viable
    
    @formula
    PI = (NPV + Inversión_Inicial) / Inversión_Inicial
    
    @note
    - PI > 1: proyecto viable (crea valor)
    - PI < 1: proyecto no viable (destruye valor)
    - PI = 1: proyecto indiferente (NPV = 0)
    - Usa net_present_value() internamente
    """
    initial_investment = abs(cash_flows[0])
    npv_result = net_present_value(rate, cash_flows, periods_per_year)
    return (npv_result + initial_investment) / initial_investment

# %%

def payback_period(cash_flows: list) -> float:
    """
    Calcula el período de recuperación de la inversión.
    
    @param {list} cash_flows - [inversión_inicial_negativa, flujo1, flujo2, ...]
    @returns {float} Período de recuperación en años
    
    @example
    >>> payback_period([-10000, 3000, 4000, 5000])
    2.75  # Se recupera en 2.75 años
    >>> payback_period([-8000, 2500, 3000, 4000])
    2.17  # Se recupera en 2.17 años
    
    @formula
    Período donde Σ(CF_t) >= 0 (con interpolación)
    
    @note
    - No considera valor temporal del dinero
    - Retorna float('inf') si nunca se recupera
    - Incluye interpolación para cálculo exacto
    """
    initial_investment = abs(cash_flows[0])
    cumulative_cash_flow = 0
    
    for i, cf in enumerate(cash_flows[1:], 0):
        cumulative_cash_flow += cf
        
        if cumulative_cash_flow >= initial_investment:
            # Interpolación para encontrar el momento exacto
            previous_cumulative = cumulative_cash_flow - cf
            fraction = (initial_investment - previous_cumulative) / cf
            return i + fraction
    
    # Si nunca se recupera la inversión
    return float('inf')

# %% Funciones Avanzadas de Análisis

def sensitivity_analysis_npv(initial_investment: float, cash_flows: list, 
                            r_range: np.ndarray, T: Optional[int] = None, m: int = 1) -> np.ndarray:
    """
    Análisis de sensibilidad del NPV variando la tasa de descuento.
    
    @param {float} initial_investment - Inversión inicial
    @param {list} cash_flows - Lista de flujos de caja futuros
    @param {np.ndarray} r_range - Array de tasas a analizar
    @param {Optional[int]} T - Número total de períodos (por defecto len(cash_flows))
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {np.ndarray} Array de valores NPV correspondientes
    
    @example
    >>> rates = np.linspace(0.05, 0.15, 11)
    >>> npvs = sensitivity_analysis_npv(10000, [3500, 4500, 5500], rates)
    >>> npvs.shape
    (11,)  # 11 valores NPV diferentes
    
    @formula
    NPV(r) = -Initial_Investment + Σ[CF_t / (1 + r/m)^(m*t)] para cada r
    
    @note
    - Útil para análisis de riesgo de tasa de interés
    - Permite visualizar sensibilidad del proyecto a cambios en r
    - Vectorización para eficiencia computacional
    """
    
    # Vectorizar el cálculo para todas las tasas
    npv_values = np.full(len(r_range), -initial_investment, dtype=float)
    
    for i, cf in enumerate(cash_flows):
        time_period = (i + 1) / m
        npv_values += cf / (1 + r_range/m) ** (m * time_period)
    
    return npv_values

# %%

def monte_carlo_npv(cash_flows: list, discount_rate_mean: float, volatility_flows: float,
                   volatility_rate: float, simulations: int = 1000) -> np.ndarray:
    """
    Simulación Monte Carlo simplificada para análisis de riesgo de NPV - Versión Académica.
    
    Esta función implementa una simulación Monte Carlo para evaluar el riesgo de inversión
    considerando la incertidumbre tanto en los flujos de caja como en la tasa de descuento.
    La simulación genera múltiples escenarios posibles y calcula el NPV para cada uno,
    proporcionando una distribución de resultados que permite cuantificar el riesgo.
    
    @param {list} cash_flows - Array de flujos de caja que incluye:
                              - Primer elemento: Inversión inicial (valor negativo)
                              - Elementos siguientes: Flujos de caja futuros esperados (valores positivos)
                              Ejemplo: [-10000, 3500, 4500, 5500] significa inversión de $10,000
                              y flujos futuros de $3,500, $4,500 y $5,500 en años 1, 2 y 3
    
    @param {float} discount_rate_mean - Tasa de descuento promedio (valor central esperado)
                                       Representa la tasa de retorno requerida para el proyecto
                                       Ejemplo: 0.10 significa 10% anual
    
    @param {float} volatility_flows - Volatilidad de los flujos de caja (desviación estándar relativa)
                                     Representa qué tan variables pueden ser los flujos respecto a su valor esperado
                                     Ejemplo: 0.15 significa que los flujos pueden variar ±15% de su valor base
    
    @param {float} volatility_rate - Volatilidad de la tasa de descuento (desviación estándar absoluta)
                                    Representa la incertidumbre en la tasa de descuento
                                    Ejemplo: 0.02 significa que la tasa puede variar ±2 puntos porcentuales
    
    @param {int} simulations - Número de simulaciones a realizar (por defecto 1000)
                              Mayor número = mayor precisión pero más tiempo de cálculo
                              1000 simulaciones suelen ser suficientes para análisis inicial
    
    @returns {np.ndarray} Array con resultados NPV de todas las simulaciones
                         Cada elemento representa el NPV calculado en una simulación específica
                         La distribución completa permite calcular:
                         - NPV promedio: np.mean(resultado)
                         - Riesgo (desviación): np.std(resultado)
                         - Probabilidad de éxito: np.sum(resultado >= 0) / len(resultado)
    
    @example
    Análisis de un proyecto de inversión en equipamiento:
    >>> # Proyecto: Inversión $100,000, flujos esperados $35,000, $45,000, $55,000
    >>> cash_flows = [-100000, 35000, 45000, 55000]
    >>> tasa_descuento = 0.10  # 10% anual
    >>> volatilidad_flujos = 0.20  # ±20% de variabilidad en flujos
    >>> volatilidad_tasa = 0.025   # ±2.5% de variabilidad en tasa
    >>> 
    >>> resultados = monte_carlo_npv(cash_flows, tasa_descuento, volatilidad_flujos, volatilidad_tasa, 1000)
    >>> 
    >>> # Análisis de resultados
    >>> npv_promedio = np.mean(resultados)      # NPV esperado: $8,456
    >>> riesgo = np.std(resultados)             # Desviación estándar: $15,234
    >>> prob_exito = np.mean(resultados >= 0)   # Probabilidad NPV ≥ 0: 72.3%
    >>> 
    >>> print(f"NPV Promedio: ${npv_promedio:,.0f}")
    >>> print(f"Riesgo (σ): ${riesgo:,.0f}")
    >>> print(f"Probabilidad de éxito: {prob_exito:.1%}")
    
    @formula
    Para cada simulación i:
    1. Generar tasa aleatoria: r_i ~ N(discount_rate_mean, volatility_rate²)
    2. Para cada flujo j: CF_j_i ~ N(cash_flows[j], (cash_flows[j] × volatility_flows)²)
    3. Calcular NPV_i = CF_0 + Σ[CF_j_i / (1 + r_i)^j] para j = 1 a n
    
    Distribución final: {NPV_1, NPV_2, ..., NPV_simulations}
    
    @methodology
    Método Monte Carlo:
    1. **Modelado de Incertidumbre**: Se asume que tanto los flujos de caja como la tasa de descuento
       siguen distribuciones normales, lo cual es razonable para muchos proyectos empresariales
    
    2. **Generación de Escenarios**: Se crean múltiples escenarios posibles combinando valores
       aleatorios de flujos y tasas, cada uno con su probabilidad de ocurrencia
    
    3. **Cálculo de NPV**: Para cada escenario se calcula el NPV usando la fórmula tradicional
       de valor presente neto con los valores específicos de ese escenario
    
    4. **Análisis Estadístico**: La distribución resultante permite calcular métricas de riesgo
       y probabilidades de éxito del proyecto
    
    @applications
    - **Evaluación de Proyectos**: Determinar viabilidad considerando riesgo e incertidumbre
    - **Análisis de Sensibilidad**: Entender cómo la variabilidad afecta los resultados
    - **Gestión de Riesgo**: Cuantificar probabilidades de pérdida o ganancia
    - **Toma de Decisiones**: Comparar proyectos considerando riesgo y retorno esperado
    
    @limitations
    - Asume distribuciones normales (puede no ser realista en algunos casos)
    - Los flujos se consideran independientes entre períodos
    - No considera correlaciones entre tasa de descuento y flujos de caja
    - La volatilidad se mantiene constante durante todo el período
    
    @note
    - **Reproducibilidad**: Usa semilla fija (seed=42) para resultados consistentes en análisis académico
    - **Eficiencia**: Implementación vectorizada usando NumPy para cálculos rápidos
    - **Robustez**: Incluye validación para evitar tasas de descuento negativas
    - **Interpretación**: Resultados positivos indican NPV favorable, negativos indican pérdida
    """    
    # ===================================================================================
    # PASO 1: CONFIGURACIÓN INICIAL Y VALIDACIÓN
    # ===================================================================================
    
    # Establecer semilla para reproducibilidad en análisis académico
    # Esto garantiza que las simulaciones den resultados consistentes entre ejecuciones
    np.random.seed(42)
    
    # Extraer inversión inicial (primer elemento, debe ser negativo)
    initial_investment = cash_flows[0]
    # Extraer flujos futuros (elementos restantes, deben ser positivos)
    future_cash_flows = cash_flows[1:]
    
    # ===================================================================================
    # PASO 2: GENERACIÓN DE VARIABLES ALEATORIAS
    # ===================================================================================
    
    # Generar tasas de descuento aleatorias siguiendo distribución normal
    # La tasa representa el costo de capital o retorno requerido del proyecto
    discount_rates = np.random.normal(discount_rate_mean, volatility_rate, simulations)
    
    # Asegurar que las tasas sean positivas (restricción económica lógica)
    # Se establece un mínimo de 0.1% para evitar problemas matemáticos
    discount_rates = np.maximum(discount_rates, 0.001)
    
    # Inicializar array de resultados NPV con la inversión inicial
    # Todos los NPV comenzarán con el valor negativo de la inversión
    npv_results = np.full(simulations, initial_investment, dtype=float)
    
    # ===================================================================================
    # PASO 3: SIMULACIÓN DE FLUJOS DE CAJA Y CÁLCULO DE NPV
    # ===================================================================================
    
    # Iterar sobre cada flujo de caja futuro (año 1, año 2, etc.)
    for period, expected_cash_flow in enumerate(future_cash_flows, start=1):
        
        # Calcular desviación estándar absoluta para este flujo específico
        # La volatilidad se expresa como porcentaje del flujo esperado
        cash_flow_std = abs(expected_cash_flow * volatility_flows)
        
        # Generar flujos de caja aleatorios para este período
        # Cada simulación tendrá un valor diferente para este flujo
        simulated_cash_flows = np.random.normal(expected_cash_flow, cash_flow_std, simulations)
        
        # Calcular valor presente de los flujos simulados para cada escenario
        # Fórmula: PV = CF / (1 + r)^t, donde t es el período
        present_values = simulated_cash_flows / (1 + discount_rates) ** period
        
        # Sumar el valor presente de este período al NPV acumulado
        # Cada simulación acumula el valor presente de todos sus flujos
        npv_results += present_values
    
    # ===================================================================================
    # PASO 4: RETORNO DE RESULTADOS
    # ===================================================================================
    
    # Retornar array completo con todos los NPV simulados
    # Cada elemento representa un escenario posible del proyecto
    return npv_results

# %%

def plot_monte_carlo_results(npv_results: np.ndarray, title: str = "Simulación Monte Carlo - Análisis de NPV") -> dict:
    """
    Genera visualización estilo SPSS para resultados de simulación Monte Carlo de NPV.
    
    Esta función crea un histograma profesional que muestra la distribución de NPV obtenida
    mediante simulación Monte Carlo, incluyendo análisis estadístico completo y probabilidades
    de éxito. El estilo visual emula las salidas de software estadístico profesional como SPSS.
    
    @param {np.ndarray} npv_results - Array con resultados de simulación Monte Carlo
                                     Debe contener valores NPV de múltiples simulaciones
                                     Típicamente obtenido de la función monte_carlo_npv()
    
    @param {str} title - Título personalizado para el gráfico (opcional)
                        Por defecto: "Simulación Monte Carlo - Análisis de NPV"
                        Permite personalizar según el proyecto específico
    
    @returns {dict} Diccionario con métricas estadísticas calculadas:
                   - 'npv_mean': NPV promedio de todas las simulaciones
                   - 'npv_std': Desviación estándar (medida de riesgo)
                   - 'success_probability': Probabilidad de NPV ≥ 0
                   - 'failure_probability': Probabilidad de NPV < 0
                   - 'percentile_5': Percentil 5 (peor escenario del 95% de casos)
                   - 'percentile_95': Percentil 95 (mejor escenario del 95% de casos)
                   - 'total_simulations': Número total de simulaciones realizadas
    
    @example
    Análisis completo de un proyecto de inversión:
    >>> # Ejecutar simulación Monte Carlo
    >>> cash_flows = [-100000, 35000, 45000, 55000]
    >>> resultados = monte_carlo_npv(cash_flows, 0.10, 0.20, 0.025, 1000)
    >>> 
    >>> # Generar visualización y obtener métricas
    >>> metricas = plot_monte_carlo_results(resultados, "Proyecto Expansión Industrial")
    >>> 
    >>> # Interpretar resultados
    >>> print(f"NPV Esperado: ${metricas['npv_mean']:,.0f}")
    >>> print(f"Riesgo (Desv. Std.): ${metricas['npv_std']:,.0f}")
    >>> print(f"Probabilidad de Éxito: {metricas['success_probability']:.1%}")
    >>> print(f"En el 90% de casos, NPV estará entre ${metricas['percentile_5']:,.0f} y ${metricas['percentile_95']:,.0f}")
    
    @visualization_features
    El gráfico incluye:
    1. **Histograma con Colores Diferenciados**:
       - Verde: NPV ≥ 0 (escenarios exitosos)
       - Rojo: NPV < 0 (escenarios de pérdida)
    
    2. **Líneas de Referencias**:
       - Línea vertical en NPV = 0 (punto de equilibrio)
       - Línea vertical en NPV promedio (resultado esperado)
    
    3. **Anotaciones Estadísticas**:
       - Probabilidad de éxito prominente
       - NPV promedio y desviación estándar
       - Rango de confianza (percentiles 5-95)
    
    4. **Formato Profesional**:
       - Grilla para facilitar lectura
       - Ejes claramente etiquetados en español
       - Colores profesionales y legibles
       - Leyenda explicativa
    
    @interpretation_guide
    **Cómo interpretar los resultados**:
    
    - **NPV Promedio > 0**: El proyecto es favorable en promedio
    - **Alta Probabilidad de Éxito (>70%)**: Proyecto con buen perfil riesgo-retorno
    - **Baja Desviación Estándar**: Menor riesgo, resultados más predecibles
    - **Amplio rango Percentil 5-95**: Mayor incertidumbre en resultados
    
    **Criterios de Decisión Sugeridos**:
    - Probabilidad éxito > 70% AND NPV promedio > 0: ACEPTAR proyecto
    - Probabilidad éxito 50-70% AND NPV promedio > 0: ANALIZAR más detalladamente
    - Probabilidad éxito < 50% OR NPV promedio < 0: RECHAZAR proyecto
    
    @statistical_methodology
    Las métricas calculadas utilizan:
    - **Media**: np.mean() - Valor esperado del NPV
    - **Desviación Estándar**: np.std() - Medida de riesgo/volatilidad
    - **Percentiles**: np.percentile() - Rango de resultados probable
    - **Probabilidad**: Conteo condicional / Total simulaciones
    
    @note
    - **Dependencias**: Requiere matplotlib.pyplot importado como plt
    - **Formato Salida**: Muestra el gráfico automáticamente con plt.show()
    - **Retorno**: Diccionario con métricas para análisis posterior
    - **Idioma**: Todas las etiquetas y texto en español académico
    """
    import matplotlib.pyplot as plt
    
    # ===================================================================================
    # CÁLCULO DE MÉTRICAS ESTADÍSTICAS
    # ===================================================================================
    
    # Métricas básicas de tendencia central y dispersión
    npv_mean = np.mean(npv_results)          # Valor esperado del NPV
    npv_std = np.std(npv_results)            # Riesgo medido como desviación estándar
    
    # Probabilidades de éxito y fracaso
    success_count = np.sum(npv_results >= 0)  # Número de NPV no negativos
    total_simulations = len(npv_results)      # Total de simulaciones
    success_probability = success_count / total_simulations
    failure_probability = 1 - success_probability
    
    # Percentiles para análisis de rango de resultados
    percentile_5 = np.percentile(npv_results, 5)    # Peor escenario típico
    percentile_95 = np.percentile(npv_results, 95)   # Mejor escenario típico
    
    # ===================================================================================
    # CONFIGURACIÓN DEL GRÁFICO ESTILO PROFESIONAL
    # ===================================================================================
    
    # Configurar figura con tamaño apropiado para análisis detallado
    plt.figure(figsize=(12, 8))
    
    # Determinar número óptimo de bins para el histograma
    # Regla de Sturges: número de bins ≈ log2(n) + 1, redondeado
    n_bins = min(50, max(20, int(np.log2(total_simulations)) + 1))
    
    # ===================================================================================
    # CREACIÓN DEL HISTOGRAMA CON COLORES DIFERENCIADOS
    # ===================================================================================
    
    # Separar datos en exitosos y no exitosos para coloreado diferencial
    success_data = npv_results[npv_results >= 0]    # NPV positivos o cero
    failure_data = npv_results[npv_results < 0]     # NPV negativos
    
    # Crear histograma con colores diferenciados y ancho de barras consistente
    # Verde para éxito, rojo para pérdidas
    # Usar rwidth para controlar el ancho de las barras (0.85 = 85% del espacio disponible)
    plt.hist(success_data, bins=n_bins, alpha=0.7, color='green', 
             label=f'NPV ≥ 0 ({success_probability:.1%})', edgecolor='darkgreen', 
             linewidth=0.5, rwidth=0.85)
    
    plt.hist(failure_data, bins=n_bins, alpha=0.7, color='red', 
             label=f'NPV < 0 ({failure_probability:.1%})', edgecolor='darkred', 
             linewidth=0.5, rwidth=0.85)
    
    # ===================================================================================
    # LÍNEAS DE REFERENCIA Y ANOTACIONES
    # ===================================================================================
    
    # Línea vertical en NPV = 0 (punto de equilibrio)
    plt.axvline(0, color='black', linestyle='--', linewidth=2, 
                label='Punto de Equilibrio (NPV = 0)')
    
    # Línea vertical en NPV promedio
    plt.axvline(float(npv_mean), color='blue', linestyle='-', linewidth=2, 
                label=f'NPV Promedio: ${npv_mean:,.0f}')
    
    # ===================================================================================
    # ETIQUETAS Y FORMATO DEL GRÁFICO
    # ===================================================================================
    
    # Títulos y etiquetas en español académico
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Valor Presente Neto (NPV) en $', fontsize=12, fontweight='bold')
    plt.ylabel('Frecuencia de Simulaciones', fontsize=12, fontweight='bold')
    
    # Configurar grilla para facilitar lectura
    plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Leyenda en posición óptima
    plt.legend(loc='upper left', fontsize=10, framealpha=0.9)
    
    # ===================================================================================
    # CAJA DE ESTADÍSTICAS DETALLADAS
    # ===================================================================================
    
    # Crear texto con métricas principales
    stats_text = f"""ANÁLISIS ESTADÍSTICO
    
NPV Promedio: ${npv_mean:,.0f}
Desviación Estándar: ${npv_std:,.0f}
    
ANÁLISIS DE RIESGO
Probabilidad de Éxito: {success_probability:.1%}
Probabilidad de Pérdida: {failure_probability:.1%}
    
RANGO DE CONFIANZA (90%)
Percentil 5%: ${percentile_5:,.0f}
Percentil 95%: ${percentile_95:,.0f}
    
Simulaciones: {total_simulations:,}"""
    
    # Posicionar caja de estadísticas en ubicación óptima
    plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
             fontsize=9, family='monospace')
    
    # ===================================================================================
    # AJUSTES FINALES Y VISUALIZACIÓN
    # ===================================================================================
    
    # Ajustar diseño para evitar superposiciones
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()
    
    # ===================================================================================
    # RETORNO DE MÉTRICAS PARA ANÁLISIS POSTERIOR
    # ===================================================================================
    
    return {
        'npv_mean': npv_mean,
        'npv_std': npv_std,
        'success_probability': success_probability,
        'failure_probability': failure_probability,
        'percentile_5': percentile_5,
        'percentile_95': percentile_95,
        'total_simulations': total_simulations
    }

# %%

def ejemplo_monte_carlo_completo():
    """
    Ejemplo académico completo de análisis Monte Carlo para evaluación de inversiones.
    
    Este ejemplo demuestra el uso integrado de las funciones monte_carlo_npv() y 
    plot_monte_carlo_results() para realizar un análisis completo de riesgo de inversión
    en un contexto empresarial típico de la carrera de Ciencias Económicas.
    
    @scenario
    **CASO DE ESTUDIO: Expansión de Línea de Producción**
    
    Una empresa manufacturera evalúa la inversión en una nueva línea de producción
    para ampliar su capacidad. El análisis considera la incertidumbre típica en:
    - Flujos de caja por variaciones en demanda y costos
    - Tasa de descuento por cambios en condiciones de mercado
    
    **Datos del Proyecto:**
    - Inversión Inicial: $500,000 (equipamiento y puesta en marcha)
    - Flujos Esperados: $180,000, $220,000, $280,000 (años 1, 2, 3)
    - Tasa de Descuento: 12% anual (costo promedio de capital)
    - Volatilidad Flujos: 25% (variabilidad por incertidumbre de mercado)
    - Volatilidad Tasa: 3% (variabilidad por condiciones económicas)
    
    @returns None - Imprime resultados y muestra gráfico
    
    @methodology
    1. **Definición de Parámetros**: Establecer valores base y niveles de incertidumbre
    2. **Simulación Monte Carlo**: Generar 1000 escenarios posibles
    3. **Análisis Estadístico**: Calcular métricas de riesgo y rentabilidad
    4. **Visualización**: Crear gráfico estilo SPSS con interpretación
    5. **Toma de Decisión**: Evaluar viabilidad basada en criterios establecidos
    
    @educational_objectives
    - Demostrar aplicación práctica de simulación Monte Carlo
    - Enseñar interpretación de resultados de análisis de riesgo
    - Mostrar integración de herramientas financieras y estadísticas
    - Desarrollar criterios de decisión empresarial bajo incertidumbre
    """
    
    print("="*70)
    print("ANÁLISIS MONTE CARLO - EVALUACIÓN DE PROYECTO DE INVERSIÓN")
    print("="*70)
    print()
    
    # ===================================================================================
    # DEFINICIÓN DE PARÁMETROS DEL PROYECTO
    # ===================================================================================
    
    print("📊 PARÁMETROS DEL PROYECTO")
    print("-" * 30)
    
    # Flujos de caja del proyecto (incluyendo inversión inicial como primer elemento)
    cash_flows = [-500000, 180000, 220000, 280000]
    
    print(f"• Inversión Inicial: ${abs(cash_flows[0]):,}")
    print("• Flujos Esperados:")
    for i, flujo in enumerate(cash_flows[1:], 1):
        print(f"  - Año {i}: ${flujo:,}")
    
    # Parámetros de incertidumbre
    discount_rate_mean = 0.12    # 12% costo de capital
    volatility_flows = 0.25      # 25% volatilidad en flujos
    volatility_rate = 0.03       # 3% volatilidad en tasa
    simulations = 1000           # Número de simulaciones
    
    print(f"\n• Tasa de Descuento Promedio: {discount_rate_mean:.1%}")
    print(f"• Volatilidad de Flujos: ±{volatility_flows:.1%}")
    print(f"• Volatilidad de Tasa: ±{volatility_rate:.1%}")
    print(f"• Número de Simulaciones: {simulations:,}")
    print()
    
    # ===================================================================================
    # EJECUCIÓN DE SIMULACIÓN MONTE CARLO
    # ===================================================================================
    
    print("🎯 EJECUTANDO SIMULACIÓN MONTE CARLO...")
    print("-" * 40)
    
    # Ejecutar simulación
    resultados = monte_carlo_npv(
        cash_flows=cash_flows,
        discount_rate_mean=discount_rate_mean,
        volatility_flows=volatility_flows,
        volatility_rate=volatility_rate,
        simulations=simulations
    )
    
    print(f"✅ Simulación completada: {len(resultados):,} escenarios generados")
    print()
    
    # ===================================================================================
    # ANÁLISIS ESTADÍSTICO DE RESULTADOS
    # ===================================================================================
    
    print("📈 RESULTADOS ESTADÍSTICOS")
    print("-" * 30)
    
    # Generar visualización y obtener métricas
    metricas = plot_monte_carlo_results(
        resultados, 
        "Proyecto Expansión Línea de Producción - Análisis Monte Carlo"
    )
    
    # Mostrar métricas principales
    print(f"• NPV Promedio: ${metricas['npv_mean']:,.0f}")
    print(f"• Riesgo (Desv. Std.): ${metricas['npv_std']:,.0f}")
    print(f"• Probabilidad de Éxito: {metricas['success_probability']:.1%}")
    print(f"• Probabilidad de Pérdida: {metricas['failure_probability']:.1%}")
    print()
    
    print("📊 RANGO DE CONFIANZA (90%)")
    print("-" * 30)
    print(f"• Escenario Pesimista (Percentil 5%): ${metricas['percentile_5']:,.0f}")
    print(f"• Escenario Optimista (Percentil 95%): ${metricas['percentile_95']:,.0f}")
    print(f"• Amplitud del Rango: ${metricas['percentile_95'] - metricas['percentile_5']:,.0f}")
    print()
    
    # ===================================================================================
    # INTERPRETACIÓN Y RECOMENDACIÓN
    # ===================================================================================
    
    print("🎯 INTERPRETACIÓN Y RECOMENDACIÓN")
    print("-" * 40)
    
    # Criterios de decisión
    npv_positivo = metricas['npv_mean'] > 0
    alta_probabilidad = metricas['success_probability'] > 0.70
    riesgo_aceptable = metricas['npv_std'] / abs(metricas['npv_mean']) < 1.5  # CV < 150%
    
    print("Criterios de Evaluación:")
    print(f"✓ NPV Promedio Positivo: {'SÍ' if npv_positivo else 'NO'}")
    print(f"✓ Probabilidad Éxito > 70%: {'SÍ' if alta_probabilidad else 'NO'}")
    print(f"✓ Riesgo Aceptable: {'SÍ' if riesgo_aceptable else 'NO'}")
    print()
    
    # Recomendación final
    if npv_positivo and alta_probabilidad:
        recomendacion = "🟢 ACEPTAR EL PROYECTO"
        justificacion = "El proyecto muestra NPV positivo con alta probabilidad de éxito"
    elif npv_positivo:
        recomendacion = "🟡 ANALIZAR MÁS DETALLADAMENTE"
        justificacion = "NPV positivo pero con riesgo significativo"
    else:
        recomendacion = "🔴 RECHAZAR EL PROYECTO" 
        justificacion = "NPV promedio negativo indica destrucción de valor"
    
    print(f"RECOMENDACIÓN: {recomendacion}")
    print(f"JUSTIFICACIÓN: {justificacion}")
    print()
    
    print("="*70)
    print("ANÁLISIS COMPLETADO")
    print("="*70)

# %%

def batch_loan_analysis(principals: np.ndarray, rates: np.ndarray, periods: np.ndarray) -> dict:
    """
    Análisis en lote de múltiples préstamos.
    
    @param {np.ndarray} principals - Array de montos de préstamos
    @param {np.ndarray} rates - Array de tasas de interés
    @param {np.ndarray} periods - Array de períodos
    @returns {dict} Diccionario con arrays de resultados
    
    @example
    >>> principals = np.array([100000, 200000, 300000])
    >>> rates = np.array([0.005, 0.006, 0.007])
    >>> periods = np.array([360, 240, 180])
    >>> results = batch_loan_analysis(principals, rates, periods)
    >>> results['payments']
    array([599.55, 1438.06, 2491.78])
    
    @formula
    Calcula PMT, IPMT, PPMT, Total pagado e Interés total para cada préstamo
    
    @note
    - Procesamiento vectorizado para eficiencia
    - Retorna métricas completas de análisis de préstamos
    - Útil para comparación de múltiples escenarios
    """
    # Calcular todas las métricas usando las funciones vectorizadas
    payments = payment_amount(principals, rates, periods)
    first_interest = payment_interest(principals, rates, 1, periods)
    first_principal = payment_principal(principals, rates, 1, periods)
    
    # Calcular total pagado y total de intereses
    total_paid = payments * periods
    total_interest = total_paid - principals
    
    return {
        'payments': payments,
        'first_interest': first_interest,
        'first_principal': first_principal,
        'total_paid': total_paid,
        'total_interest': total_interest,
        'interest_ratio': total_interest / principals  # Proporción de interés vs capital
    }
    first_principal = payment_principal(principals, rates, 1, periods)
    
    # Calcular total pagado y total de intereses
    total_paid = payments * periods
    total_interest = total_paid - principals
    
    return {
        'payments': payments,
        'first_interest': first_interest,
        'first_principal': first_principal,
        'total_paid': total_paid,
        'total_interest': total_interest,
        'interest_ratio': total_interest / principals  # Proporción de interés vs capital
    }
# %%
