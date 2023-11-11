import random


def getRandomString(randomLength=8):
    """
    生成一个指定长度的随机字符串
    """
    digits = '0123456789'
    ascii_letters = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_list = [random.choice(digits + ascii_letters) for _ in range(randomLength)]
    random_str = ''.join(str_list)
    return random_str


def main():
    with open('test3.2.1.txt', mode='r+') as file:
        for i in range(10):
            file.seek(0)
            string_readed = file.read().split('\n')
            print('字符串的个数为:{}'.format(len(string_readed)))
            random_string = getRandomString()
            file.write(random_string + '\n')


if __name__ == '__main__':
    main()
