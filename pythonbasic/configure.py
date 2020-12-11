"""
@Time     :   2020/10/15 15:57
@Author   :   Winter
@File     :   configure.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
print("猩红全是2x的情况下提升如下：")
orghp3 = 1600
orgdamage3 = 125
orghp6 = 3800
orgdamage6 = 400
orghp9 = 6666
orgdamage9 = 1000
nowbasichp3 = 1000
nowbasichp6 = 1750
nowbasichp9 = 2500
nowbasicdamage3 = 80
nowbasicdamage6 = 180
nowbasicdamage9 = 400
nowhp3 = nowbasichp3*(1+0.12*6)
nowhp6 = nowbasichp6*(1+0.12*12)
nowhp9 = nowbasichp9*(1+0.12*16)
nowdamage3 = nowbasicdamage3*(1+0.12*6)
nowdamage6 = nowbasicdamage6*(1+0.12*12)
nowdamage9 = nowbasicdamage9*(1+0.12*16)
levelhp3 = nowhp3/orghp3
levelhp6 = nowhp6/orghp6
levelhp9 = nowhp9/orghp9
leveldamage3 = nowdamage3/orgdamage3
leveldamage6 = nowdamage6/orgdamage6
leveldamage9 = nowdamage9/orgdamage9
print("三腥红生命值提升：", levelhp3)
print("三腥红攻击力提升：", leveldamage3)
print("六腥红生命值提升：", levelhp6)
print("六腥红攻击力提升：", leveldamage6)
print("九腥红生命值提升：", levelhp9)
print("九腥红攻击力提升：", leveldamage9)
