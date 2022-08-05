#Creating a new class
#Parent class
class vehicle():
    def __init__(self,name,fuel,size):
       self.name = name
       self.fuel = fuel
       self.size = size

       #method
    def car_ability(self,speed):
       self.speed = 20
       #-->if the return function isnt there it wont be stored in the computer for it to be printed out
       return("the automobile speed is:", self.speed)
      #  print("the aitomobile speed is:", self.speed,)

    def car_color(self,color):
       self.color = color
       return("the automobile color is:", self.color)
       #--> the return function can also serve as a print function but can also do better
      #  print("the automobile color is:", self.color)

#sub/child class
#the child class inherit all the methods or parameters of the parent class
class brand(vehicle):
   def __init__(self,name,brand):
      self.name = name
      self.brand = brand
      print("name of brand:", self.name,)
      print("color of brand:", self.brand,)
   def car_color(self):
      return("This is me overiding the parent method")


t = vehicle("toyota",40, 60)
y = brand("benz","benz 2022")
print(t.car_ability(30))
print(y.car_color())

#if you dont want your vehicle to have any method you could use the pass function

class student():
   # pass
   print('helo zuri')
s = student()

#clases makes use of methods and functions
#method or function are unique to clases

#for calling a function of a class
# first call the class then call the function by storing both in any variable
#e.g h = class()
#print(h.function())



#kwargs behaves like dictionary
#this function is new to windows 7
def new(*args):
   print(new)
new('yello','bye bye')

help(int)