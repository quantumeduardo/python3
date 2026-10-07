# def counter():

#     number_list = [4,5,6,7,4,3,2]
#     total = 0
#     for number in number_list:
#         total = total + number
#     return total
# print (counter())

# def counter2():
#     user_input = []
#     i = 0
#     while i < 5:
#         user_input.append(int(input("Enter a number: ")))
#         i += 1
#     total = 0
#     for number in user_input:
#         total = total + number
#     return total
# print (counter2())

def counter3():
    user_input = [] #empty list to store user input
    number = 1         #initialized to 1
    while number != 0:   #while loop continues until number is not equal to 0
        number = float(input("Enter a number: "))
        if number != 0:
            user_input.append(number)
        total = 0      # total is initialized to 0
    for number in user_input:           #for loop iterates through the user_input list
        total = total + number
    
    total = total / len(user_input)  # calculate average
   
    return total #returns the average of the user input numbers

print(counter3())