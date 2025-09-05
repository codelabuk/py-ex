class Robot_Dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val

    def bark(self):
        print('Woof Woof!')    

my_dog = Robot_Dog('Spot', 'Chihuahua')
print(my_dog.breed)
print(my_dog.name)
my_dog.bark()