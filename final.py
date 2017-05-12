import math
import random


class Circle:
    """Input a radius ( ex. Circle(23) and area, circumference, and diameter will be returned"""

    def __init__(self, radius):
        area = math.pi * radius * radius
        circum = 2 * math.pi * radius
        diam = 2 * radius
        print("area: ", area, "\ncirumference: ", circum, "\n diameter: ", diam)


class Triangle:
    """Call Triangle and it will return the hypotenuse for values of 1 to 20"""

    def __init__(self):
        upperlimit = 20
        a = 1
        b = 1
        while a <= upperlimit:
            a += 1
            b = 0
            while b <= upperlimit:
                c = (a * a) + (b * b)
                c = math.sqrt(c)

                b += 1
                if c >= 20:
                    break
                else:

                    print(a, "squared plus", b, "squared equals", c, "squared")


# Addition will run on its own because no initial requirements to run
class AdditionPractice:
    """Addition practice generates a pair of random integers and asks the user to add them.
    If the user is incorrect they will be asked to try again. If they are right the loop will end."""

    def __init__(self):

        intA = random.randint(1, 100)
        intB = random.randint(1, 100)
        intC = intA + intB
        answer = 0
        while intC != answer:
            try:
                print("What is", intA, "+", intB, "?")
                answer = int(input(":"))
                if answer != intC:
                    print("try again!")
                else:
                    print("Good Job!")
            except ValueError:
                pass


class NumberChecker:
    """NumberChecker will generate a list of 30 random integers between 1 and 10.
    If the number has a duplicate value it will print out a statement."""
    def __init__(self):
        list1 = []
        list2 = []

        while len(list1) < 30:
            list1.append(random.randint(1, 10))
        x = 0
        while x < 30:
            list2.append(list1[x])
            if list2.count(list1[x]) > 1:
                print(list1[x], "at index ", x, " is a duplicate")
            x += 1


class Rectangle:
    """Rectangle alone will take length and width as arguments.
    Rectangle.coords will take 4 values and pair them into coordinates."""

    def __init__(self, x, y):
        x = float(x)
        y = float(y)

        perimeter = x + x + y + y
        area = x * y
        print("perimeter: ", perimeter, "\narea: ", area)

    def coords(topleftx, toplefty, botrightx, botrighty):
        topleft = (topleftx, toplefty)
        botright = (botrightx, botrighty)
        if topleftx == botrighty:
            print("it's a square! woo!\n")
        perimeter = (toplefty * 2) + (botrightx * 2)
        area = toplefty * botrightx
        print("perimeter: ", perimeter, "\narea: ", area)


#Circle(5)
#Triangle()
#NumberChecker()
#AdditionPractice()
#Rectangle(10, 10)
#Rectangle.coords(0, 10, 10, 0)