# coding=utf-8
str = "abicdfeboxyz"
print(str)
strtolist = list(str)
begin = 0
end = len(strtolist) - 1
while begin < end:
    while strtolist[begin] not in 'aeiou':
        begin += 1
    while strtolist[end] not in 'aeiou':
        end -= 1
    if begin < end:
        strtolist[begin], strtolist[end] = strtolist[end], strtolist[begin]
        begin += 1
        end -= 1

print(''.join(strtolist))

