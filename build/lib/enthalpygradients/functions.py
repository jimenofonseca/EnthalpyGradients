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

from enthalpygradients.constants import CPW_kJ_kgC, h_we_kJ_kg, CPA_kJ_kgC


def calc_humidity_ratio(rh_percent, dry_bulb_C, patm_mbar):
    """
    convert relative humidity to moisture content
    Based on https://www.vaisala.com/sites/default/files/documents/Humidity_Conversion_Formulas_B210973EN.pdf
    """
    patm_hPa = patm_mbar

    A, m, Tn = get_phycometric_constants(dry_bulb_C)
    T_dry = dry_bulb_C

    p_ws_hPa = A * 10 ** ((m * T_dry) / (T_dry + Tn))
    p_w_hPa = p_ws_hPa * rh_percent / 100
    B_kgperkg = 0.6219907
    x_kgperkg = B_kgperkg * p_w_hPa / (patm_hPa - p_w_hPa)
    return x_kgperkg


def calc_h_sen(dry_bulb_C):
    """
    Calc specific temperature of moist air (sensible)
    """

    h_kJ_kg = dry_bulb_C * CPA_kJ_kgC

    return h_kJ_kg


def calc_h_lat(dry_bulb_C, humidity_ratio_out_kgperkg):
    """
    Calc specific temperature of moist air (latent)

    :param temperatures_out_C:
    :param CPA:
    :return:
    """

    h_kJ_kg = humidity_ratio_out_kgperkg * (dry_bulb_C * CPW_kJ_kgC + h_we_kJ_kg)

    return h_kJ_kg


def get_phycometric_constants(T_C):
    if -20 <= T_C <= 50:
        m = 7.591386
        Tn = 240.7263
        A = 6.116441
    elif -70 <= T_C <= 0:
        m = 9.778707
        Tn = 273.1466
        A = 6.114742
    else:
        raise ValueError("The temperature indicated is out of bounds (-70, 50) degrees celsius")

    return A, m, Tn
