from math import sqrt

# Looking for errors in input
try:
    # Enter a, b, c
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    # Discriminant
    D = b**2 - 4*a*c
    print(f"Discriminant = {D}")

    # Finding x
    if D < 0:
        print("No solutions")
    elif D == 0:
        # Finding x
        x = -b / 2*a
        print(f"x = {x}")
    else:
        # Finding x1, x2
        x1 = (-b + sqrt(D)) / 2*a
        x2 = (-b - sqrt(D)) / 2*a
        print(f"x1 = {x1}\nx2 = {x2}")
except:
    print("Invalid input")
