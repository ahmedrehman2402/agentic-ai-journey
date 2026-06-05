###calculator###

while True:
    operator = input("select an operator (+ - * /) or 'q' to quit: ")
    
    if operator == 'q':
        break
        
    if operator not in ['+', '-', '*', '/']:
        print("invalid operator")
        continue

    try:
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
    except ValueError:
        print("invalid input, please enter numbers")
        continue

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            print(num1 / num2)
            
    print()
