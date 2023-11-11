import re


def function(s:str):
    fmt = re.compile(r'(\b\w{3}\b)')
    result = fmt.findall(s.strip())
    print('这段英文中所有长度为 3 个字母的单词:')
    print(*result)

i = input('请输入一段英文:')
function(i)