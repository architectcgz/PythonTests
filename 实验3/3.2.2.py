import re


def check(s:str):
    fmt = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$')
    codes = s.split(',')
    result = [x for x in codes if fmt.match(x)]
    if result:
        return result
    return None

print(check('bcdEF12＃@,ccword12'))