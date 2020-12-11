# coding=utf-8
'''
插入排序（升序）【稳定排序】
原理：
1、假设初始时假设第一个记录，自成一个有序序列，其余的记录为无序序列；
2、从第二个记录开始，按记录大小，依次插入之前的有序序列中；
3、直到最后一个记录插入到有序序列中为止

以 list = [5, 4, 2, 1, 3] 为例：
第一步，插入5之后: [5], 4, 2, 1, 3
第二步，插入4之后: [4, 5], 2, 1, 3
第三步，插入2之后: [2, 4, 5], 1, 3
第四步，插入1之后: [1, 2, 4, 5], 3
第五步，插入3之后: [1, 2, 3, 4, 5]

时间复杂度: O(n) ~ O(n**2)  平均: O(n**2)
空间复杂度: O(1)

:param lists:
:return: lists
'''


def get_insertsort1(l):
    for i in range(len(l)):
        ans = i
        j = i-1
        while j >= 0:
            if l[ans] < l[j]:
                l[ans], l[j] = l[j], l[ans]
                ans = j
                j -= 1
            else:
                break
    return l


def get_insertsort2(lists):
    for i in range(len(lists)):
        key = lists[i]
        j = i-1
        while j >= 0:
            if key > lists[j]:
                lists[j+1] = key
                key = lists[j]
            j -= 1
    return lists


if __name__ == '__main__':
    l = [5, 4, 2, 1, 3]
    print(get_insertsort1(l))
    print(get_insertsort2(l))

