class Human:
    # attributes
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # behaviours
    def eating(self, food):
        return ("{} is eating {}".format(self.name, food))


# creating objects 
ram = Human("Ram", 6, 60)
praveen = Human("Praveen", 5.9, 56)
arun=Human("Arun",6.0,50)

# printing object information
print("Height of {} is {}".format(ram.name, ram.height))
print("Weight of {} is {}".format(ram.name, ram.weight))
print(ram.eating("Pizza"))
print("Weight of {} is {}".format(praveen.name, praveen.height))
print("Weight of {} is {}".format(praveen.name, praveen.weight))
print(praveen.eating("Banana"))
print("Weight of {} is {}".format(arun.name, arun.height))
print("Weight of {} is {}".format(arun.name, arun.weight))
print(arun.eating("Rice"))