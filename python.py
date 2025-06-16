#1. Write a Python program that asks the user for their name and age, then prints a greeting message

'''a = input("enter your name: ")
b = int(input("enter your age: "))
print(f"welcome {a}, you are {b} years old")'''

#2. Write a Python program that checks if a given word is a Python keyword.
'''import keyword
a = input("enter a word: ")
if keyword.iskeyword(a):
      print(f"{a} is python keyword")
else:
        print(f"{a} is not python keyword")'''

#3. Write a Python program that assigns different types of values to variables and prints their types
'''a = [1,5,6,8]
b = 5
c = "hello"
d = (5,6,8)
e = {"a":1,"b":2,"c":3}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''

#4. Write a Python program that asks the user for two numbers and prints their sum.

'''a = int(input("enter first number: "))
b = int(input("enter second number: "))
print(f"the two number sum of" ,a+b)'''

#5. Write a Python script that lists all the keywords in Python.

'''import keyword
lst = keyword.kwlist
print("the python all keywords")
for i in lst:
    print(i)'''


#6. Write a Python program that declares a variable, assigns a value to it, and prints the value.

'''string = "hi"
print(string)'''       
    
#7. Write a Python program to calculate the area of a rectangle using variables for width and height.

'''width = 7
height = 14
rectangle_area = width*height
print(f"area of rectangle is",rectangle_area)'''

#8. Write a Python program to convert kilometers to miles. (Formula : miles = kilometers * conversion_factor, where conversion_factor = 0.621371)

'''kilometer = int(input("enter a kilometer: "))
conversion_factor = 0.621371
miles = kilometer * conversion_factor
print(f"converted kilometer into miles is",miles)'''

#9. Write a Python program to convert Celsius to Fahrenheit.(Forumula: fahrenheit = (celsius * 9/5) + 32)

'''celsius = int(input("enter a celsius: "))
fahrenheit = (celsius* 9/5 + 32)
print(f"{celsius} convert into fahrenheit is",fahrenheit)'''

#10. Explain why the following identifier is invalid and correct it: 2ndVariable = “Hello”.

second_variable = "hello"
var2nd = "hello"