def get_average(number1,number2):
    return (number1 + number2) / len([number1, number2])

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))

print(get_average(number1, number2))
