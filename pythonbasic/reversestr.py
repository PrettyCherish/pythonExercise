# coding=utf-8
# 用函数实现字符串反转


def get_reversestr(str):
    ls = list(str)
    end = len(ls) - 1
    begin = 0
    while(begin<end):
        ls[begin],ls[end] = ls[end],ls[begin]
        begin += 1
        end -= 1
    return ''.join(ls)


if __name__ == '__main__':
    s = 'abcdefg'
    print(get_reversestr(s))
    print(s[::-1])  # 使用系统方法反转
