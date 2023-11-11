import os
import re


class Student:
    def __init__(self, student_id: int, name: str, gender: str, age: int, grades: dict):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age
        self.grades = grades
        self.avg_grade = sum(grades.values()) / len(grades)

    def __str__(self):
        grade_str = ', '.join([f'{key}:{value}' for key, value in self.grades.items()])
        return f'{self.student_id},{self.name},{self.age},{self.gender},{grade_str},平均成绩{self.avg_grade:.3f}'

    def modifyGrade(self, key, value):
        self.grades[key] = value


class Class:
    def __init__(self):
        self.students = []
        self.readFile(f'{os.curdir}/students.txt')

    def readFile(self, filepath):
        with open(filepath, encoding='UTF-8') as file:
            first_line = file.readline()
            info = re.split(r'\s+', first_line.strip())
            column_num = len(info)
            # 课程数量
            class_num = column_num - 4
            dic_keys = info[-class_num:]
            # 读取文件的每一行
            for line in file:
                # 去掉换行符
                line = line.strip()
                stu_info = re.split(r'\s+', line)
                dic = {k: int(v) for k, v in zip(dic_keys, stu_info[-class_num:])}
                student = Student(*stu_info[:column_num - class_num], dic)
                self.students.append(student)
            self.students.sort(key=lambda x: x.avg_grade, reverse=True)

    def __str__(self):
        student_strings = [f'{student},排名:{i + 1}' for i, student in enumerate(self.students)]
        return '\n'.join(student_strings)


if __name__ == "__main__":
    a = Class()
    print(a)
