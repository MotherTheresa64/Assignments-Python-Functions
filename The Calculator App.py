# Task 1: Create functions for each arithmetic operation.
# Each of the below functions pertain to their designated arythmatic operation (addition, subtraction, multiplication or division)
# This function adds two numbers
def addition(x, y):
    return x + y

# This function subtracts two numbers
def subtractraction(x, y):
    return x - y

# This function multiplies two numbers
def multiplication(x, y):
    return x * y

# This function divides two numbers
def division(x, y):
    return x / y




# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# This function adds two numbers
def addition(x, y):
    return x + y

# This function subtracts two numbers
def subtractraction(x, y):
    return x - y

# This function multiplies two numbers
def multiplication(x, y):
    return x * y

# This function divides two numbers
def division(x, y):
    return x / y

print("What would you like to do?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtractraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Would you like to do more? (yes/no): ")
        if next_calculation == "no":
          break
        

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
# This function adds two numbers
def addition(x, y):
    return x + y

# This function subtracts two numbers
def subtractraction(x, y):
    return x - y

# This function multiplies two numbers
def multiplication(x, y):
    return x * y

# This function divides two numbers
def division(x, y):
    return x / y

print("What would you like to do?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtractraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            if num2 != 0:
                 print(num1, "/", num2, "=", division(num1, num2))
        # Will ask the user to pick a number larger than 0 if they try to divide by 0
            else: 
                print("Please choose a second number that is larger than 0")
           
            
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Would you like to do more? (yes/no): ")
        if next_calculation == "no":
          break
        