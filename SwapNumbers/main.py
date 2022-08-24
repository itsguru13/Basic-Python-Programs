x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

temp = x
x = y
y = temp

print("x: {} and y: {} swapped!".format(x, y))