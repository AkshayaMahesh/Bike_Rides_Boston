#Problem 1
# Creating a Class 'Adder' with methods and constructor
class Adder:
    # Initializing Class  objects
    def __init__(self,start=[]):
        self.data=start
    # defining a method to automatically dispatch add methods
    def __add__(self, other):
        return self.add(other)
    # defining a method for addition
    def add(self,x,y):
        print("Not implemented")
# Creating a class 'ListAdder' and defining methods
class ListAdder(Adder):
    # Method to add lists
    def add(self,y):
        return self.data+y
# Creating a class 'DictAdder' and defining methods
class DictAdder(Adder):
    # Method to add items in two dictionaries
    def add(self,y):
        k=self.data.copy()
        k.update(y)
        return k
print('Part1 :')
k=Adder().add([],[])  # creating Adder Object and calling Add method of Adder class
x=ListAdder([1,3]) # Creating a ListAdder object
y=x+[1,7,8] # Adding two lists
print('Addition of two lists gives:',y)# Result
a= DictAdder(dict(colour='Red'))+{'tint':1} # Creating DictAdder object and adding two dict items
print('Addition of two dictionaries gives:',a) # Result
print( "It is best to put constructors in super class and operator overloading methods in subclass.\n"
       "Here values are attached to objects and hence this version is more object-oriented.\n"
       )

#Problem 2
# Creating a class MyList that shadows a Python List
class MyList:
    # Initilalizing object and adding constructors
    def __init__(self,start):
        #self.data=start[:] We can use empty list as well to copy initial value
        self.data=list(start)
    # Method to add lists
    def __add__(self, other):
        return MyList(self.data + other)
    # method to multiply lists
    def __mul__(self, other):
        return MyList(self.data * other)
    # Method to return an item from a list
    def __getitem__(self, item):
        return MyList(self.data[item])
    # method to find the number of items in a list
    def __len__(self):
        return MyList(self.data)
    # method to return sliced list
    def __getslice__(self, start, end):
        return MyList(self.data[start:end])
    #method to append a list
    def append(self,value):
        self.data.append(value)
    # method to sort and reverse a list
    def __getattr__(self, value):
        return getattr(self.data,value)
    # Catchall display method
    def __repr__(self):
        return repr(self.data)

print("\nPart 2:")
if __name__ == '__main__':
 x = MyList('World') # Creating an object
 print('Initial list:',x)
 print('Addition of lists:',x + ['life']) # Adding lists
 print('last item:',x[-1]) # getting an item of the list
 print('On Slicing:',x[1:4]) # returns sliced list
 print('Multiplication of lists:',x * 2) # multiplication of lists
 x.append('k') # Appending the list
 x.sort() # sorting list
 print('list after appending and sorting:',x)
 x.reverse()# reverse of list items
 print('Reversal of list:',x)
 print("Copying initial value in constructor is important as it may be mutable.\n"
       "The __getattr__ method routes calls to the wrapped list.\n"
       "We can use empty list as well to copy initial value.")


#Problem 3
class MyListSub(MyList):
 calls = 0 # Shared by instances
 def __init__(self, start):
  self.adds = 0 # Varies in each instance
  MyList.__init__(self, start)
 def __add__(self, other):
  print('add: ' + str(other))
  MyListSub.calls += 1 # Class-wide counter
  self.adds += 1 # Per-instance counts
  return MyList.__add__(self, other)
 def stats(self):
  return self.calls, self.adds

print("\nPart 3:")
if __name__ == '__main__':
# Creating MyListSub objects
 x = MyListSub('Hello')
 y = MyListSub('World')
 print('Item of First Object:',x[2])
 print('Item of Second Object:',y[1:])
# Adding items to created objects
 print(x + ['one'])
 print(y+['two'])
 print(y + ['three'])
# Printing the count of calls
 print("Count of Calls:",x.stats())

# Problem 4
# Creating a class Lunch and defining methods
class Lunch:
    # Initializing Customer and Employee objects
    def __init__(self):
        self.customer=Customer()
        self.employee=Employee()
    # Method to place order
    def order(self,foodName):
        self.customer.placeOrder(foodName,self.employee)
    # Method to print the items ordered by the customer
    def result(self):
        self.customer.printFood()
# creating a Customer class and defining it's methods
class Customer:
    # initializing food names to None
    def __init__(self):
        self.food=None
    # Method to place food order by the customer
    def placeOrder(self,foodName,employee):
        self.food=employee.takeOrder(foodName)
    # Method to print food items ordered
    def printFood(self):
         print('Item Ordered:',self.food.name)
# creating a Employee class and defining it's methods
class Employee:
    # Method to take order from Customer
    def takeOrder(self,foodName):
        return Food(foodName)
# creating a class Food
class Food:
    # method to store food names
    def __init__(self,name):
        self.name=name

print('\nPart 4:')
x=Lunch()  # Creating a 'Lunch' object
x.order('Idli') # Taking orders from customersw1
x.result() # Result Gives Items ordered

# Problem 5
# Creating classes and adding methods to it
class Animal:
    # Reply method for Animal
    def reply(self):
        self.speak()
    # Speak method for animal
    def speak(self):
        print("Grrrr")
# Creating Mammal class that inherits Animal class
class Mammal(Animal):
    # Speak method for mammal
    def speak(self):
        print("hisss")
# Creating Cat class that inherits mammal class
class Cat(Mammal):
    # Speak method for Cat
    def speak(self):
        print("Meowww")
# Creating Dog class that inherits mammal class
class Dog(Mammal):
    # Speak method for Dog
        def speak(self):
            print("bouuuu")
    # Creating Primate class that inherits mammal class
class Primate(Mammal):
    # Speak method for Primate
    def speak(self):
        print("Hello")
# Hacker class inheriting Primate Class
class Hacker(Primate):
    pass
print("\nPart 5:")
k=Dog() # Creating an object for Dog class
k.reply() # Calling Reply method
b=Hacker() # Creating a object for Hacker class
b.reply() # Calling Reply method








