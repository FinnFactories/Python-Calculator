print("CALCULATOR")
while True:
    try:
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        op = input("Operator(add-subtract-multiply-divide-exponent): ")
        if op == "add":
                print(num1+num2)
        elif op == "multiply":
                print(num1*num2)
        elif op == "divide":
                print(num1/num2)
        elif op == "subtract":
                print(num1-num2)
        elif op == "exponent":
                print(num1**num2)
        else:
                print("INVALID OPERATOR")
    except ZeroDivisionError:
           print("Can't Divide By Zero")
