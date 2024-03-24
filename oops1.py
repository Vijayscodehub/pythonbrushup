# class is template to create object
# object is instance of class
# method is a function that is bound to instance of class
# attr is var bound to the instance of class

#self =  reference to instance of class
class Kettle:
    power_source = "Electricity"
    
    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False
        
    def switch_on(self):
        self.on = True
        
kenwood = Kettle("Kenwood", 20.99)
print(kenwood.price)
print(kenwood.make)

kenwood.price = 12.99
print(kenwood.price)

hamilton = Kettle("Hamilton", 15.90)
print(hamilton.price)
print(hamilton.make)

hamilton.price = 13.99
print(hamilton.price)

print("Models : {} = {}, {} = {}" .format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))
print("Models : {0.make} = {0.price}, {1.make} = {1.price}" .format(kenwood,hamilton))

print()
print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

Kettle.switch_on(hamilton)
print(hamilton.on)
# hamilton.on = False  #here comes the part of private.. etc
# print(hamilton.on)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)  # hamilton does not have a attr power
print("x"*70)
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print("power source changed to fire")
Kettle.power_source = "fire"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print("power source kenwood changed to atomic")
kenwood.power_source = "atomic"  #adds a new attr to kenwood dict
print(kenwood.power_source)
print(kenwood.__dict__)


