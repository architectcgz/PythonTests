import random


def func(n):
    lst = [random.randint(1, 100) for i in range(n)]
    print('随机生成的列表为{}'.format(lst))
    average = sum(lst) / len(lst)
    return (average,) + tuple(filter(lambda x: x > average, lst))


n = int(input('请输入整数n:'))
print(f'输出为:{func(n)}')
