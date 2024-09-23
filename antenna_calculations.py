# ---------------------YAGI formula-------------------
'''         Lengths:
Reflector:       .495 * Wavelength =
Dipole Radiator: .473 * Wavelength =
Director 1:      .440 * Wavelength =
Director 2:      .435 * Wavelength =
Director 3:      .430 * Wavelength =


            Separation:
RE to DR:  .125 * Wavelength =
DR to D1:  .125 * Wavelength =
D1 to D2:  .250 * Wavelength =
D2 to D3:  .250 * Wavelength =


            Wavelength calculation:
Full WL = 936/Freq
1/2  WL = 468/Freq
1/4  WL = 234/Freq


'''


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


def calculate_yagi(freq, label_field):
    result = calculate_wavelength(freq)
    label_field(text=f"Full WL = {result[0]}")  # Display only Full Wl for now( 0 index o a tupple


# ---------------------Moxon formula-------------------


def calculate_moxon():
    pass


# ---------------------Dipole formula-------------------


def calculate_dipole():
    pass
