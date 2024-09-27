# Calculate Wavelength
def calculate_wavelength(freq):
    freq = int(freq)
    full_wl = 936 / freq
    half_wl = 468 / freq
    quart_wl = 234 / freq
    return full_wl, half_wl, quart_wl


# Calculate Wavelengths
def calculate_lengths(wavelength):
    reflector = .495 * wavelength
    dipole_radiator = .473 * wavelength
    director1 = .440 * wavelength
    director2 = .435 * wavelength
    director3 = .430 * wavelength
    return reflector, dipole_radiator, director1, director2, director3


# Calculate Separation between elements
def calculate_separation(wavelength):
    re_dr = .125 * wavelength
    dr_d1 = .125 * wavelength
    d1_d2 = .250 * wavelength
    d2_d3 = .250 * wavelength
    return re_dr, dr_d1, d1_d2, d2_d3


# Main calculate Yagi function
def calculate_yagi(freq, label_field):
    result = calculate_wavelength(freq)
    label_field(text=f"Full WL = {result[0]}")  # Display only Full Wl for now( 0 index o a tupple


# ---------------------Moxon formula-------------------


def calculate_moxon():
    pass


# ---------------------Dipole formula-------------------


def calculate_dipole():
    pass
