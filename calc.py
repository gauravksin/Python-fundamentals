# Simple calculator program in Python 

# addition, subtraction, multiplication, and division functions
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# function to display the menu, user inputs and perform the selected operation
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
     choice = input("Enter your choice from 1 to 4: ")

     if choice in ['1', '2', '3', '4']:
        try: 
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
     else:
        print("Invalid input")
    
     print("Do you want to continue? (y/n)")
     continue_choice = input().lower()
     if continue_choice != 'y':
         break
    print("Thank you for using the calculator!")

# Run the calculator    
calculator()
