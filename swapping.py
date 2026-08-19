# Function Declaration
def swap(a, b):

    # Function Definition
    print("The numbers before swapping:", a, b)

    temp = a
    a = b
    b = temp

    print("The numbers after swapping:", a, b)


# Function Call
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

swap(a, b)