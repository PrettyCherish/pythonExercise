# coding=utf-8
# 丑数是只包含质因数2，3，5的正整数（1也是特殊的丑数），请编写程序，找出第n个丑数


def get_uglynumber(n):
    l1, l2, l3 = 0, 0, 0
    s = [1]
    while(len(s)<n):
        m = min(2*(l1+1), 3*(l2+1), 5*(l3+1))
        s.append(m)
        if s[-1] == 2*(l1+1):
            l1 += 1
        if s[-1] == 3*(l2+1):
            l2 += 1
        if s[-1] == 5*(l3+1):
            l3 += 1
    return s[n-1]


if __name__ == '__main__':
    print(get_uglynumber(7))
