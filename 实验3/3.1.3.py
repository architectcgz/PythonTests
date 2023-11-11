class Vehicle:
    def __init__(self, max_speed, weight):
        self.__MaxSpeed = max_speed
        self.__weight = weight


class Bicycle(Vehicle):
    def __init__(self, max_speed, weight, height):
        super().__init__(max_speed,weight)
        self.__height = height

    def SetMaxSpeed(self, max_speed):
        self._Vehicle__MaxSpeed = max_speed

    def __setHeight(self, h):
        self.__height = h

    def __getHeight(self):
        return self.__height

    def __delHeight(self):
        del self.__height

    height = property(__getHeight, __setHeight, __delHeight)


def main():
    b = Bicycle(50, 40, 100)
    b.SetMaxSpeed(60)
    print('当前Bicycle的高度为:{}'.format(b.height))
    b.height = 120
    print('当前Bicycle的高度为:{}'.format(b.height))
    del b.height

if __name__ == '__main__':
    main()
