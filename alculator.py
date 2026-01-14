"""
Simple calculator.
Supports +, -, *, / operations.
Handles negative numbers like 3 * -5 or 5 - -2.
Returns error messages for invalid input.
"""



def calculate(expression:str):

    expression = expression.replace(" ", "")
    operators = ["+", "-", "*", "/"]
    found_operator = None 
    
    for i, ch in enumerate(expression):
        if ch in operators:
            if ch == "-" and (i==0 or expression[i-1] in operators):
                continue
            found_operator = ch
            break
    if found_operator is None:
        return "error: operator not found"
    
    try:
        left_number , right_number = expression.split(found_operator,1)
        left_number = float(left_number)
        right_number = float(right_number)
        if found_operator == "+":
            return left_number + right_number
        elif found_operator == "-":
            return left_number - right_number
        elif found_operator == "*":
            return left_number * right_number
        elif found_operator == "/": 
            if right_number == 0:   
                return "error: division by zero"
            else:
                return left_number / right_number 
        else:
            return "error: unknown operator"
    except ValueError:
        return "error: invalid number format"


def main():
    expression = input("enter a mathematical expression: ")
    result = calculate(expression)
    print("result:", result)




if __name__ == "__main__":
    main()
