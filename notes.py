# More about variables #
#**Learning objectives**
#
#After this section:
#
#* You will be able to use variables in different contexts
#* You will know what kind of data can be stored in variables
#* You will understand the difference between strings, integers and floating point numbers



myXVAL = 10
myxval = 7

print (myXVAL)

name = "Chuck"
number = 100
newNumber = "100"

print (number/2)
#Casting Example
print(int(newNumber)/2)

myFLoat = 3.53

num1=100
num2=75
num3=976

avg = (num1 + num2 + num3)/3

print (f"Average: {avg}")
print (avg)
print ("Average ", avg)
print("AVerage " + str(avg))


beds = 4
bath = 3
address = "123 Maple Street"
city = "Folsom"
zip = 95630
rent = 6500

print(f"House for rent at {address} in {city} ({zip})")
print(f"\t{beds} bedrooms, {bath} bathrooms")
print(f"\trent is ${rent}/month")



#File path example
print("I have a file loacted at: C:\\users\\myname\\unnatiyagnik\\Docume...")

## Live Demo ##
#
# Casing
#name = input("What is your name? ")
#Name = input("What is your name? ")
#print(name)
#print(Name)
#
# Talk about Variable Types
#   * int vs string vs float
#intNum = 75
#print(intNum/2)
#number = "100"
#print(number / 2)
#number1 = 2.5
#number2 = -1.25
#number3 = 3.62
#
#print(f"Mean: {mean}")
#mean = (number1 + number2 + number3) / 3
#
# Printing different types and Casting
#result = 10 * 25
#print("The result is " + result)
#print("The result is " + str(result))
#print("The result is", result)
#print(f"The result is {result}") # Format string {} denotes values to be printed
#name = "Mark"
#age = 37
#city = "Palo Alto"
#print(f"Hi {name}, you are {age} years old. You live in {city}.")
#
# Printing invisible things
#print("\n") # newline
#print("\t") # tab
#print("\\") # \
