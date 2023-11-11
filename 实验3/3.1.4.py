class MyQueue:
    def __init__(self, maxSize):
        self.__data = [None] * maxSize
        self.__size = maxSize
        self.__current = 0

    def isEmpty(self):
        return self.__current == 0

    def isFull(self):
        return self.__current == self.__size

    def getHead(self):
        if self.isEmpty():
            return None
        return self.__data[0]

    def enQueue(self, data):
        if self.isFull():
            return
        # 将元素都向右移动一个单位
        for i in range(self.__current, 0, -1):
            self.__data[i] = self.__data[i - 1]
        self.__data[0] = data
        self.__current += 1

    def deQueue(self):
        if not self.isEmpty():
            for i in range(self.__current - 1):
                self.__data[i] = self.__data[i + 1]
            self.__data[self.__current - 1] = None
            self.__current -= 1


def main():
    q = MyQueue(10)
    print(q.isFull())
    print(q.isEmpty())
    q.enQueue(1)
    q.enQueue(2)
    print(q.isEmpty())
    print(q.getHead())
    q.deQueue()
    print(q.getHead())


if __name__ == '__main__':
    main()
