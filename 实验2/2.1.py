import random


def solution1():
    s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()') for i in range(1000))
    value_cnt = {}
    for i in range(len(s)):
        if s[i] not in value_cnt.keys():
            value_cnt[s[i]] = 0
        value_cnt[s[i]] += 1
    print(value_cnt)


def solution2():
    s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()') for i in range(1000))
    value_cnt = {letter: s.count(letter) for letter in list(s)}
    print(value_cnt)


def main():
    solution1()
    print()
    print()
    solution2()


if __name__ == '__main__':
    main()
