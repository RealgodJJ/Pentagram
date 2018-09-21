# coding=utf-8
"""
    author: RealgodJJ
    function: draw a fractal tree
    version: 1.0
    date: 2018/09/21
"""
import turtle


def draw_branch(branch_length):
    if branch_length > 5:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        turtle.right(20)
        turtle.backward(branch_length)


def main():
    length = 100
    turtle.penup()
    turtle.left(90)
    turtle.backward(200)
    turtle.pendown()
    turtle.color('brown')
    draw_branch(length)
    turtle.exitonclick()
    pass


if __name__ == '__main__':
    main()
