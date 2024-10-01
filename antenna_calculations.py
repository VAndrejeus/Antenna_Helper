# Calculate Wavelength
def calculate_wavelength(freq):
    freq = int(freq)
    full_wl = 936 / freq
    half_wl = 468 / freq
    quart_wl = 234 / freq
    return full_wl, half_wl, quart_wl


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
def calculate_yagi(freq, wl_label_field, canvas, l_re, l_dr, l_d1, l_d2, l_d3, d_dr_re, d_d1_dr, d_d1_d2, d_d2_d3):
    wave_length = calculate_wavelength(freq)[0]
    wl_label_field(text=f"Full WL = {wave_length}")  # Display only Full Wl for now( 0 index o a tupple

    #Lengths of elements
    lengths = calculate_lengths(wave_length)
    canvas.itemconfig(l_re, text=f"{lengths[0]:.3f} ft")
    canvas.itemconfig(l_dr, text=f"{lengths[1]:.3f} ft")
    canvas.itemconfig(l_d1, text=f"{lengths[2]:.3f} ft")
    canvas.itemconfig(l_d2, text=f"{lengths[3]:.3f} ft")
    canvas.itemconfig(l_d3, text=f"{lengths[4]:.3f} ft")

    #Distance between elements
    distances = calculate_separation(wave_length)
    canvas.itemconfig(d_dr_re, text=f"{distances[0]:.3f} ft")
    canvas.itemconfig(d_d1_dr, text=f"{distances[1]:.3f} ft")
    canvas.itemconfig(d_d1_d2, text=f"{distances[2]:.3f} ft")
    canvas.itemconfig(d_d2_d3, text=f"{distances[3]:.3f} ft")




# ---------------------Moxon formula-------------------


def calculate_moxon():
    pass


# ---------------------Dipole formula-------------------


def calculate_dipole():
    pass
