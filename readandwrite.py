# import os  --import the entire module for built in functions
# from os import remove #import the remove function from the os module to delete files
# from os.path import exists #import the exists function from the os.path module to check if a file exists

# if exists('new file'):
#     print("File exists")
# else:
#     print("File does not exist")

# with open('readmefile','r') as f: #using read mode with the function open - takes parameter file name and mode. r is read  
#     for line in f:             #iterating over each line in the file 'f'
#         print(line.rstrip("\n")) #printing each line without the newline character rstrip and \n stripping the gap 

# with open('new file', 'a+') as f: #using write mode with the function open - takes parameter file name and mode. w is write and a is append to add more on the current file - w+ makes it so that it reads and writes a+ appends and reads and writes   
#     f.write("\n test, World!") #writing a line to the file 'f' - overwrites- if there is something on there already it will replaced
#     f.write("\n HHHH") #writing a newline character to the file 'f'

from mycomputations import get_average, get_sum        #impporting the functions get_average and get_sum from the mycomputations.py file

listofnumerals = []  #creates an empy list to store the numbers from the file

with open ('listofnumbers.txt','r') as f:  #this is with module built in function open - takes parameter file name and mode. r is read 
    for line in f:                          #iterates over each line in the file 'f'
        listofnumerals.append(int(line))    #appends each line as an integer to the list
        print(listofnumerals)               # each line is printed as it is appended to the list
print(get_average(listofnumerals[0], listofnumerals[1], listofnumerals[2])) #importing the function get_average from the mycomputations.py file and passing the first three numbers in the list to it
print(get_sum(listofnumerals[0], listofnumerals[1]))                        #importing the function get_sum from the mycomputations.py file and passing the first two numbers in the list to it