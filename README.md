# Enthalpy Gradients

Library for calculation of daily and hourly enthalpy gradients in buildings. 

Enthalpy gradients can be used to estimate the specific thermal energy consumption of a building due to space heating, space cooling, humidification and dehumidification.


## How does it work

Enthalpy Gradients [`Fonseca et al., 2020`](https://doi.org/10.1016/j.apenergy.2019.114458) are defined as the difference in enthalpy between outdoor conditions of temperature and humidity and a desired or base state of indoor temperature and humidity in a building. This difference or gradient is equivalent to the amount of thermal energy needed to achieve a state of indoor thermal comfort. The concept of Enthalpy Gradients departs from the operation of buildings with air-conditioning. In these buildings, the difference in enthalpy between supply and exhaust air equals the thermal energy per unit of mass needed for heating, cooling, humidifying and dehumidifying air. Similar to the concept of Heating Degree Days, Daily Enthalpy Gradients depend on a base state (a fixed temperature and humidity in our case) known as a threshold below (or above) where thermal processes in buildings do not need to operate to satisfy a state of indoor thermal comfort. A robust formulation of Daily Enthalpy Gradients requires knowledge about heat gains (e.g., heat and moisture from people and appliances, solar radiation), heat losses (e.g., ventilation, infiltration) and building technology. Despite this, I suggest that an initial formulation of Enthalpy Gradients based on the fixed state of indoor comfort is useful in helping to understand the magnitude of thermal energy consumption in buildings.

As such, Enthalpy gradients can be used to estimate the specific thermal energy consumption of a building due to space heating, space cooling, humidification and dehumidification. Check the [`examples`](https://github.com/JIMENOFONSECA/EnthalpyGradients/tree/master/enthalpygradients/examples) 
folder for basic and advanced functionality

## Installation

    pip install EnthalpyGradients
    
## Simple Example
Here is a simple example in Python:

```python
import numpy as np
from enthalpygradients import EnthalpyGradient

# local variables
Temperature_base_C = 18.5
Relative_humidity_base_perc = 50

# Initialize class
eg = EnthalpyGradient(Temperature_base_C, Relative_humidity_base_perc)

# calculate enthalpy gradients for certain outdoor conditions for one year (8760 hours)
Temperature_outdoor_C = np.random.normal(22, 5, 8760)
Relative_humidity_outdoor_perc = np.random.normal(40, 10, 8760)

## total daily enthalpy gradient
deg_total_kJ_kg_day = eg.enthalpy_gradient(Temperature_outdoor_C, Relative_humidity_outdoor_perc)
print("The total daily enthalpy gradient is {}".format(deg_total_kJ_kg_day))

## total specific thermal energy consumption
q_total_kWh_m2 = eg.specific_thermal_consumption(Temperature_outdoor_C, Relative_humidity_outdoor_perc)
print("The specific thermal energy consumption is {} kWh/m2".format(q_total_kWh_m2))
```

The library offers much more functionality. Check the[`examples`](https://github.com/JIMENOFONSECA/EnthalpyGradients/tree/master/enthalpygradients/examples) 
folder to learn how to calculate enthalpy gradients at the hourly level, for heating, cooling, dehumidification, and humidification.

You can also check the examples folder for more information on how to calculate the specific thermal energy consumption
of a building using enthalpy gradients.


## Cite

J. A. Fonseca and A. Schlueter, Daily enthalpy gradients and the effects of climate change on the thermal 
energy demand of buildings in the United States, Appl. Energy, vol. 262, no. September 2019, p. 114458, 2020.
https://doi.org/10.1016/j.apenergy.2019.114458
