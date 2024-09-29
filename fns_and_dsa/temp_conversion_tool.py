temp = float(input("Enter the temperature: "))
FAHRENHEIT_TO_CELSIUS_FACTOR = ((9 * temp) / 5 + 32, 1)
CELSIUS_TO_FAHRENHEIT_FACTOR = round((temp - 32) * 5 / 9, 1)
unit = input("Is this Temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))


if unit == "C":
    temp = ((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
