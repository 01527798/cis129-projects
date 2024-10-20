"""
Hotdog Cookout Lab:
Students will be provided the Pseudocode, then they are to create this in Python.

Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of 
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the 
number of hot dogs each person will be given. The program should display the following:

1. The minimum number of packages of hot dogs required.
2. The minimum number of packages of buns required
3. The number of hot dogs that will be left over
4. The number of buns that will be left over

Programming Exercise (Hotdog Cookout Calculator)
"""
#Kaitlyn Chung
#CIS129
#10/20/24

#Importing ceiling function from the math module
from math import ceil

#Local variable for the total number of hot dogs needed.
#The getTotalHotDogs module gets the number of people attending the cookout and the number of hot dogs each
#person will be given, and stores the product in thetotalHotDogs reference variable.

def getTotalHotDogs():
    people = 0   #Number of people attending
    hotDogs = 0  #Hot dogs per person

   #Get the number of people attending the cookout.
    print("Enter the number of people attending the cookout: ")
    people = input()
    people = int(people)
    
   #Get the number of hot dogs each person will be given.
    print("Enter the number of hot dogs for each person: ")
    hotDogs = input()
    hotDogs = int(hotDogs)

   #Calculate and return the total number of hot dogs needed.
    return people * hotDogs
total = getTotalHotDogs()

#Named constants for the package sizes
DOGS = 10   #Hot dogs in a package
BUNS = 8    #Hot dog buns in a package

#Local variables
dogsLeft = 0  #Leftover hot dogs
bunsLeft = 0  #Leftover hot dog buns
minDogs = 0   #Minimum packages of hot dogs
minBuns = 0   #Minimum packages of hot dog buns

#Calculate the number of leftover hot dogs.
dogsLeft = (DOGS - total % DOGS) % DOGS

# Calculate the minimum number of packages of hot dogs.
minDogs = ceil(total / DOGS) 

#Calculate the number of leftover hot dog buns.
bunsLeft = (BUNS - total % BUNS) % BUNS

#Calculate the minimum number of packages of hot dog buns.
minBuns = ceil(total / BUNS) 

#The showResults module accepts the total number of hot dogs as an argument and calculates the minimum packages of hot
# dogs and hot dog buns, the left over hot dogs and hot dog buns, and displays the results.

#Display the minimum packages of hot dogs needed.
print("Minimum packages of hot dogs needed: ", minDogs)

#Display the minimum packages of buns needed.
print("Minimum packages of hot dog buns needed: ", minBuns)

#Display the number of hot dogs left over.
print("Hot dogs left over: ", dogsLeft)

#Display the number of hot dog buns left over.
print("Hot dog buns left over: ", bunsLeft)