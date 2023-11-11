def function(s:str):
    dic = {}
    for i in s.split(' '):
        if i not in dic.keys():
            dic[i] = 0
        dic[i] += 1
    for i in dic.keys():
        print(f'{i}:{dic[i]}')

function('I prefer apple and I like eatting apples')