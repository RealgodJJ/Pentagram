# coding=utf-8
"""
    author: RealgodJJ
    function: BMR Calculator
    version: 1.0
    date: 2018/09/21
"""


def main():
    gender = '男'
    weight = 72
    height = 175
    age = 23
    if gender == '男':
        bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
    elif gender == '女':
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1

    if bmr != -1:
        print('BMR: ', bmr)
    else:
        print('暂不支持该性别')


if __name__ == '__main__':
    main()
