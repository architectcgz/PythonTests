def function_System(setA: set, setB: set):
    print(f'交集: {setA.intersection(setB)}')
    print(f'setA对于setB的差集: {setA.difference(setB)}')
    print(f'setB对于setA的差集: {setB.difference(setA)}')
    print(f'并集: {setA.union(setB)}')


class MySet:
    def __init__(self, *args):
        self.__items = []
        for i in args:
            if i not in self.__items:
                self.__items.append(i)

    def __str__(self):
        str_repr = '{' + ', '.join(map(str, self.__items)) + '}'
        return str_repr

    def intersection(self, other_set):
        common_items = []
        for item in self.__items:
            if item in other_set.__items and item not in common_items:
                common_items.append(item)
        return MySet(*common_items)

    def difference(self, other_set):
        different_set = []
        for i in self.__items:
            if i in self.__items and i not in other_set.__items:
                different_set.append(i)
        return MySet(*different_set)
    def union(self,other_set):
        union_set = self.__items+other_set.__items
        return MySet(*union_set)

def function_SelfDefine(setA:MySet,setB:MySet):
    print(f'交集: {setA.intersection(setB)}')
    print(f'setA对于setB的差集: {setA.difference(setB)}')
    print(f'setB对于setA的差集: {setB.difference(setA)}')
    print(f'并集: {setA.union(setB)}')





def main():
    # 例子的用法：
    set_1 = {1, 2, 3, 4}
    set_2 = {3, 4, 5, 6}
    set1 = MySet(1, 2, 3, 4)
    set2 = MySet(3, 4, 5, 6)
    function_System(set_1, set_2)
    function_SelfDefine(set1,set2)


if __name__ == '__main__':
    main()
