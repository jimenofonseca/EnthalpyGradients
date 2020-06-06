from enthalpygradients import EnthalpyGradient


c = EnthalpyGradient(18.5, 20)
r = c.enthalpy_gradient([23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34],
                          [23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34], 'total', 'hourly')
l = c.specific_thermal_consumption([23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34],
                          [23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34,23,34,34,34], 'dehumidification', 'hourly')

print(r, l)