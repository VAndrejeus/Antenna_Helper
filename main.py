# Main program file that creates the windows and all of the elements
from tkinter import *
from tkinter import ttk
import antenna_calculations as ac

# Define the main window
window = Tk()
window.title("Antenna Helper")
window.minsize(width=300, height=300)

# Main variables
MEASUREMENT_FONT = ("Times New Roman", 12, "bold") # Dimensions font constant variable


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

freq_field_yagi = ttk.Entry(yagi_tab, )  # Entry field for the frequency
freq_field_yagi.grid(column=0, row=0)


yagi_wl_label = ttk.Label(yagi_tab, text="Wavelength", foreground="purple", font=MEASUREMENT_FONT) #Yagi Wavelength label
yagi_wl_label.grid(column=1, row=0)

calc_button_yagi = ttk.Button(yagi_tab, text="Calculate",
                              command=lambda: ac.calculate_yagi(freq_field_yagi.get(),
                                                                yagi_wl_label.config,
                                                                canvas,
                                                                length_reflector,
                                                                length_driven,
                                                                length_director1,
                                                                length_director2,
                                                                length_director3,
                                                                d3_d2_distance,
                                                                d2_d1_distance,
                                                                d1_dr_distance,
                                                                dr_re_distance
                                                                ))
calc_button_yagi.grid(column=0, row=1)
# Yagi Image
canvas = Canvas(yagi_tab, width=450, height=180)
yagi_image = PhotoImage(file="Yagi_image.png")
image = canvas.create_image(225, 90, image=yagi_image)
# Element lengths
length_reflector = canvas.create_text(420,100, text="0", fill="green", font=MEASUREMENT_FONT)
length_driven = canvas.create_text(330, 20, text="0", fill="green", font=MEASUREMENT_FONT)
length_director1 = canvas.create_text(245, 20, text="0", fill="green", font=MEASUREMENT_FONT)
length_director2 = canvas.create_text(165, 20, text="0", fill="green", font=MEASUREMENT_FONT)
length_director3 = canvas.create_text(80, 20, text="0", fill="green", font=MEASUREMENT_FONT)
# Distances between elements
d3_d2_distance = canvas.create_text(120,70, text="0", fill="green", font=MEASUREMENT_FONT)
d2_d1_distance = canvas.create_text(205,70, text="0", fill="green", font=MEASUREMENT_FONT)
d1_dr_distance = canvas.create_text(290, 70, text="0", fill="green", font=MEASUREMENT_FONT)
dr_re_distance = canvas.create_text(355, 70, text="0", fill="green", font=MEASUREMENT_FONT)
canvas.grid(column=0, row=2, columnspan=2)


# Moxon tab
moxon_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(moxon_tab, text="Moxon Antenna")

freq_field_moxon = ttk.Entry(moxon_tab)  # Entry field for the frequency
freq_field_moxon.grid(column=0, row=0)

calc_button_moxon = ttk.Button(moxon_tab, text="Calculate",
                               command=ac.calculate_moxon())  # Create Moxon calculate button
calc_button_moxon.grid(column=0, row=1)

# Dipole tab
dipole_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(dipole_tab, text="Dipole Antenna")

freq_field_dipole = ttk.Entry(dipole_tab)  # Entry field for the frequency
freq_field_dipole.grid(column=0, row=0)

calc_button_dipole = ttk.Button(dipole_tab, text="Calculate",
                                command=ac.calculate_dipole())  #Create Dipole calculate button
calc_button_dipole.grid(column=0, row=1)

window.mainloop()
