'''
MIT License

Copyright (c) 2020 Jimeno A. Fonseca

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import numpy as np
from enthalpygradients import EnthalpyGradient


# SIMPLE EXAMPLE

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