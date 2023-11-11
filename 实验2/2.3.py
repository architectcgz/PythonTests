import random


def function(n, m):
    s = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()0123456789'
    lst = [[''.join(random.choices(s, k=random.randint(1, m)))] for _ in range(n)]
    print('生成的列表为:{}'.format(lst))
    lst.sort(key=lambda x: len(x[0]), reverse=True)
    print('按照字符串长度排序后的结果为:{}'.format(lst))


function(3, 6)
