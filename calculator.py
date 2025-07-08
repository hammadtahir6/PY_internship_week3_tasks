try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("enter second number: "))
    operator = input("select operator (+, -, /, *, %, **)")
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    elif operator == "**":
        print(first_number ** second_number)
    elif operator == "%":
        print(first_number % second_number)
    else:
        print("invalid Operator")

except ZeroDivisionError:
    print("Zero division error is not allowed")
except ValueError:
    print("Enter valid numerical number")
    