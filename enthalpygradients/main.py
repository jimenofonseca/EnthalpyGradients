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

from enthalpygradients.checks import check_array_length, check_lenght_two_array, check_valid_options_of_DEG_types, \
    check_and_transform_to_array, check_valid_options_of_gradient_how
from enthalpygradients.constants import HOURS_OF_THE_DAY, AIR_DENSITY_DEFAULT_kgm3, COP_DEFAULT, \
    STOREY_HEIGHT_DEFAULT_m, \
    ACH_DEFAULT
from enthalpygradients.functions import calc_h_lat, calc_h_sen, calc_humidity_ratio


class EnthalpyGradient(object):
    """
      main class
    """

    def __init__(self, T_base_C: float, RH_base_C: float, patm_mbar=1013.25):
        self.T_base_C = T_base_C
        self.RH_base_C = RH_base_C
        self.patm_mbar = patm_mbar
        self.x_indoor_kg_kg = calc_humidity_ratio(RH_base_C, T_base_C, self.patm_mbar)
        self.H_latent_indoor_kJ_kg = calc_h_lat(T_base_C, self.x_indoor_kg_kg)
        self.H_sensible_indoor_kJ_kg = calc_h_sen(T_base_C)

    def calc_enthalpy_gradient_latent(self, T_out_C: np.array, RH_out_C: np.array, flag):

        x_out_kg_kg = calc_humidity_ratio(RH_out_C, T_out_C, self.patm_mbar)
        H_latent_outdoor_kJ_kg = calc_h_lat(T_out_C, x_out_kg_kg)
        AH_latent_kJperKg = H_latent_outdoor_kJ_kg - self.H_latent_indoor_kJ_kg

        if flag == 'humidification':
            if AH_latent_kJperKg > 0.0:
                return 0.0
            else:
                return abs(AH_latent_kJperKg)
        elif flag == 'dehumidification':
            if AH_latent_kJperKg < 0.0:
                return 0.0
            else:
                return abs(AH_latent_kJperKg)

    def calc_enthalpy_gradient_sensible(self, T_out_C: np.array, flag):

        # Cooling case
        H_sen_outdoor_kJ_kg = calc_h_sen(T_out_C)
        AH_sensible_kJ_kg = H_sen_outdoor_kJ_kg - self.H_sensible_indoor_kJ_kg
        if flag == 'cooling':
            if AH_sensible_kJ_kg > 0.0:
                AH_sensible_kJ_kg = abs(AH_sensible_kJ_kg)
            else:
                AH_sensible_kJ_kg = 0.0
        elif flag == 'heating':
            if AH_sensible_kJ_kg > 0.0:
                AH_sensible_kJ_kg = 0.0
            else:
                AH_sensible_kJ_kg = abs(AH_sensible_kJ_kg)

        return AH_sensible_kJ_kg

    def humidification(self, T_out_C: np.array, RH_out_C: np.array, how: str = 'daily'):

        check_lenght_two_array(T_out_C, RH_out_C)
        check_array_length(T_out_C)
        check_array_length(RH_out_C)
        enthalpy_gradient_kJ_kg = np.vectorize(self.calc_enthalpy_gradient_latent)(T_out_C, RH_out_C, 'humidification')

        if how == 'daily':
            enthalpy_gradient_kJ_kg = sum(enthalpy_gradient_kJ_kg) / HOURS_OF_THE_DAY

        return enthalpy_gradient_kJ_kg

    def dehumidification(self, T_out_C: np.array, RH_out_C: np.array, how: str = 'daily'):

        check_lenght_two_array(T_out_C, RH_out_C)
        check_array_length(T_out_C)
        check_array_length(RH_out_C)
        enthalpy_gradient_kJ_kg = np.vectorize(self.calc_enthalpy_gradient_latent)(T_out_C, RH_out_C,
                                                                                   'dehumidification')

        if how == 'daily':
            enthalpy_gradient_kJ_kg = sum(enthalpy_gradient_kJ_kg) / HOURS_OF_THE_DAY

        return enthalpy_gradient_kJ_kg

    def heating(self, T_out_C: np.array, how: str = 'daily'):

        check_array_length(T_out_C)
        enthalpy_gradient_kJ_kg = np.vectorize(self.calc_enthalpy_gradient_sensible)(T_out_C, 'heating')

        if how == 'daily':
            enthalpy_gradient_kJ_kg = sum(enthalpy_gradient_kJ_kg) / HOURS_OF_THE_DAY

        return enthalpy_gradient_kJ_kg

    def cooling(self, T_out_C: np.array, how: str = 'daily'):

        check_array_length(T_out_C)
        enthalpy_gradient_kJ_kg = np.vectorize(self.calc_enthalpy_gradient_sensible)(T_out_C, 'cooling')

        if how == 'daily':
            enthalpy_gradient_kJ_kg = sum(enthalpy_gradient_kJ_kg) / HOURS_OF_THE_DAY

        return enthalpy_gradient_kJ_kg

    def total(self, T_out_C: np.array, RH_out_C: np.array, how: str = 'daily'):

        enthalpy_gradient_kJ_kg = (self.humidification(T_out_C, RH_out_C, how) +
                                   self.dehumidification(T_out_C, RH_out_C, how) +
                                   self.heating(T_out_C, how) +
                                   self.cooling(T_out_C, how))
        return enthalpy_gradient_kJ_kg

    def enthalpy_gradient(self, T_out_C: np.array, RH_out_C: np.array, type: str = 'total', how: str = 'daily'):

        T_out_C = check_and_transform_to_array(T_out_C)
        RH_out_C = check_and_transform_to_array(RH_out_C)

        check_valid_options_of_gradient_how(type)
        check_valid_options_of_DEG_types(type)
        check_lenght_two_array(T_out_C, RH_out_C)
        check_array_length(T_out_C)
        check_array_length(RH_out_C)

        if type == 'heating':
            enthalpy_gradient_kJ_kg = self.heating(T_out_C, how)
        elif type == 'cooling':
            enthalpy_gradient_kJ_kg = self.cooling(T_out_C, how)
        elif type == 'humidification':
            enthalpy_gradient_kJ_kg = self.humidification(T_out_C, RH_out_C, how)
        elif type == 'dehumidification':
            enthalpy_gradient_kJ_kg = self.dehumidification(T_out_C, RH_out_C, how)
        elif type == 'total':
            enthalpy_gradient_kJ_kg = self.total(T_out_C, RH_out_C, how)

        return enthalpy_gradient_kJ_kg

    def specific_thermal_consumption(self,
                                     T_out_C: np.array,
                                     RH_out_C: np.array,
                                     type: str = 'total',
                                     how: str = 'daily',
                                     ACH=ACH_DEFAULT,
                                     COP=COP_DEFAULT,
                                     air_density_kgm3=AIR_DENSITY_DEFAULT_kgm3,
                                     storey_height_m=STOREY_HEIGHT_DEFAULT_m):

        T_out_C = check_and_transform_to_array(T_out_C)
        RH_out_C = check_and_transform_to_array(RH_out_C)
        enthalpy_gradient_kJ_kg = self.enthalpy_gradient(T_out_C, RH_out_C, type, how)

        if how == "daily":
            specific_thermal_consumption_kWhm2 = (storey_height_m *
                                                  air_density_kgm3 *
                                                  ACH *
                                                  enthalpy_gradient_kJ_kg
                                                  * HOURS_OF_THE_DAY) / (COP * 3600)
        else:
            specific_thermal_consumption_kWhm2 = (storey_height_m *
                                                  air_density_kgm3 *
                                                  ACH *
                                                  enthalpy_gradient_kJ_kg) / (COP * 3600)

        return specific_thermal_consumption_kWhm2
