from converter import Converter
from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

convert = Converter()


class UiWindow(ttkb.Window):

    def __init__(self):
        super().__init__(themename='superhero')
        self.title('Metric/Imperial Converter')
        self.geometry('600x350')
        self.config(padx=60, pady=75)

        self.title_label = ttkb.Label(text='Converter app', font=('Helvetica', 18))
        self.title_label.grid(row=0, column=1)

        self.instruction_label = ttkb.Label(text='Please select the unit of measure you want to convert.')
        self.instruction_label.config(padding=30)
        self.instruction_label.grid(row=1, column=1)

        self.reset_button = Button(text='Reset', command=self.reset, width=10)
        self.reset_button.grid(row=3, column=0)

        self.go_button = Button(text='Go', command=self.first_selection, width=10)
        self.go_button.grid(row=3, column=2)

        self.option_select = ttkb.Combobox(state='readonly',
                                     values=['Temperature', 'Speed', 'Distance', 'Height'])
        self.option_select.grid(row=2, column=1)
        self.option_select.current(0)

        self.entry_box1 = ttkb.Entry()
        self.entry_box2 = ttkb.Entry()

        self.feet_label = ttkb.Label(text='Feet: ')
        self.inch_label = ttkb.Label(text='Inches: ')

        self.result_label = ttkb.Label()

        self.unit = ''

    def reset(self):
        self.geometry('600x350')
        self.instruction_label.config(text='Please select the unit of measure you want to convert.')

        self.go_button.config(command=self.first_selection)
        self.go_button.grid(row=3, column=2)

        self.reset_button.grid(row=3, column=0)

        self.option_select.config(values=['Temperature', 'Speed', 'Distance', 'Height'])

        self.entry_box1.grid_forget()
        self.entry_box2.grid_forget()
        self.feet_label.grid_forget()
        self.inch_label.grid_forget()
        self.result_label.grid_forget()

        self.option_select.grid(row=2, column=1)
        self.option_select.current(0)

    def first_selection(self):
        choice = self.option_select.get()
        if choice == 'Temperature':
            self.temperature_select()
        elif choice == 'Speed':
            self.speed_select()
        elif choice == 'Distance':
            self.distance_select()
        else:
            self.height_select()

    # Update screen for initial choice
    def temperature_select(self):
        self.instruction_label.config(text='Are you converting from Metric to Imperial (Metric), '
                                           'or Imperial to Metric (Imperial)?')
        self.option_select.config(values=['Metric', 'Imperial'])
        self.go_button.config(command=self.temperature_selection)
        self.geometry('800x350')
        self.option_select.current(0)

    def speed_select(self):
        self.instruction_label.config(text='Are you converting from Metric to Imperial (Metric), '
                                           'or Imperial to Metric (Imperial)?')
        self.option_select.config(values=['Metric', 'Imperial'])
        self.go_button.config(command=self.speed_selection)
        self.geometry('800x350')
        self.option_select.current(0)

    def distance_select(self):
        self.instruction_label.config(text='Are you converting from Metric to Imperial (Metric), '
                                           'or Imperial to Metric (Imperial)?')
        self.option_select.config(values=['Metric', 'Imperial'])
        self.go_button.config(command=self.distance_selection)
        self.geometry('800x350')
        self.option_select.current(0)

    def height_select(self):
        self.instruction_label.config(text='Are you converting from Metric to Imperial (Metric), '
                                           'or Imperial to Metric (Imperial)?')
        self.option_select.config(values=['Metric', 'Imperial'])
        self.go_button.config(command=self.height_selection)
        self.geometry('800x350')
        self.option_select.current(0)

    # Update screen after choosing Metric or Imperial
    def temperature_selection(self):
        self.instruction_label.config(text='Please enter the temperature.')
        self.entry_box1.grid(row=2, column=1)
        self.option_select.grid_forget()
        self.go_button.config(command=self.calc_temp)
        self.geometry('500x350')
        self.unit = self.option_select.get()

    def speed_selection(self):
        self.instruction_label.config(text='Please enter the speed (only the number).')
        self.entry_box1.grid(row=2, column=1)
        self.option_select.grid_forget()
        self.go_button.config(command=self.calc_speed)
        self.geometry('550x350')
        self.unit = self.option_select.get()

    def distance_selection(self):
        self.instruction_label.config(text='Please enter the distance.')
        self.entry_box1.grid(row=2, column=1)
        self.option_select.grid_forget()
        self.go_button.config(command=self.calc_dist)
        self.geometry('475x350')
        self.unit = self.option_select.get()

    def height_selection(self):
        if self.option_select.get() == 'Imperial':
            self.instruction_label.config(text='Please enter the height.')
            self.entry_box1.grid(row=2, column=1)
            self.entry_box2.grid(row=3, column=1)
            self.inch_label.grid(row=3, column=0)
            self.feet_label.grid(row=2, column=0)
            self.reset_button.grid(row=4, column=0)
            self.go_button.grid(row=4, column=2)
            self.geometry('475x350')
        else:
            self.instruction_label.config(text='Please enter the height in centimeters.')
            self.entry_box1.grid(row=2, column=1)
            self.geometry('535x350')
        self.option_select.grid_forget()
        self.go_button.config(command=self.calc_height)

        self.unit = self.option_select.get()

    # Calculation methods
    def calc_temp(self):
        temp = float(self.entry_box1.get())
        if self.unit == 'Imperial':
            converted_temp = convert.f_to_c(temp)
            self.result_label.config(text=f'{converted_temp}°C')
            self.result_label.grid(row=4, column=1)
        else:
            converted_temp = convert.c_to_f(temp)
            self.result_label.config(text=f'{converted_temp}°F')
            self.result_label.grid(row=4, column=1)

    def calc_speed(self):
        speed = float(self.entry_box1.get())
        if self.unit == 'Imperial':
            converted_speed = convert.m_to_k(speed)
            self.result_label.config(text=f'~ {converted_speed}Km/h')
            self.result_label.grid(row=4, column=1)
        else:
            converted_speed = convert.k_to_m(speed)
            self.result_label.config(text=f'~ {converted_speed}Mph')
            self.result_label.grid(row=4, column=1)

    def calc_dist(self):
        distance = float(self.entry_box1.get())
        if self.unit == 'Imperial':
            converted_distance = convert.m_to_k(distance)
            self.result_label.config(text=f'~ {converted_distance} kilometers')
            self.result_label.grid(row=4, column=1)
        else:
            converted_distance = convert.k_to_m(distance)
            self.result_label.config(text=f'~ {converted_distance} miles')
            self.result_label.grid(row=4, column=1)

    def calc_height(self):
        if self.unit == 'Imperial':
            feet = int(self.entry_box1.get())
            inches = int(self.entry_box2.get())

            total_height = (feet * 12) + inches
            converted_cm = convert.f_to_cm(total_height)
            converted_m = converted_cm / 100

            self.result_label.config(text=f'{converted_cm} cm / {converted_m} meters')
            self.result_label.grid(row=5, column=1)
        else:
            height = float(self.entry_box1.get())

            converted_height = convert.cm_to_f(height)
            converted_in = converted_height % 12
            converted_feet = int((converted_height - converted_in) / 12)

            self.result_label.config(text=f'{converted_height} inches / {converted_feet}\'{converted_in}"')
            self.result_label.grid(row=5, column=1)
