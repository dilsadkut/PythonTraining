# -*- coding: utf-8 -*-
"""Day4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1onNqftEhESJNaccr42Xx_MdnziHHX14V

# Functions

Functions are blocks of code that can be used over and over again to perform a specific action.

As we know, in Python, there are print (), len () etc. Many available functions are defined.

We can use it in our own code by providing access to functions defined in libraries, modules and packages. These are called predefined functions, embedded functions (built-in) or library functions. We can use ready-made functions as well as create our own functions. (User-defined)


Functions prevent code repetition and our code stays more modular and organized.


*****

def "function_name"(parameter1,parameter2,..):


> "Do something"

  return "return something"  (depends on functionality)
"""

def hello():
  print("Hello Everyone!!")

hello()   #calling the func   #the functions don't have any parameters

def hello(name):
  print("Hello " + name)

hello("Asli")

def func_in_func(name1):
    return hello(name1)

func_in_func("Ugurcan")

def func1():
  print("Hello World!!")


func1()
print("Google")
func1()
func1()
func1()
func1()

def summ(a,b):
  summ = a + b
  print(summ)

summ(6.0,7.5)

t = summ(8,9)
t

def func(x,y):
  summ = x + y
  multip = x * y
  return (summ,multip)

#t = summ 
#c = multip

t,c = func(23,45)

print(t,c)

func(23,45)

print("Sum of the values: " + str(t) + ", Multiplying of the values: " + str(c))

#Let's write a function that it will square the entered number, but will be terminated when you enter the number 5 and give us an error message.


def sqr(x):
  if x == 5:
    return ("Terminated because you entered 5")

  result = x **2
  return (result)

sqr(10)

sqr(5)

d = sqr(5)
print(d)

# Let's write a function that tells you whether the entered number is positive, negative or zero.



def func(x):
  if x > 0:
    return ("Positive")
  elif x < 0:
    return ("Negative")
  else:
    return ("Zero")

for i in [-2,5,6,0,-4,-7]:
  print(func(i))

#factorial calculation
#0! = 1
#1!= 1
#2!= 2 * 1 =2
#6! = 6 * 5* 4 *3 * 2 *1 = 720


def factorial(num):
  factorial = 1
  if (num == 0 or num == 1):
    print("Factorial: ", factorial)
  else:
    while (num >= 1):
      factorial = factorial * num
      num -= 1
    print("Factorial: ", factorial)


# 1 * 5 = 5 = factorial
# 5 * 4 = 20
# 20 * 3 = 60
#60 * 2 = 120
# 120 * 1 = 120

factorial(5)

def faktoriyel(sayi):
  faktoriyel = 1
  for i in range(1,sayi+1):
    faktoriyel *= i
  return faktoriyel

faktoriyel(5)

#using for loop

def factorial2(num2):
  factorial2 = 1
  if (num2 == 0 or num2 == 1):
    print("Factorial: ", factorial2)
  else:
    for i in range(factorial2, num2+1):    
        factorial2 *= i      
    print("Factorial: ", factorial2)

factorial2(6)

def factorial3(nums):
  factorial3 = 1
  if (nums == 0 or nums == 1):
    return ("Factorial: ", factorial3)
  else:
    for i in range(factorial3, nums+1):
       factorial3 *= i      
    return (factorial3)

x = factorial3(6)
print(x)

x

def hello2(name, capLetter = False):
  if capLetter:
    print("Hello " + name.upper())
  else:
    print("Hello " + name)

hello2("asli")

hello2("Asli", capLetter= True)

#lambda function
(lambda x: x + 1)(2)

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')

"""### * args and   ** kwargs
* args (Non Keyword Arguments)
* kwargs (Keyword Arguments)
"""

def multp(*args):
  result = 1
  for i in args:
        result *= i
        print(result) 

# *args keeps the data as tuple type.

multp(4,5,6,7,8,9)

def multp1(*args):
  result = 2
  for i in args:
        result *= i # result = result * i
        print(result) 


# *args keeps the data as tuple type.

multp1([4,5,6,7])

multp1(2,3,4,5)

[4,5,6] * 3

def func_kwargs(**kwargs):
    print(kwargs)
    
func_kwargs(name = "Murat", name2 = "Ömer", number=12345, can='Emir', beril='yılmaz')

def salaryCalc(salary):

  if salary < 0:
    return("Invalid value")
  else:
    if 0 < salary <= 1000:
      salary = salary + salary * 0.15
    elif salary <= 2000:
      salary = salary + salary * 0.1
    elif salary <= 3000:
      salary = salary + salary * 0.05
    else:
      salary = salary + salary * 0.025

    return ("New salary: ", salary)

salaryCalc(-5)

salaryCalc(800)

def salaryCalc2():

  salary = float(input("Please enter your current salary: "))

  if salary < 0:
    return("Invalid value")
  else:
    if 0 < salary <= 1000:
      salary = salary + salary * 0.15
    elif salary <= 2000:
      salary = salary + salary * 0.1
    elif salary <= 3000:
      salary = salary + salary * 0.05
    else:
      salary = salary + salary * 0.025

    return ("New salary: ", salary)

new_salary = salaryCalc2() 
print(new_salary)

"""### Let's write a function that returns a random word from a list.

### Modules

import numpy

import tensorflow as tf

import myModules

myModules.myFunc()

from myModules import *

myFunc()
"""

words = ["artificial","intelligence","machine","learning","python","programming"]


#from random import *
import random as rnd

def randomWord(words):
  index = rnd.randint(0, len(words)-1)
  return words[index]

len(words)

word = randomWord(words)
print(word)

"""### Global & Local Variables"""

x = 5

print(x)

def display():
  x = 4
  return(x)

display()

print(x)

"""## Methods

Functions are called by name, it can take parameters inside and optionally the resulting value can be used outside of the function.


Methods are also called by name, in many ways they are like functions, but calling is performed through an object such as a String or list.


object.methodName(parameter)
"""

s = input("Please enter a name: ")


print(s.upper())

#it does not return any value
list1 = [1,2,3,4,5,6]

list1.remove(4)
list1

list1

list1.index(6)

#return the index of the element with the highest value in a given list.

myList = [45,7,23,6,12,78]

maxElement = max(myList)

maxIndex = myList.index(maxElement)

print(maxIndex)

"""# Exceptions 

* Programmer Errors 
* Program Bugs 
* Exceptions
"""

# error example,SyntaxError.

print "Hello World!"

#bug example.

num1 = input("Enter the first integer: ")
num2 = input("Enter the second integer: ")

print(num1, "+", num2, "=", num1 + num2)

#exception example, ValueError.

num3 = int(input("First integer: "))
num4 = int(input("Second integer: "))

print(num3, "/",num4, "=", num3/num4)

# ZeroDivisionError.


num3 = int(input("First integer: "))
num4 = int(input("Second integer: "))

print(num3, "/",num4, "=", num3/num4)

"""## Exception Handling


try:


> the situations where we can get exceptions

except "Exception Name":


> the operations in case of exceptions




"""

x = "Alan Turing"

int(x)

try:
  int(x)

except ValueError:
  print("Please enter an integer value!!!")

num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ValueError:
  print("Please enter an integer value!!!")

num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ZeroDivisionError:
    print("Please enter the second input different than 0 value!!!")
    ebru = int(input("Enter a integer number"))
ebru

num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ValueError:
  print("Please enter an integer value!!!")
except ZeroDivisionError:
  print("Please enter the second input different than 0 value!!!")
except:
  print("Unknown error...")

num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except (ValueError, ZeroDivisionError):
  print("Error!!!")

#try/except/as


num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ValueError as error:
  print("Error!!!")
  print("Error message: ", error)

#exception handling in loop structure


while True:
    num1 = input("First number: (Press q for quit the program): ")

    if num1 == "q":
        break

    num2 = input("Second number: ")

    try:
        num1_int = int(num1)
        num2_int = int(num2)
        print(num1_int, "/", num2_int, "=", num1_int / num2_int)
    except (ValueError, ZeroDivisionError):
        print("Error!")
        print("Please try again!")

"""
exception handling in functions
using raise command
"""


def reverse(s):

    if (type(s) != str):
        raise ValueError("Please enter a String type.")
    else:
        return s[::-1]

reverse("python")

reverse(12)