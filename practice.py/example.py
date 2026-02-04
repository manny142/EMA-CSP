def hello():
    print("hello world")

def hello_user(name):
    print(f"hello {name}")

def area(length, width):
    return length * width

side_one = 12
side_two = 8

print(f"the area of a rectangle with side of {side_one} and {side_two} is {area(side_one, side_two)}")
print(f"the area of the rectangle with side of 4 and 3 is {area(4,3)} ")
hello()
hello_user("katie")
hello_user("treyson")



def factorial(numder):
    total = 1
    for x in range(numder, 1, -1):
        total *= x
    return total

print(f"the factorial of 5 is {factorial(5)}")
print(f"the factorial of 5 is {factorial(3)}")
print(f"the factorial of 5 is {factorial(10)}")

