#Create a superclass called Vehicle which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick
#Create a class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes: 
    #year, make, model, doors (2 or 4), roof (solid or sunroof)
#Write an app that will accept user input for a car and will store the data in the attributes above
#The app will then output the data in an easy-to-read format

class Vehicle:
    def __init__(self, car, truck, plane, boat, broomstick):
        self.car = car
        self.truck = truck
        self.plane = plane
        self.boat = boat
        self.broomstick = broomstick

class Automobile (Vehicle):
    def __init__(year, make, model, doors, roof):
        super().__init__(car, truck, plane, boat, broomstick)
        self.year = year
        self.make = make
        self.model = model 
        self.doors = doors
        self.roof = roof
    type = input("Please enter the type of automobile: ")
    year = input("Please enter the year of the automobile: ")
    make = input("Please enter the make of the automobile: ")
    model = input("Please enter the model of the automobile: ")
    doors = input("Please enter the number of doors on the automobile (2 or 4): ")
    roof = input("Plase enter the the type of roof on the automobile (solid or sunroof): ")
    print("Vehicle Type: ", type)
    print("Year: ", year)
    print("Make: ", make)
    print("Model: ", model)
    print("Number of doors: ", doors)
    print("Type of roof: ", roof)


    
