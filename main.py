user_name = input("Please enter your name: ")
print(f"Hello, {user_name}!")

user_age = int(input("Please enter your age: "))


if user_age < 18:
    print("You are a minor.")
elif user_age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")  


