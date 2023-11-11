import random


def _getRightInput():
    while True:
        user_input = input("请猜一个数字:");
        try:
            guess = int(user_input)
            return guess
        except ValueError:
            print('输入有误，请输入不包含其他字符的数字')


def _guessNumber_if():
    print("这是一个猜数字的游戏".center(20, '-'))
    print("数字从1-10之间随机生成".center(20, '-'))
    num = random.randint(1, 10)
    guess = _getRightInput()
    if guess < num:
        print('too small')
        print(f'你猜错了!答案是{num}')
    elif guess > num:
        print('too large')
        print(f'你猜错了!答案是{num}')
    else:
        print('恭喜你猜对了！')


_guessNumber_if()
