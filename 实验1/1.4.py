def connect_strings(s1, s2):
    # 使用 lambda 表达式找到两个字符串首尾交叉的最大子串长度
    max_len = lambda s1, s2: max([i for i in range(len(s1)+1) if s1[-i:] == s2[:i]])
    # 连接两个字符串，首尾交叉部分只保留一份
    return s1 + s2[max_len(s1, s2):]


s1 = input('请输入第一个字符串:')
s2 = input('请输入第二个字符串:')
print(connect_strings(s1, s2))