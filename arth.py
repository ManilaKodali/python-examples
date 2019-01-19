num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/:")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
     print("input character is not recognised!")

print(num1 , ch , num2, ":",result)


