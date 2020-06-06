from EnthalpyGradients.constants import ENTHALPY_TYPES, HOURS_OF_THE_DAY, ENTHALPY_HOW
import numpy as np

def check_array_length(array: np.array):
    x = array.size
    if (x / HOURS_OF_THE_DAY).is_integer() == False:
        raise ValueError("your data is not divisible by 24, we cannot calculate daily enthalpy gradients")


def check_lenght_two_array(array1: np.array, array2: np.array):
    x = array1.size
    y = array2.size
    if x != y:
        raise ValueError("your data does not have the same length, we cannot calculate daily enthalpy gradients")

def check_valid_options_of_DEG_types(type):
    if type not in ENTHALPY_TYPES:
        raise ValueError("valid options are {}".format(ENTHALPY_TYPES))


def check_and_transform_to_array(array):
    if isinstance(array, list):
        return np.array(array)
    else:
        return array

def check_valid_options_of_gradient_how(how):
    if how not in ENTHALPY_TYPES:
        raise ValueError("valid options are {}".format(ENTHALPY_HOW))
