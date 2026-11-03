# Byoung Hartzel L. Kim         9 - Beryllium
# 2nd quarter 3rd task

# creates the main parent class called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    @property # @property is a decorator that allows you to define a method as a property, which can be accessed like an attribute.
    def animal_name(self):
        return self.name

    @animal_name.setter
    def animal_name(self, newname):
        self.name = newname
        
# we create three child classes named Lion, Elephant, and Monkey that inherit from the Animal class.
# each child class has its own implementation of the eat() and make_sound() methods, so that they all have their unique methods.
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return self.name + " eats fresh meat."

    def make_sound(self):
        return self.name + " roars loudly!"
        
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return self.name + " eats grass and fruits."

    def make_sound(self):
        return self.name + " trumpets!"
        
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return self.name + " eats bananas."

    def make_sound(self):
        return self.name + " chatters!"
    
# the reason why we just dont use a single instance of eat and make_sound is because as shown in the guide, they all have different types of sound and eating habits
# we create variables with the names of the animals and use their own classes
lion = Lion("Simba")  # Lion is named Simba
elephant = Elephant("Dumbo")  # Elephant is named Dumbo
monkey = Monkey("George")  # Monkey is named George

# we print their sounds and eating habits
print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")

