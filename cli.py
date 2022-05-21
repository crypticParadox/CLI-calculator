# CLI calculator
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide

print("select an operation to perfom")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

Selection = input("Input your Selection:")

if Selection == "1":
    num1 = input("Your first number:")
    num2 = input("Your second value:")
    print(str(int(num1) + int(num2)))
elif Selection =="2":
    num1 = input("Your first number:")
    num2 = input("Your second value:")
    print(str(int(num1) - int(num2)))
elif Selection =="3":
    num1 = input("Your first number:")
    num2 = input("Your second value:")
    print(str(int(num1) + int(num2)))
elif Selection =="4":
    num1 = input("Your first number:")
    num2 = input("Your second value:")
    print(str(int(num1) + int(num2)))
elif Selection =="5":
    num1 = input("Your first number:")
    num2 = input("Your second value:")
    print(str(int(num1) % int(num2)))
else: 
    print ("invalid Entry")

