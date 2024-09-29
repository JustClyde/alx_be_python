FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9) 
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5) 
def convert_to_celsius(fahrenheit): 
    celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR - 32 
    return celsius 
def convert_to_fahrenheit(celsius): 
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32 
    return fahrenheit 
def main(): 
    try: 
        temperature = float(input("Enter the temperature to convert: ")) 
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper() 
    if unit == 'C': 
        converted_temp = convert_to_fahrenheit(temperature) 
        print(f"{temperature}°C is {converted_temp}°F") 
    elif unit == 'F': 
        converted_temp = convert_to_celsius(temperature) 
        print(f"{temperature}°F is {converted_temp}°C") 
    else: 
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.") 
 
