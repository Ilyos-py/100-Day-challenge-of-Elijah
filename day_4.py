#Augmented assignments: variable <operator>= value
number = 5
number += 4
print(number)

number -= 5
print(number)

number *=2
print(number)

number /= 2
print(number)
#This also works with //, % and **


#Boolean operators and conditional statements
print(1 == 1)# equals to
print(1 > 2)#bigger than
print(1 < 2)#less than
print(1 >= 2)#bigger than or equals to
print(1 <= 2)# less than or equals to

age = 18
if age >= 18:
    print("You're an adult")
else:
    print("You are not an adult")
#and = checks if both conditions are True
age = 18
is_citisen = True
if age >= 18 and is_citisen:
    print("You are elligible to vote")
else:
    print("You are not elligible to vote")
#or - checks if at least one condition is True
age = 18
is_citisen = False
if is_citisen or age >= 18:
    print("You are elligible to vote")
else:
    print("You are not elligible to vote")
#not - checks the opposite of condition example:
is_citisen = True
if not is_citisen:
    print("You are not a citizen")
else:
    print("You are a citizen")


#Functions 
#def name(argument) - body of function
def hello():
    print("Hello world")
hello()

#here s another function that prints the sum of two numbers
def summ(a, b):
    return a + b

mysum = summ(5, 5)
print(mysum)


