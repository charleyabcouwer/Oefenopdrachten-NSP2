class Temperature:
    def __init__(self, temperature_celsius):
        
        self.temperature = temperature_celsius

    def to_celsius(self):

        C = temperature
        
        # print(f"De temperatuur in celsius is {self.temperature} graden Celsius.")

    def to_kelvin(self):
        K = temperature + 273.15
        # print(f"De temperatuur in kelvin is {K} K.")

    def to_fahrenheit(self):
        F = temperature * 9/5 + 32
        # print(f"De temperatuur in Fahrenheit is {F} graden Fahrenheit.")

    def update_temperature(self, temperature_celsius):
        # update the stored temperature
        ...

temperature = Temperature(37) # Instance

print(f"{temperature.temperature=}")
print(f"{temperature.to_celsius()=}")
print(f"{temperature.to_kelvin()=}")
print(f"{temperature.to_fahrenheit()=}")
print()

temperature.update_temperature(21)
print(f"{temperature.to_celsius()=}")
print(f"{temperature.to_kelvin()=}")
print(f"{temperature.to_fahrenheit()=}")