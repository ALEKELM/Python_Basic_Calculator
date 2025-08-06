def calculator(expression):

    operators = ["+","-","*","/"]
    # remove the blanck spaces from the input
    expression = expression.replace(" ", "")

    for operator in operators:
        if operator in expression:
            parts = expression.split(operator)
            if len(parts) == 2:
                # Convert the parts to float for calculation
                num1 = float(parts[0])
                num2 = float(parts[1])
               
                # Perform the calculation based on the operator
                if operator == '+':
                    return num1 + num2
                elif operator == '-':
                    return num1 - num2
                elif operator == '*':
                    return num1 * num2
                elif operator == '/':
                    if num2 != 0:
                        return num1 / num2
                    else:
                        return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operator or expression format."             
def main():
    print("Hello User! Welcome to the Basic Calculator.")                    
    while True:
    # basic_calculator.py
    # This is a simple calculator program that performs basic arithmetic operations.
        expression = input("Enter a mathematical expression (e.g., 2 + 3 or 'leave' to exit): ")
        if expression.lower() == 'leave':
            print("Thank you for using the Basic Calculator. Goodbye!")
            break
        
        result = calculator(expression)

        if isinstance(result, str):
            print(result)
        elif result.is_integer():
            print(f"The result of your expression is: {int(result)}")
        else:
            print(f"The result of your expression is: {result:.2f}")  

        if result is None:
            print("Invalid expression. Please try again.")

main()                