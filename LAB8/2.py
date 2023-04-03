# define a Vehicle class
class Vehicle:
    # initialize the instance attributes
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    # define a function to display the attributes
    def display(self):
        print(f"Max speed: {self.max_speed}, Mileage: {self.mileage}")

# define a Bus class that inherits from Vehicle class
class Bus(Vehicle):
    # initialize the instance attributes with default value for seating capacity
    def __init__(self, max_speed, mileage, seating_capacity=50):
        # call the parent constructor
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity
    
    # define a function to calculate and display the total fare
    def total_fare(self):
        # calculate the base fare as seating capacity * 100
        base_fare = self.seating_capacity * 100
        # add 10% extra charges for bus
        total_fare = base_fare + (base_fare * 0.1)
        print(f"Total fare: {total_fare}")

# create an object of Vehicle class with max speed 200 and mileage 20
v1 = Vehicle(200, 20)
# create an object of Bus class with max speed 150, mileage 15 and seating capacity 40
b1 = Bus(150, 15, 40)

# call the display method on both objects
v1.display() # output: Max speed: 200, Mileage: 20 
b1.display() # output: Max speed: 150, Mileage: 15

# call the total fare method on bus object only (vehicle does not have this method)
b1.total_fare() # output: Total fare: 4400.0