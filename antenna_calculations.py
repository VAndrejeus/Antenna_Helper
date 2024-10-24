import math


# Calculate Wavelength
def calculate_wavelength(freq):
    freq = int(freq)
    # feet per second
    full_wl = 983 / freq
    half_wl = 491 / freq
    quart_wl = 245 / freq

    # inches per second
    full_wl_in = 11802.71 / freq
    half_wl_in = 5901.42/ freq
    quart_wl_in = 2950.71 / freq

    return full_wl, half_wl, quart_wl, full_wl_in, half_wl_in, quart_wl_in


# Calculate Wavelengths
def calculate_lengths(wavelength):
    reflector = 0.495 * wavelength
    dipole_radiator = 0.473 * wavelength
    director1 = 0.440 * wavelength
    director2 = 0.435 * wavelength
    director3 = 0.430 * wavelength
    return reflector, dipole_radiator, director1, director2, director3


# Calculate Separation between elements
def calculate_separation(wavelength):
    re_dr = 0.125 * wavelength
    dr_d1 = 0.125 * wavelength
    d1_d2 = 0.250 * wavelength
    d2_d3 = 0.250 * wavelength
    return re_dr, dr_d1, d1_d2, d2_d3


# Main calculate Yagi function
def calculate_yagi(freq, wave_length_size, wl_label_field, canvas_yagi, l_re, l_dr, l_d1, l_d2, l_d3, d_dr_re, d_d1_dr, d_d1_d2, d_d2_d3):
    radio_button_selected = wave_length_size.get()
    if radio_button_selected == 1:
        wave_length = calculate_wavelength(freq)[0]
        wl_label_field(text=f"Full WL = {wave_length:.2f} ft")
    elif radio_button_selected == 2:
        wave_length = calculate_wavelength(freq)[1]
        wl_label_field(text=f"Half WL = {wave_length:.2f} ft")
    elif radio_button_selected == 3:
        wave_length = calculate_wavelength(freq)[2]
        wl_label_field(text=f"Quarter WL = {wave_length:.2f} ft")


    #Lengths of elements
    lengths = calculate_lengths(wave_length)
    canvas_yagi.itemconfig(l_re, text=f"{lengths[0]:.2f} ft")
    canvas_yagi.itemconfig(l_dr, text=f"{lengths[1]:.2f} ft")
    canvas_yagi.itemconfig(l_d1, text=f"{lengths[2]:.2f} ft")
    canvas_yagi.itemconfig(l_d2, text=f"{lengths[3]:.2f} ft")
    canvas_yagi.itemconfig(l_d3, text=f"{lengths[4]:.2f} ft")

    #Distance between elements
    distances = calculate_separation(wave_length)
    canvas_yagi.itemconfig(d_dr_re, text=f"{distances[0]:.2f} ft")
    canvas_yagi.itemconfig(d_d1_dr, text=f"{distances[1]:.2f} ft")
    canvas_yagi.itemconfig(d_d1_d2, text=f"{distances[2]:.2f} ft")
    canvas_yagi.itemconfig(d_d2_d3, text=f"{distances[3]:.2f} ft")


# ---------------------Moxon formula-------------------
def calculate_moxon(freq, diam, wave_length_size, wl_label_field, canvas_moxon, l_a, l_b, l_c, l_d, l_e):
    radio_button_selected = wave_length_size.get()
    if radio_button_selected == 1:
        wave_length = calculate_wavelength(freq)[3]
        wl_label_field(text=f"Full WL = {wave_length:.2f} in")
    elif radio_button_selected == 2:
        wave_length = calculate_wavelength(freq)[4]
        wl_label_field(text=f"Half WL = {wave_length:.2f} in")
    elif radio_button_selected == 3:
        wave_length = calculate_wavelength(freq)[5]
        wl_label_field(text=f"Quarter WL = {wave_length:.2f} in")

    diam = int(diam)

    # Calculate wave_length from given diameter
    diameter_wavelength = diam / wave_length
    # d1 = encapsulation of the effect of the wire diameter on the antenna dimensions
    d1 = 0.4342945 / math.log(diameter_wavelength)

    # Calculating dimensions and converting values for display
    a = ((-0.0008571428571 * d1 * d1) + (-0.009571428571 * d1) + 0.3398571429) * wave_length
    b = ((0.001809523381 * d1 * d1) + (0.01780952381 * d1) + 0.05164285714) * wave_length
    c = ((-0.002142857143 * d1 * d1) + (-0.02035714286 * d1) + 0.008285714286) * wave_length
    d = ((0.001 * d1) + 0.07178571429) * wave_length
    e = b + c + d

    # Converting dimension to display in feet and inches
    length_a = a//12
    length_a_in = a % 12
    length_b = b//12
    length_b_in = b % 12
    length_c = c//12
    length_c_in = c % 12
    length_d = d//12
    length_d_in = d % 12
    length_e = e//12
    length_e_in = e % 12
    canvas_moxon.itemconfig(l_a, text=f"A:{length_a:.0f} ft {length_a_in:.1f} in")
    canvas_moxon.itemconfig(l_b, text=f"B:{length_b:.0f} ft {length_b_in:.1f} in")
    canvas_moxon.itemconfig(l_c, text=f"C:{length_c:.0f} ft {length_c_in:.1f} in")
    canvas_moxon.itemconfig(l_d, text=f"D:{length_d:.0f} ft {length_d_in:.1f} in")
    canvas_moxon.itemconfig(l_e, text=f"E:{length_e:.0f} ft {length_e_in:.1f} in")

# ---------------------Dipole formula-------------------


def calculate_dipole(freq, wave_length_size, wl_label_field, canvas_dipole, l_l, l_e):
    # Wavelength Radio buttons selection options
    radio_button_selected = wave_length_size.get()
    if radio_button_selected == 1:
        element_l = calculate_wavelength(freq)[0]
        wl_label_field(text=f"Full WL = {element_l:.2f} ft")
    elif radio_button_selected == 2:
        element_l = calculate_wavelength(freq)[1]
        wl_label_field(text=f"Half WL = {element_l:.2f} ft")
    elif radio_button_selected == 3:
        element_l = calculate_wavelength(freq)[2]
        wl_label_field(text=f"Quarter WL = {element_l:.2f} ft")
    element_e = element_l/2

    canvas_dipole.itemconfig(l_l, text=f"{element_l:.2f} ft ")
    canvas_dipole.itemconfig(l_e, text=f"{element_e:.2f} ft ")
