import random

def function(n, m):
    result = tuple(random.randint(1, m) for _ in range(n))
    print('生成的元组为:{}'.format(result))
    result = tuple(x for x in result if x%2 != 0)
    print('过滤掉偶数整数后的元组为:{}'.format(result))



function(5,100)