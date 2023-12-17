#task to make calculator using operator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /)")

if operation == "+":
    result = a + b
    print("Result:", result)
elif operation == "-":
    result = a - b
    print("Result:", result)
elif operation == "*":
    result = a * b
    print("Result:", result)
elif operation == "/":
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

def calculator(a,b, operator):
    if operator == "+":
       result = a + b
    elif operator == "-":
        result = a-b
    
    elif operator == "*":
        result = a*b   
    
    elif operator == "/":
        result = a/b
    else:
        print("not matched")
    return result

print(calculator(12,5,'+'))
print(calculator(12,5,"-"))
print(calculator(12,5,"*"))
print(calculator(12,5,"/"))

calculator(12,3, "+")







