# Main program file that creates the windows and all of the elements
from tkinter import *
from tkinter import ttk

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
# ---------------------Moxon formula-------------------

# ---------------------Dipole formula-------------------


# Define the main window
window = Tk()
window.title("Antenna Helper")
window.minsize(width=300,height=300)
# Main program elements

# Frame that will hold most of the tabs for different antennas
tabs_base = Frame(window)
tabs_base.grid(column=0, row=0)

# Notebook that will have tabs for different antenna types
antenna_tabs = ttk.Notebook(tabs_base)
antenna_tabs.grid(column=0, row=0)
# Yagi tab
yagi_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(yagi_tab, text="Yagi Antenna")
freq_field_yagi = ttk.Entry(yagi_tab)# Entry field for the frequency
freq_field_yagi.grid(column=0, row=0)
# Moxon tab
moxon_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(moxon_tab, text="Moxon Antenna")
freq_field_moxon = ttk.Entry(moxon_tab)# Entry field for the frequency
freq_field_moxon.grid(column=0, row=0)
# Dipole tab
dipole_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(dipole_tab, text="Dipole Antenna")
freq_field_dipole = ttk.Entry(dipole_tab)# Entry field for the frequency
freq_field_dipole.grid(column=0, row=0)


window.mainloop()




