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

from enthalpygradients.constants import ENTHALPY_TYPES, HOURS_OF_THE_DAY, ENTHALPY_HOW
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
