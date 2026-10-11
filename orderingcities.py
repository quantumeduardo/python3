cities = [] #initialize an empty list to store cities
with open('unordered_cities.txt', 'r') as f: #open the file in read mode
    for line in f: #iterate over each line in the file
        print(line.rstrip("\n")) #print the line without the newline character
        cities.append(line.rstrip("\n")) #add the line to the cities list
    print(cities) #print the list of cities before sorting
    cities.sort() #sort the list of cities in ascending order
    print(cities) #print the list of cities after sorting