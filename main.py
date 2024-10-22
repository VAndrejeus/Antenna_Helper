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
# Wavelength frame
wavelength_radio_buttons_frame = Frame(window)
wavelength_radio_buttons_frame.grid(row=0, column=1)

# Wavelength radio buttons
wave_length_size = IntVar()
wave_length_size.set(1) # Set the default wavelength to Full
wave_length_full = ttk.Radiobutton(wavelength_radio_buttons_frame, text="Full", value=1, variable=wave_length_size)
wave_length_half = ttk.Radiobutton(wavelength_radio_buttons_frame, text="Half", value=2, variable=wave_length_size)
wave_length_quarter = ttk.Radiobutton(wavelength_radio_buttons_frame, text="Quarter", value=3, variable=wave_length_size)
wave_length_full.grid(column=0, row=0)
wave_length_half.grid(column=0, row=1)
wave_length_quarter.grid(column=0, row=2)


# Notebook that will have tabs for different antenna types
antenna_tabs = ttk.Notebook(tabs_base)
antenna_tabs.grid(column=0, row=0)


# Yagi tab
yagi_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(yagi_tab, text="Yagi Antenna")

freq_field_yagi = ttk.Entry(yagi_tab)  # Entry field for the frequency
freq_field_yagi.grid(column=0, row=0)

#Yagi Wavelength label
yagi_wl_label = ttk.Label(yagi_tab, text="Wavelength", foreground="purple", font=MEASUREMENT_FONT)
yagi_wl_label.grid(column=1, row=0)


calc_button_yagi = ttk.Button(yagi_tab, text="Calculate",
                              command=lambda: ac.calculate_yagi(freq_field_yagi.get(),
                                                                wave_length_size,
                                                                yagi_wl_label.config,
                                                                canvas_yagi,
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
canvas_yagi = Canvas(yagi_tab, width=450, height=180)
yagi_image = PhotoImage(file="Yagi_image.png")
image_yagi = canvas_yagi.create_image(225, 90, image=yagi_image)
# Yagi element lengths
length_reflector = canvas_yagi.create_text(420,100, text="0", fill="green", font=MEASUREMENT_FONT)
length_driven = canvas_yagi.create_text(330, 20, text="0", fill="green", font=MEASUREMENT_FONT)
length_director1 = canvas_yagi.create_text(250, 20, text="0", fill="green", font=MEASUREMENT_FONT)
length_director2 = canvas_yagi.create_text(165, 20, text="0", fill="green", font=MEASUREMENT_FONT)
length_director3 = canvas_yagi.create_text(85, 20, text="0", fill="green", font=MEASUREMENT_FONT)
# Distances between elements
d3_d2_distance = canvas_yagi.create_text(130,70, text="0", fill="green", font=MEASUREMENT_FONT)
d2_d1_distance = canvas_yagi.create_text(210,70, text="0", fill="green", font=MEASUREMENT_FONT)
d1_dr_distance = canvas_yagi.create_text(290, 70, text="0", fill="green", font=MEASUREMENT_FONT)
dr_re_distance = canvas_yagi.create_text(355, 70, text="0", fill="green", font=MEASUREMENT_FONT)
canvas_yagi.grid(column=0, row=2, columnspan=2)


# Moxon tab
moxon_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(moxon_tab, text="Moxon Antenna")

# Entries
freq_field_moxon = ttk.Entry(moxon_tab)  # Entry field for the frequency
freq_field_moxon.grid(column=0, row=0)
wire_diameter_field = ttk.Entry(moxon_tab) # Entry field for wire diameter
wire_diameter_field.grid(column=1, row=0)



# Moxon image
canvas_moxon = Canvas(moxon_tab, width=440, height=220)
moxon_image = PhotoImage(file="Moxon_image.png")
image_moxon = canvas_moxon.create_image(200, 110, image=moxon_image)
canvas_moxon.grid(column=0, row=2, columnspan=3)

# Moxon element lengths
a_element = canvas_moxon.create_text(60, 60, text="A:", fill="green", font=MEASUREMENT_FONT)
b_element = canvas_moxon.create_text(60, 80, text="B:", fill="green", font=MEASUREMENT_FONT)
c_element = canvas_moxon.create_text(60, 100, text="C:", fill="green", font=MEASUREMENT_FONT)
d_element = canvas_moxon.create_text(60, 120, text="D:", fill="green", font=MEASUREMENT_FONT)
e_element = canvas_moxon.create_text(60, 140, text="E:", fill="green", font=MEASUREMENT_FONT)

# Moxon Wavelength Label
moxon_wl_label = ttk.Label(moxon_tab, text="Wavelength", foreground="purple", font=MEASUREMENT_FONT)
moxon_wl_label.grid(column=2, row=0)

# Create Moxon calculate button
calc_button_moxon = ttk.Button(moxon_tab, text="Calculate",
                               command=lambda: ac.calculate_moxon(freq_field_moxon.get(),
                                                                  wire_diameter_field.get(),
                                                                  wave_length_size,
                                                                  moxon_wl_label.config,
                                                                  canvas_moxon,
                                                                  a_element,
                                                                  b_element,
                                                                  c_element,
                                                                  d_element,
                                                                  e_element
                                                                  ))
calc_button_moxon.grid(column=0, row=1)

# Dipole tab
dipole_tab = ttk.Frame(antenna_tabs)
antenna_tabs.add(dipole_tab, text="Dipole Antenna")

# Entry field for the frequency
freq_field_dipole = ttk.Entry(dipole_tab)
freq_field_dipole.grid(column=0, row=0)

#Dipole image
canvas_dipole = Canvas(dipole_tab, width=440, height=220)
dipole_image = PhotoImage(file="Dipole_image.png")
image_dipole = canvas_dipole.create_image(220, 110, image=dipole_image)
canvas_dipole.grid(row=2, column=0, columnspan=2)


#Dipole elements length
l_element = canvas_dipole.create_text(215, 10, text="0", fill="green", font=MEASUREMENT_FONT)
e_element_dipole = canvas_dipole.create_text(115, 50, text="0", fill="green", font=MEASUREMENT_FONT)

# Dipole Wavelength Label
dipole_wl_label = ttk.Label(dipole_tab, text="Wavelength", foreground="purple", font=MEASUREMENT_FONT)
dipole_wl_label.grid(column=1, row=0)


#Create Dipole calculate button
calc_button_dipole = ttk.Button(dipole_tab, text="Calculate",
                                command=lambda: ac.calculate_dipole(freq_field_dipole.get(),
                                                                    wave_length_size,
                                                                    dipole_wl_label.config,
                                                                    canvas_dipole,
                                                                    l_element,
                                                                    e_element_dipole))
calc_button_dipole.grid(column=0, row=1)

window.mainloop()
