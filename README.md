# Enthalpy Gradients

Library for calculation of daily and hourly enthalpy gradients in buildings

## Installation

    pip install EnthalpyGradients
    
## Simple Example
Here's a simple example in Python:

```python
# SIMPLE EXAMPLE

# local variables
Temperature_base_C = 18.5
Relative_humidity_base_perc = 50

# Initialize class
eg = EnthalpyGradient(Temperature_base_C, Relative_humidity_base_perc)

# calculate enthalpy gradients for certain outdoor conditions for one year (8760 hours)
Temperature_outdoor_C = np.random.normal(22, 5, 8760)
Relative_humidity_outdoor_perc = np.random.normal(40, 10, 8760)

## daily enthalpy gradient for heating
how = 'daily'
type = 'heating'
deg_heating_kJ_kg_day = eg.enthalpy_gradient(Temperature_outdoor_C, Relative_humidity_outdoor_perc, type=type, how=how)
print("The daily enthalpy gradient for sensible heating is {}".format(deg_heating_kJ_kg_day))

## daily enthalpy gradient for cooling
how = 'daily'
type = 'cooling'
deg_cooling_kJ_kg_day = eg.enthalpy_gradient(Temperature_outdoor_C, Relative_humidity_outdoor_perc, type=type, how=how)
print("The daily enthalpy gradient for sensible cooling is {}".format(deg_cooling_kJ_kg_day))

## daily enthalpy gradient for heating
how = 'daily'
type = 'humidification'
deg_humidification_kJ_kg_day = eg.enthalpy_gradient(Temperature_outdoor_C, Relative_humidity_outdoor_perc, type=type, how=how)
print("The daily enthalpy gradient for latent heating (humidification) is {}".format(deg_humidification_kJ_kg_day))

## daily enthalpy gradient for heating
how = 'daily'
type = 'dehumidification'
deg_dehumidification_kJ_kg_day = eg.enthalpy_gradient(Temperature_outdoor_C, Relative_humidity_outdoor_perc, type=type, how=how)
print("The daily enthalpy gradient for latent cooling (dehumidification) is {}".format(deg_dehumidification_kJ_kg_day))

## total daily enthalpy gradient
## we can calculate it, or alternatively you can sum up the other 4 gradients (heating, cooling, dehum., and hum.
how = 'daily'
type = 'total'
deg_total_kJ_kg_day = eg.enthalpy_gradient(Temperature_outdoor_C, Relative_humidity_outdoor_perc, type=type, how=how)
print("The total daily enthalpy gradient is {}".format(deg_total_kJ_kg_day))
```

## Cite

J.A. Fonseca and A. Schlueter, Daily enthalpy gradients and the effects of climate change on the thermal 
energy demand of buildings in the United States, Appl. Energy, vol. 262, no. September 2019, p. 114458, 2020.
