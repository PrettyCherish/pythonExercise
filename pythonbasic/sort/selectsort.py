# coding=utf-8
'''
    选择排序（升序）【不稳定排序】
    原理：
    1、给定一个列表，经过第一轮比较后，找到最小值，与第一个位置交换；
    2、接着对不包括第一个元素的剩下的元素，找到最小值，与第二个位置交换；
    3、重复该过程，直到进行比较的记录只有一个为止

    以 list = [5, 4, 2, 1, 3] 为例：
    第一次排序后： [1, 4, 2, 5, 3]
    第二次排序后： [1, 2, 4, 5, 3]
    第三次排序后： [1, 2, 3, 5, 4]
    第四次排序后： [1, 2, 3, 4, 5]

        时间复杂度：O(n**2)
        空间复杂度：O(1)

    :param lists:
    :return: lists
'''


def get_selectsort(l):
    for i in range(len(l)):
        flag = i
        for j in range(i+1, len(l)):
            if l[j] < l[flag]:
                 l[j], l[flag] = l[flag], l[j]
    return l


if __name__ == '__main__':
    l = [5, 4, 2, 1, 3]
    print(get_selectsort(l))
