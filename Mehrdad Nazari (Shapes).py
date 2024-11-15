msg = "Hello my friend...\n"
print(msg)
attempt = 3
while attempt:
    shape = input("Please choose between square, rectangle, circle,triangle,diamond and trapezoid:... ")
    if shape == "square":
        while True:
            operation1 = input("Please choose between perimeter and area:... ")
            if operation1 == "perimeter":
                x = int(input("Please insert a square side:... "))
                print(x * 4)
                print("Thank you for follow me...")
                break
            elif operation1 == "area":
                x = int(input("Please insert a square side:... "))
                print(x * x)
                print("Thank you for follow me...")
                break
            else:
                print("Invalid input :(")
                continue
        break
    elif shape == "rectangle":
        while True:
            operation2 = input("Please choose between perimeter and area:... ")
            if operation2 == "perimeter":
                x2 = int(input("Please insert your 1st number:... "))
                y2 = int(input("Please insert your 2nd number:... "))
                print((x2 + y2) * 2)
                print("Thank you for follow me...")
                break
            elif operation2 == "area":
                x2 = int(input("Please insert your 1st number:... "))
                y2 = int(input("Please insert your 2nd number:... "))
                print(x2 * y2)
                print("Thank you for follow me...")
                break
            else:
                print("Invalid input :(")
        break
    elif shape == "circle":
        while True:
            operation3 = input("Please choose between perimeter and area:... ")
            if operation3 == "perimeter":
                x3 = int(input("Please insert diameter of the circle:... "))
                print(x3 * 3.14)
                print("Thank you for follow me...")
                break
            elif operation3 == "area":
                x3 = int(input("Please insert radius of the circle:... "))
                print(x3 * x3 * 3.14)
                print("Thank you for follow me...")
                break
            else:
                print("Invalid input :(")
        break
    elif shape == "triangle":
        while True:
            operation4 = input("Please choose between perimeter and area:... ")
            if operation4 == "perimeter":
                x4 = int(input("Please insert a triangle side:... "))
                print(x4 + x4 + x4)
                print("Thank you for follow me...")
                break
            elif operation4 == "area":
                x4 = int(input("Please insert base of triangle:... "))
                y4 = int(input("Please insert height of triangle:... "))
                print((x4 * y4) // 2)
                print("Thank you for follow me...")
                break
            else:
                print("Invalid input :(")
        break
    elif shape == "diamond":
        while True:
            operation5 = input("Please choose between perimeter and area:... ")
            if operation5 == "perimeter":
                x5 = int(input("Please insert a diamond side:... "))
                print(x5 * 4)
                print("Thank you for follow me...")
                break
            elif operation5 == "area":
                x5 = int(input("Please insert large diameter of diamond:... "))
                y5 = int(input("Please insert small diameter of diamond:... "))
                print((x5 * y5) / 2)
                print("Thank you for follow me...")
                break
            else:
                print("Invalid input :(")
        break
    elif shape == "trapezoid":
        while True:
            operation6 = input("Please choose between perimeter and area:... ")
            if operation6 == "perimeter":
                a = int(input("Please insert the 1st side:... "))
                b = int(input("Please insert the 2nd side:... "))
                c = int(input("Please insert the 3rd side:... "))
                d = int(input("Please insert the 4th side:... "))
                print(a + b + c + d)
                print("Thank you for follow me...")
                break
            elif operation6 == "area":
                a = int(input("Please insert small diameter of trapezoid:... "))
                b = int(input("Please insert large diameter of trapezoid:... "))
                h = int(input("Please insert height of trapezoid:... "))
                print(((a + b) * h) / 2)
                print("Thank you for follow me...")
                break
            else:
                print("Invalid input :(")
        break
    else:
        print("Invalid input\n")
        attempt -= 1
        print(f"You have {attempt} attempt left")
        if attempt == 0:
            print("Have a good day...")
            exit()