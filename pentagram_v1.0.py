"""
    Author: RealgodJJ
    Function: Draw a pentagram
    Version: 1.0
    Date: 09/19/2018
"""
import turtle


def main():
    count = 1
    length = 50
    while count <= 25:
        turtle.forward(length)
        turtle.right(144)
        if count % 5 == 0:
            length += 50
        count += 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()
