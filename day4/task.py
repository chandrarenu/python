#pyramid pattern using FOR loop

for i in range(1,8):
    for j in range(1, i+1):
        print(j,end="")
    print()
    
    
    
#pyramid pattern using WHILE loop

i = 1
while i<=5:
    j = 1
    while j<=i:
        print(j,end='')
        j += 1
    print()
    i += 1
        
#implement function in calculator


def calculator(a,b, operation):
    if operation == "+":
        result = a+b
    elif operation == "-":
        result = a -b
    elif operation == "*":
        result = a *b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
             raise ZeroDivisionError("Division by zero is not allowed.")
    else:
      raise ValueError("Invalid operation. Please enter +, -, *, or /.")
    return result

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /)")

try:
  result = calculator(a, b, operation)
  print(f"Result: {result}")
except Exception as e:
  print(f"Error: {e}")

            
  