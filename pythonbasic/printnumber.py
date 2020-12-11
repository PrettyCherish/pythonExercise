# coding=utf-8
# 用递归代替循环，输出1~100


def get_printnumber(n):
    if(n>0):
        get_printnumber(n-1)
        print(n)


if __name__ == '__main__':
    get_printnumber(100)
