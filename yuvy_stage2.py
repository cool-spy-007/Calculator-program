num_1 = int(input("Enter the number: "))
num_2 = int(input("Enter the number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+": 
    result = num_1 + num_2
    print(result)
elif operator == "-":
    result = num_1 - num_2
    print(result)
elif operator == "*":
    result = num_1 * num_2
    print(result)
elif operator == "/":
    result = num_1 / num_2
    print(result)
else:
    print(f"{operator} is not found")

if (result > 0):
    print("Positive")
elif (result < 0):
    print ("Negative")
else:
    print("Zero")