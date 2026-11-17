# Byoung Hartzel L. Kim         9 - Beryllium
# activity 5 - polymorphism activity 2
class Car: # creates a class named "car"
    def move(self):
        print("The car drives on the road.") # self explanatory

class Boat: # creates a class named "boat"
    def move(self):
        print("The boat sails on the water.")

class Drone: # creates a class named "drone"
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

# we give very unique names to the objects of the classes we created above
truck = Car()
yacht = Boat()
helicopter = Drone()

# we start the trip!
start_trip(truck)
start_trip(yacht)
start_trip(helicopter)
