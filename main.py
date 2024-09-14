# Main program file that creates the windows and all of the elements
from tkinter import *

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

label_yagi = Label(text="Yagi Antenna")
label_yagi.grid(column=0, row=1)

window.mainloop()




