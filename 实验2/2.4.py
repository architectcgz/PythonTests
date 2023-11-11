import random

lst = [random.randint(1,100) for _ in range(10)]
print(f'原列表:{lst}')
print(f'包含原列表中所有元素的新列表:{lst[::]}')
print(f'包含原列表中所有元素的逆序列表:{lst[::-1]}')
print(f'具有偶数位置的元素列表:{lst[::2]}')