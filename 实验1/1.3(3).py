def func(str):
    if str == str[::-1]:
        return True
    else:
        return False



s = input('请输入一串字符:')
if func(s):
    print(f'{s}是回文')
else:
    print(f'{s}不是回文')
