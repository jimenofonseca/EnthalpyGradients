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


# local variables
Temperature_base_C = 18.5
Relative_humidity_base_perc = 50
air_exchanges_per_hour = 4
ACH = 4
COP = 3.0
air_density_kgm3 = 1.03
storey_height_m = 3

# Initialize class
eg = EnthalpyGradient(Temperature_base_C, Relative_humidity_base_perc)

# calculate enthalpy gradients for certain outdoor conditions for one year (8760 hours)
Temperature_outdoor_C = np.random.normal(22, 5, 8760)
Relative_humidity_outdoor_perc = np.random.normal(40, 10, 8760)


## daily enthalpy gradient for heating
how = 'daily'
type = 'heating'
q_heating_kWh_m2 = eg.specific_thermal_consumption(Temperature_outdoor_C,
                                                        Relative_humidity_outdoor_perc,
                                                        type=type,
                                                        how=how,
                                                        ACH=ACH,
                                                        COP=COP,
                                                        air_density_kgm3=air_density_kgm3,
                                                        storey_height_m=storey_height_m)
print("The specific thermal energy consumption due to heating is {} kWh/m2".format(q_heating_kWh_m2))

## specific themal energy consumption due to cooling
how = 'daily'
type = 'cooling'
q_cooling_kWh_m2 = eg.specific_thermal_consumption(Temperature_outdoor_C,
                                                        Relative_humidity_outdoor_perc,
                                                        type=type,
                                                        how=how,
                                                        ACH=ACH,
                                                        COP=COP,
                                                        air_density_kgm3=air_density_kgm3,
                                                        storey_height_m=storey_height_m)
print("The specific thermal energy consumption due to cooling is {} kWh/m2".format(q_cooling_kWh_m2))

## daily enthalpy gradient for heating
how = 'daily'
type = 'humidification'
q_hum_kWh_m2 = eg.specific_thermal_consumption(Temperature_outdoor_C,
                                               Relative_humidity_outdoor_perc,
                                               type=type,
                                               how=how,
                                               ACH=ACH,
                                               COP=COP,
                                               air_density_kgm3=air_density_kgm3,
                                               storey_height_m=storey_height_m)
print("The specific thermal energy consumption due to humidification is {} kWh/m2".format(q_hum_kWh_m2))

## daily enthalpy gradient for heating
how = 'daily'
type = 'dehumidification'
q_dehum_kWh_m2 = eg.specific_thermal_consumption(Temperature_outdoor_C,
                                                 Relative_humidity_outdoor_perc,
                                                 type=type,
                                                 how=how,
                                                 ACH=ACH,
                                                 COP=COP,
                                                 air_density_kgm3=air_density_kgm3,
                                                 storey_height_m=storey_height_m)
print("The specific thermal energy consumption due to dehumidification is {} kWh/m2".format(q_dehum_kWh_m2))

## total daily enthalpy gradient
## we can calculate it, or alternatively you can sum up the other 4 gradients (heating, cooling, dehum., and hum.
how = 'daily'
type = 'total'
q_total_kWh_m2 = eg.specific_thermal_consumption(Temperature_outdoor_C,
                                                 Relative_humidity_outdoor_perc,
                                                 type=type,
                                                 how=how,
                                                 ACH=ACH,
                                                 COP=COP,
                                                 air_density_kgm3=air_density_kgm3,
                                                 storey_height_m=storey_height_m)
print("The specific thermal energy consumption is {} kWh/m2".format(q_total_kWh_m2))