# coding=utf-8
import random
# 1.求列表中相邻乘积最大的值以及下标


def get_mutiwonums(lis):
    flag, ans = 0, 0
    for i in range(len(lis)-1):
        if ans < lis[i]*lis[i+1]:
            ans = lis[i]*lis[i+1]
            flag = i
    print('列表中相邻数字乘积最大的值是{},对应下标是{} {}'.format(ans, flag, flag+1))


if __name__ == '__main__':
    L = [2, 4, 6, 3, 9, 11, -12]
    get_mutiwonums(L)
# 2.一行代码实现字典中key,value的反转。
    dictcase = {'id': 1, 'name': 'Tom'}
    dictcase1 = {key: value for value, key in dictcase.items()}
    print(dictcase1)
# 3.打乱一个排好序的列表
    # random.shuffle()会在原地操作，没有返回值。
    random.shuffle(L)
    print(L)

