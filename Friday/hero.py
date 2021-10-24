# DEFINING THE GENERIC HERO class
class Person:
    def __init__(self, name, hairColor, eyeColor, age): # Initialize, Create a person
        self.name = name
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.age = age

Brian = Person("Brian", "Blonde", "Green", 28) # Calls constructor, which calls init function
print(f"{Brian.name} has a hair color of {Brian.hairColor}, and {Brian.eyeColor} eyes")
