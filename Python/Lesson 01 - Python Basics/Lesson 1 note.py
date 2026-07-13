# # #These are my note for Lesson 1

# # #DataTypes
# # integers = 1
# # float = 3.14
# # Boolean = True
# # string = "Hello" 

# # #Conversion Casting
# # str(15)
# # int("2")
# # bool("hello")
# # float("10.3")

# # #Operators
# # addition = x + y
# # Concatenation = x + y
# # subtraction = x - y
# # Multiplication = x * y 
# # Division = x / y
# # floor division = x // y

# # #Operands
# # x += 3

# # #Comparison always evaluate to a boolean
# # less_than = x > y
# # greater_than = x < y
# # equal_to = x == y 
# # less_than_or_equal_to = x <= y
# # greater_than_or_equal_to = x >= y 

# # #Logical Statements
# # x+


# # # Variable rules


# # newline


# user_name = input("What is your name?")
# user_number = int(input("What is your favorite number?"))
# print("Hello " + user_name)
# print("Your favorite number is ", user_number)
# print("Your favorite number minus 10 is ", (user_number - 10))

pi = 3.14

diameter_of_pizza = int(input("What is the diameter of the 1st pizza do you want?"))
diameter_of_pizza2 = int(input("What is the diameter of the 2nd pizza do you want?"))
price_of_pizza = float(input("How much would you pay for the 1st pizza?"))
price_of_pizza2 = float (input("How much would you pay for the 2nd pizza?"))
area_pizza = pi * (diameter_of_pizza / 2)
area_pizza2 = pi * (diameter_of_pizza2 / 2)
cost_area_pizza = price_of_pizza / area_pizza
cost_area_pizza2 = price_of_pizza2 / area_pizza2
print(cost_area_pizza)
print(cost_area_pizza2)
print(cost_area_pizza > cost_area_pizza2) 