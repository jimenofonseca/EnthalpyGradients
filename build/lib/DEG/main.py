import numpy as np

from DEG.checks import check_array_length, check_lenght_two_array, check_valid_options_of_DEG_types
from DEG.constants import HOURS_OF_THE_DAY, AIR_DENSITY_DEFAULT_kgm3, COP_DEFAULT, STOREY_HEIGHT_DEFAULT_m, ACH_DEFAULT
from DEG.functions import calc_h_lat, calc_h_sen, calc_humidity_ratio


class DailyEnhtalpyGradient(object):
    """
      main class
    """

    def __init__(self, T_base_C: float, RH_base_C: float, patm_mbar=1013.25):
        self.T_base_C = T_base_C
        self.RH_base_C = RH_base_C
        self.patm_mbar = patm_mbar
        self.x_indoor_kgperkg = calc_humidity_ratio(RH_base_C, T_base_C, self.patm_mbar)
        self.H_latent_indoor_kjperkg = calc_h_lat(T_base_C, self.x_indoor_kgperkg)
        self.H_sensible_indoor_kjperkg = calc_h_sen(T_base_C)

    def calc_enthalpy_gradient_latent(self, T_out_C: np.array, RH_out_C: np.array, flag):

        check_array_length(T_out_C)
        check_array_length(RH_out_C)
        x_out_kgperkg = calc_humidity_ratio(RH_out_C, T_out_C, self.patm_mbar)
        H_latent_outdoor_kjperkg = calc_h_lat(T_out_C, x_out_kgperkg)
        AH_latent_kJperKg = H_latent_outdoor_kjperkg - self.H_latent_indoor_kjperkg

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
        H_sen_outdoor_kjperkg = calc_h_sen(T_out_C)
        AH_sensible_kJperKg = H_sen_outdoor_kjperkg - self.H_sensible_indoor_kjperkg
        if flag == 'cooling':
            if AH_sensible_kJperKg > 0.0:
                AH_sensible_kJperKg = abs(AH_sensible_kJperKg)
            else:
                AH_sensible_kJperKg = 0.0
        elif flag == 'heating':
            if AH_sensible_kJperKg > 0.0:
                AH_sensible_kJperKg = 0.0
            else:
                AH_sensible_kJperKg = abs(AH_sensible_kJperKg)

        return AH_sensible_kJperKg

    def humidification(self, T_out_C: np.array, RH_out_C: np.array):

        check_lenght_two_array(T_out_C, RH_out_C)
        check_array_length(T_out_C)
        check_array_length(RH_out_C)
        DEG_HUM_kJperKg = sum(
            np.vectorize(self.calc_enthalpy_gradient_latent)(T_out_C, RH_out_C, 'humidification')) / HOURS_OF_THE_DAY

        return DEG_HUM_kJperKg

    def dehumidification(self, T_out_C: np.array, RH_out_C: np.array):

        check_lenght_two_array(T_out_C, RH_out_C)
        check_array_length(T_out_C)
        check_array_length(RH_out_C)
        DEG_DEHUM_kJperKg = sum(np.vectorize(self.calc_enthalpy_gradient_latent)(T_out_C,
                                                                                 RH_out_C,
                                                                                 'dehumidification')) / HOURS_OF_THE_DAY

        return DEG_DEHUM_kJperKg

    def heating(self, T_out_C: np.array):

        check_array_length(T_out_C)
        DEG_HEATING_kJperKg = sum(np.vectorize(self.calc_enthalpy_gradient_sensible)(T_out_C,
                                                                                     'heating')) / HOURS_OF_THE_DAY

        return DEG_HEATING_kJperKg

    def cooling(self, T_out_C: np.array):

        check_array_length(T_out_C)
        DEG_COOLING_kJperKg = sum(np.vectorize(self.calc_enthalpy_gradient_sensible)(T_out_C,
                                                                                     'cooling')) / HOURS_OF_THE_DAY
        return DEG_COOLING_kJperKg

    def total(self, T_out_C: np.array, RH_out_C: np.array):

        DEG_TOTAL_kJperKg = (self.humidification(T_out_C, RH_out_C) +
                             self.dehumidification(T_out_C, RH_out_C) +
                             self.heating(T_out_C) +
                             self.cooling(T_out_C))
        return DEG_TOTAL_kJperKg

    def daily_enthalpy_gradient(self, T_out_C: np.array, RH_out_C: np.array, demand_name: str):

        check_valid_options_of_DEG_types(demand_name)
        if demand_name == 'heating':
            DEG_KJperkg = self.heating(T_out_C)
        elif demand_name == 'cooling':
            DEG_KJperkg = self.cooling(T_out_C)
        elif demand_name == 'humidification':
            DEG_KJperkg = self.humidification(T_out_C, RH_out_C)
        elif demand_name == 'dehumidification':
            DEG_KJperkg = self.dehumidification(T_out_C, RH_out_C)
        elif demand_name == 'total':
            DEG_KJperkg = self.total(T_out_C)

        return DEG_KJperkg

    def specific_thermal_consumption(self, T_out_C: np.array, RH_out_C: np.array, demand_name: str,
                                     ACH=ACH_DEFAULT,
                                     COP=COP_DEFAULT,
                                     air_density_kgm3=AIR_DENSITY_DEFAULT_kgm3,
                                     storey_height_m=STOREY_HEIGHT_DEFAULT_m):

        DEG_KJperkg = self.daily_enthalpy_gradient(T_out_C, RH_out_C, demand_name)
        specific_thermal_consumption_kWhm2yr = (storey_height_m * air_density_kgm3 * ACH *
                                                DEG_KJperkg * HOURS_OF_THE_DAY) / (COP * 3600)

        return specific_thermal_consumption_kWhm2yr
