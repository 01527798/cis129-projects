#Module 12 Lab
#Kaitlyn Chung
#12-7-24
#This script creates a pet class with fields for  the name, type of pet, and age of the pet. It will also have methods to set name, type, and age. 
#This script will retrieve and display  the pet's name, type, and age to the user.

class Pet:
    """Pet class for inputting and access data about a user's pet"""
    
    def __init__(self, n, t, a):
        """Initializes variables"""
        
        self._name = n
        self._type = t
        self._age = a
   
    @property
    def getName(self):
        """Retrieves the name"""
        return self._name

    @property
    def getType(self):
        """Retrieves the type"""
        return self._type

    @property
    def getAge(self):
        """Retrieves the age"""
        return self._age
  
    def setName(self,n): #Set private name to n, which will be switched based on user inputs
        """Set the name"""
        self._name = n
        
    def setType(self,t):#Set private type to t, which will be switched based on user inputs
        """Set the type"""
        self._type = t

    def setAge(self,a): #Set private age to a, which will be switched based on user inputs
        """Set the age"""
        self._age = a

#Initialize variables for new class
inputName = 'name'
inputType = 'animal'
inputAge = 0

Animal = Pet(inputName,inputType,inputAge) #Creates a pet class named Animal

inputName = input('Enter a pet name: ') #Changes n in .setName method to user inputted name
Animal.setName(inputName)

inputType = input('Enter a pet type: ') #Changes t in .setType method to user inputted type
Animal.setType(inputType)

inputAge = input('Enter a pet age: ') #Changes a in .setAge method to user inputted age
Animal.setAge(inputAge)
                  
print(f'The pet name is {Animal._name}') #prints the Animal object's name
print(f'The pet type is {Animal._type}')
print(f'The pet age is {Animal._age}')
                  