import math

class Location:
    def __init__(self, x, y): #Constructor method that assigns location parameters to instance attributes
        self.x = x
        self.y = y
    def __str__(self): #method returns string representation of location object
        return f'({self.x}, {self.y})'

class Car:
    def __init__(self, name, location, cost): #Constructor method that assigns 3 parameters to instance attributes
        self.name = name
        self.location = location #attribute uses location object
        self.cost = cost
    def __str__(self): #method returns string of representation of car object
        return f'[{self.name}, {self.location}, {self.cost}]'
    def move_to(self, new_x, new_y): #method updates location attributes to new x and y coordinates 
        self.location.x = new_x
        self.location.y = new_y

    
class Passenger:
    def __init__(self, name, location): #constructor method that assigns 2 parameters to instance attributes
        self.name = name
        self.location = location #attribute uses location object
    def __str__(self): #method returns string representation of passenger object
        return f'[{self.name}, {self.location}]'
    def move_to(self, new_x, new_y): #method updates location attributes to new x and y coordinates 
        self.location.x = new_x
        self.location.y = new_y
    
    
class RideSharingApp:
    def __init__(self): #constructor method defines two list attibutes as empty lists
        self.cars = [] #list stores car objects
        self.passengers = [] #list stores passenger objects
    def add_car(self, car): #method adds car object to car list
        self.cars.append(car)
    def add_passenger(self, passenger): #method adds passenger object to passenger list
        self.passengers.append(passenger)
    def remove_car(self,car): #method removes car object from car list
        self.cars.remove(car)
    def remove_passenger(self,passenger): #method removes passenger object from passenger list
        self.passengers.remove(passenger)
    def find_cheapest_car(self): #method finds cheapest car available
        first_car = self.cars[0] #first_car is used as the base car to compare other cars prices to
        for car in self.cars: #method iterates through the car objects
            if car.cost < first_car.cost: #if car is less than next iterated car, that car becomes the cheapest car
                cheapest_car = car
        print(f'The cheapest car available is {cheapest_car.name} with rate of ${cheapest_car.cost} per mile.') #prints the cheapest car available to the user
    def find_nearest_car(self,passenger): #method finds nearest car available
        shortest_distance = float('inf') #shortest distanced car is initially set to infinity
        for car in self.cars: #method iterates through car objects using the distance formula to determine the shortes distance between car and passenger
            distance = ((car.location.x - passenger.location.x)**2 + (car.location.y - passenger.location.y)**2)**0.5
            if shortest_distance > distance: #if distance calculated is shorter than the shortest_distance variable, the shortest distance variable is replaced by that calculated distance
                shortest_distance = distance
        print(f'The nearest car for {passenger.name} is {car.name} at a distance of {shortest_distance:.2f}') #prints the shortest distance to the user


    
    

#For the remaining code (after this line), no modification is required
print('---------------------Object Creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)

mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)

print('-----------------------Scenario 1---------------------')
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 2---------------------')
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 3---------------------')
car3= Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

