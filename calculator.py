# user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, //, %, **): ")

#addition operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

#subtraction operation
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    
#multiplication operation
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    
#division operation
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
        
#floor division operation
elif operation == "//":
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

# modulus operation
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

# exponentiation operation
elif operation == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
    
#invalid operation/ entry
else:
    print("Invalid Entry enter a float type number for invalid  operation. Please enter +, -, *, or /.")
