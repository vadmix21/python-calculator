import math


operation = input("Enter operation (+, -, *, /, ^, sqrt): ")

if operation == 'sqrt':
    try:
        num = float(input("Enter number: "))
        if num >= 0:
            result = math.sqrt(num)
            display_result = int(result) if result.is_integer() else round(result, 4)
            print(f"√{num} = {display_result}")
        else:
            print("Error: Cannot calculate square root of negative number")
    except ValueError:
        print("Error: Please enter a valid number")

else:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is impossible!")
                exit()
            result = num1 / num2
        elif operation == '^':
            result = num1 ** num2
        else:
            print("Error: Unknown operation")
            exit()
        
        def format_number(x):
            return int(x) if x.is_integer() else round(x, 4)
        
        display_num1 = format_number(num1)
        display_num2 = format_number(num2)
        display_result = format_number(result)
        
        print(f"{display_num1} {operation} {display_num2} = {display_result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")