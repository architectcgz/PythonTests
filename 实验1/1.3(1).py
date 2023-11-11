def func(n):
    if n <= 0:
        return None
    elif n == 1:
        return None
    elif n == 2:
        return [1,1]
    fib = [1, 1]
    while True:
        next = fib[-1] + fib[-2]
        if next >= n:
            break
        fib.append(next)

    return fib


n = int(input('请输入参数n:'))
print(f'斐波那契数列中小于参数 {n} 的所有值:{func(n)}')
