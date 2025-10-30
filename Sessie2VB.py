# Ter voorbereiding van sessie 2 heb ik de volgende conversie code geschreven:


V_ref = 3.3   # Maximale spanning van de Arduino (VOlt)
ADC_max = 1023 # Maximale ACD waarde

# ADC naar spanning
def adc_naar_spanning(adc_waarde):
    spanning = (adc_waarde / ADC_max) * V_ref
    return spanning

# Spanning naar ADC
def spanning_naar_adc(spanning):
    adc_waarde = (spanning / V_ref) * ADC_max
    return round(adc_waarde)

adc_test = 700
spanning_test = 2.28

spanning = adc_naar_spanning(adc_test)
adc = spanning_naar_adc(spanning_test)

print(f"Spanning bij ADC={adc_test}: {spanning:} V.")
print(f"ADC waarde bij {spanning_test} V: {adc}.")

# Uitkomsten zijn ongeveer zoals verwacht maar nog dubbelchecken !!