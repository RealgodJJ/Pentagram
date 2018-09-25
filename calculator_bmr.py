# coding=utf-8
"""
    author: RealgodJJ
    function: BMR Calculator
    version: 1.0
    date: 2018/09/21
"""


def main():
    yes_or_no = input('是否退出程序(Y/N)？\n')

    while yes_or_no != 'Y':
        # gender = input('性别：')
        # weight = float(input('体重（kg）：'))
        # height = float(input('身高（cm）：'))
        # age = int(input('年龄：'))
        print('请输入以下信息，用空格分隔')
        try:
            input_str = input('性别 体重（kg） 身高（cm） 年龄：\n')
            str_list = input_str.split(' ')
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[3])

            if gender == '男':
                bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
            elif gender == '女':
                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
            else:
                bmr = -1

            if bmr != -1:
                print('您的性别：{}\n体重：{}千克\n身高：{}厘米\n年龄：{}'.format(gender, weight, height, age))
                print('您的基础代谢率: {}大卡'.format(bmr))
            else:
                print('暂不支持该性别')

            yes_or_no = input('是否退出程序(Y/N)？')
        # except TypeError:
        #     print("输入的数据类型有误！")
        except ValueError:
            print("请输入正确的信息！")
        except IndexError:
            print("输入的信息过少！")
        except:
            print("程序有误！")


if __name__ == '__main__':
    main()
