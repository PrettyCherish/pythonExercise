"""
@Time     :   2020/12/8 11:13
@Author   :   Winter
@File     :   theday.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
#  输入某年某月某日，判断这一天是这一年的第几天？
import datetime


def dayofyear():
    try:
        years = int(input("请输入指定的年份："))
        months = int(input("请输入指定的月份："))
        days = int(input("请输入指定的日："))
    except ValueError:
        print("输入有误，请输入整数：")
    data1 = datetime.date(year=years, month=months, day=days)
    data2 = datetime.date(year=years, month=1, day=1)
    return (data1 - data2).days+1


if __name__ == '__main__':
    days = dayofyear()
    print(days)
