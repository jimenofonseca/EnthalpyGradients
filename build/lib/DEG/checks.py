from EnthalpyGradients.constants import ENTHALPY_TYPES

def check_array_length(array):
    x = len(array)
    if x % 24 != 0:
        raise ValueError("your data is not divisible by 24, we cannot calculate daily enthalpy gradients")


def check_lenght_two_array(array1, array2):
    x = len(array1)
    y = len(array2)
    if x != y:
        raise ValueError("your data does not have the same length, we cannot calculate daily enthalpy gradients")

def check_valid_options_of_DEG_types(demand_name):
    if demand_name not in ENTHALPY_TYPES:
        raise ValueError("valid options are {)".format(ENTHALPY_TYPES))
