
FAHRENHEIT_TO_CELSIUS_FACTOR\s*=\s*5\s*\/\s*9
CELSIUS_TO_FAHRENHEIT_FACTOR\s*=\s*9\/5
<h1>temp_conversion_tool.py</h1> 
<h1>Define global conversion factors</h1> 
FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9) 
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5) 
def convert_to_celsius(fahrenheit): 
    """Converts a temperature from Fahrenheit to Celsius.""" 
    celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR - 32 
    return celsius 
def convert_to_fahrenheit(celsius): 
    """Converts a temperature from Celsius to Fahrenheit.""" 
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32 
    return fahrenheit 
def main(): 
    """Prompts the user for input and performs the conversion.""" 
    try: 
        temperature = float(input("Enter the temperature to convert: ")) 
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper() 
<pre><code>    if unit == 'C': 
        converted_temp = convert_to_fahrenheit(temperature) 
        print(f"{temperature}°C is {converted_temp}°F") 
    elif unit == 'F': 
        converted_temp = convert_to_celsius(temperature) 
        print(f"{temperature}°F is {converted_temp}°C") 
    else: 
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.") 
 main() 
 
except ValueError as e: 
