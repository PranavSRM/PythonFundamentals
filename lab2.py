# Lab 2: Conditional and Logical Statements
#
# if, elif, and else are used for conditional statements.
# and, or, and not are used for logical statements.

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs improvement")