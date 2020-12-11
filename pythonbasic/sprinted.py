# coding=utf-8
the_str = "12,33,44"

the_list = the_str.split(",")
print(the_list)

print(','.join(the_list))


the_dict = {'a': 'aa', 'b': 'bb', 'd': 'dd', 'e': 'ee'}
for key in the_dict:
    print("key is:", key)
    print("value is: ", the_dict[key])


for key, value in the_dict.items():
    print(key)
    print(value)


stu = [('张三',20), ('李四',15), ('王五',25), ('王吉',40)]
print(sorted(stu, key=lambda t:t[0], reverse=True))


def sort_stu(t):
    return t[1]


print(sorted(stu, key=sort_stu, reverse=True))


def get_listSort(data):
    startindex = 0
    endindex = 0
    count = len(data)
    while startindex + endindex < count:
        if data[startindex] == '-':
            data[startindex], data[count - endindex - 1] = data[count - endindex - 1], data[startindex]
            endindex = endindex + 1
        else:
            startindex = startindex + 1

    return data


data = ['-', '-', '+', '+', '+', '-', '+', '-', '+', '-', '-']
print(get_listSort(data))





