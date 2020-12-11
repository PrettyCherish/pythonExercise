# coding=utf-8
# 返回字符串中第一个不重复的字母和位置
# 出错点：1. .format(i,s[i])写成了.format(i,s(i))
#        2. 刚写的时候，想当然的写成tupleaim[s[i]] += 1,未写if判断语句。


def get_firstchar(s):
    tupleaim = {}
    for i in range(len(s)):
        if s[i] in tupleaim:
            tupleaim[s[i]] += 1
        else:
            tupleaim[s[i]] = 1
    for i in range(len(s)):
        if tupleaim[s[i]] == 1:
            return '第一个不重复元素的下标是{},元素是{}'.format(i, s[i])
    return '不存在不重复的元素'


if __name__ == '__main__':
    s = 'aaggoowwpp'
    print(get_firstchar(s))
