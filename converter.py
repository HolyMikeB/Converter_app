class Converter:

    def __init__(self):
        pass

    def c_to_f(self, temp):
        converted_temp = round(temp * (9 / 5) + 32, 1)
        return converted_temp

    def f_to_c(self, temp):
        converted_temp = round((temp - 32) * (5 / 9), 1)
        return converted_temp

    def m_to_k(self, speed):
        converted_speed = round(speed * 1.61, 1)
        return converted_speed

    def k_to_m(self, speed):
        converted_speed = round(speed * 0.62, 1)
        return converted_speed

    def f_to_cm(self, height):
        converted_height = round(height * 2.54)
        return converted_height

    def cm_to_f(self, height):
        converted_height = round(height / 2.54)
        return converted_height

