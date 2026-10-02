def user_info():
    
    user_name = input("Please enter your name: ")
    user_age = int(input("Please enter your age: "))
    
    return user_name, user_age

user_name, user_age = user_info()
print ("Hello, " + user_name + "! you are " + str(user_age) + "years old.")

