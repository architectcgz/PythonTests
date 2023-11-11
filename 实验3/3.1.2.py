class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.id = emp_id
        self.salary = salary

    def pay(self):
        return self.salary

    def show(self):
        return f'姓名:{self.name},编号:{self.id}'


class Manager(Employee):
    def __init__(self, name, emp_id, salary, bonus):
        super().__init__(name, emp_id, salary)
        self.bonus = bonus

    # 主管的工资为基本工资+津贴
    def pay(self):
        return self.salary + self.bonus

    def show(self):
        print(f'{super().show()},职位:主管')


class Salesman(Employee):
    def __init__(self, name, emp_id, salary, sales):
        super().__init__(name, emp_id, salary)
        self.sales = sales

    # 销售员的月薪是基本工资+销售额的5%
    def pay(self):
        return self.salary + self.sales * 0.05

    def show(self):
        super().show()
        print(f'{super().show()},职位:销售员')


def main():
    a = Manager('王经理', 1, 8000, 3000)
    b = Salesman('张三', 2, 5000, 6000)
    a.show()
    print(f'月薪{a.pay()}')
    b.show()
    print(f'月薪{b.pay()}')


if __name__ == '__main__':
    main()
