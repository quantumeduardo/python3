def celcius_to_fahrenheit(celsius):

    Farenheit = (celsius * 9/5) + 32
    return Farenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celcius_to_fahrenheit(celsius)
print(f"Temperature in Fahrenheit: {fahrenheit}")