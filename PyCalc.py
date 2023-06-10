"""
In this part we are going to made a calculator programme by using the python. Where an user can define any of the operators which are given on console. We will use the "switch case" method for doing the calculation procedure.

So, let's get Started!!

"""

# Taking input from the user

# First Number:
num1 = int(input("Enter the First value here:\n"))
# Second Number:
num2 = int(input("Enter the Second value here:\n"))

# Taking operator from the user:
operator = input("Give any of these operators: + , - , * , / , % , //\n")

# Using switch case for differtiate the Operations:

match operator:
    case "+":
        result = num1 + num2
        print("Addition result is:" ,result)
    case "-":
        result = num1 - num2
        print("Subtraction result is:" ,result)
    case "*":
        result = num1 * num2
        print("Multiplition result is:" ,result)
    case "/":
        result = num1 / num2
        print("Division result is:" ,result)
    case "%":
        result = num1 % num2
        print("Modullation result is:" ,result)
    case "//":
        result = num1 // num2
        print("Floordivision result is:" ,result)