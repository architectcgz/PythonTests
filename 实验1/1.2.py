import random


def _getRightInput():
    while True:
        user_input = input("请猜一个数字:");
        try:
            guess = int(user_input)
            return guess
        except ValueError:
            print('输入有误，请输入不包含其他字符的数字')


def _guessNumber_while():
    while True:
        chance = 6
        print("这是一个猜数字的游戏".center(20, '-'))
        print("数字从1-100之间随机生成".center(20, '-'))
        num = random.randint(1, 100)
        guess = _getRightInput()
        while guess != num:
            chance -= 1
            if guess < num:
                print(f'too small\n你还剩{chance}次机会')
            else:
                print(f'too large\n你还剩{chance}次机会')
            if chance == 0:
                print(f'猜数字机会已用完!正确答案是: {num}')
                break
            guess = _getRightInput()
        if guess == num:
            print('right!')  # 跳出循环即成功

        ctn = input('是否继续？(Y/N):')
        if ctn == 'N':
            print('感谢游玩!再见！')
            break


_guessNumber_while()
