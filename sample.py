import datetime
print("Hello")

x = 5
y = "Abc"
print(x)
print(y)

a = "Hello "
b = "World"
c = a + b
print(c)

a = ["apple", "banana", "cherry", "apple"]
print(a)
print(type(a))
a.sort()
print(a)

a = 0
v = 20

if a==0 :
    print("Right")
else:
    print("Wrong")

i=0
while i<6:
    print(i)
    i=i+1

print("For loop")

for i in range(1,6):
    print(i)
    i=i+1

mytuple=(1,2,3)
print(mytuple)
print(type(mytuple))

# a=10
# print(type(a))

dict={
    "Name":"ABC",
    "Age":23

}
print(dict)
print(dict["Name"])

# Function
def greet(a):
    print("Hello "+a)

greet("ABC")

# Array
cars=["A","B","C"]
print(cars)
for x in cars:
    print(x)

# Class and object

class demo:
    x=5

    def __init__(self,n,a):
        self.name=n
        self.age=a

d1=demo("ABC",20)
print(d1.x)
print(d1.name)
print(d1.age)

#inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("ABC", "XYZ")
x.printname()

x1=datetime.datetime.now()
print(x1)




