def getPrime(n):
    # 所有数都初始化为素数
    is_prime = [True] * (n + 1)
    # 0和1不是素数，将其标记为False 2是素数，已标记为True
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            # 如果当前数i是素数，就将i的倍数标记为合数
            for i in range(i * i, n + 1, i):
                is_prime[i] = False

    # 收集所有素数
    primes = [i for i in range(2, n) if is_prime[i]]
    return primes


n = int(input('请输入一个大于2的自然数:'))
prime_numbers = getPrime(n)
print(f'小于该数字的所有素数组成的列表:{prime_numbers}')
