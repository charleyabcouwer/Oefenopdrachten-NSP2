class Temperature:
    def __init__(self, temperature_celsius):
        
        self.temperature = temperature_celsius

    def to_celsius(self):

        C = self.temperature
        # print(f"De temperatuur in celsius is {self.temperature} graden Celsius.")
        return C

    def to_kelvin(self):
        K = self.temperature + 273.15
        # print(f"De temperatuur in kelvin is {K} K.")
        return K

    def to_fahrenheit(self):
        F = (self.temperature * 9/5) + 32
        # print(f"De temperatuur in Fahrenheit is {F} graden Fahrenheit.")
        return F

    def update_temperature(self, temperature_celsius):
        # update the stored temperature
        self.temperature = temperature_celsius
        

temperature = Temperature(37) # Instance

print(f"{temperature.temperature=}")
print(f"{temperature.to_celsius()=}")
print(f"{temperature.to_kelvin()=}")
print(f"{temperature.to_fahrenheit()=} \n")

temperature.update_temperature(21)

print(f"{temperature.to_celsius()=}")
print(f"{temperature.to_kelvin()=}")
print(f"{temperature.to_fahrenheit()=}")