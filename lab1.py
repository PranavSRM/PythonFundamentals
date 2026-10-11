# Lab 1: User Input and Output
#
# input() receives text.
# int() converts the text to an integer.
# float() converts the text to a floating-point number.
# f"..." lets you insert variables into strings.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))

print(f"Name: {name}")
print(f"Age next year: {age + 1}")
print(f"Height: {height:.2f} m")