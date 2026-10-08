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

from mycomputations import get_average, get_sum

listofnumerals = []

with open ('listofnumbers.txt','r') as f:
    for line in f:
        listofnumerals.append(int(line))
        print(listofnumerals)
print(get_average(listofnumerals[0], listofnumerals[1], listofnumerals[2]))
print(get_sum(listofnumerals[0], listofnumerals[1]))