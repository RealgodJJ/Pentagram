"""
    Author: RealgodJJ
    Function: Draw a pentagram
    Version: 1.0
    Date: 09/19/2018
"""
import turtle


def draw_pentagram(size, speed):
    count = 1

    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        turtle.speed(speed)
        count += 1

    if size <= 250:
        size += 50
        speed += 0.5
        draw_pentagram(size, speed)


def main():
    length = 50
    speed = 3
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    draw_pentagram(length, speed)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
