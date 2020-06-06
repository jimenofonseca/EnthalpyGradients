# Enthalpy Gradients

Library for calculation of daily and hourly enthalpy gradients in buildings

## Installation

    pip install EnthalpyGradients
    
## Simple Example
Here's a simple example in Python:

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
how = 'daily'
type = 'total'
deg_total_kJ_kg_day = eg.enthalpy_gradient(Temperature_outdoor_C, Relative_humidity_outdoor_perc, type=type, how=how)
print("The total daily enthalpy gradient is {}".format(deg_total_kJ_kg_day))
```

The library offers much more functionality. Check the[`examples`](https://github.com/JIMENOFONSECA/EnthalpyGradients/tree/master/enthalpygradients/examples) 
folder to learn how to calculate enthalpy gradients at the hourly level, for heating, cooling, dehumidification, and humidification.

You can also check the examples folder for more information on how to calculate the specific thermal energy consumption
of a building using enthalpy gradients.


## Cite

J.A. Fonseca and A. Schlueter, Daily enthalpy gradients and the effects of climate change on the thermal 
energy demand of buildings in the United States, Appl. Energy, vol. 262, no. September 2019, p. 114458, 2020.
