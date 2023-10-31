class Student:
    a = 'a'

    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def info(self):
        print(f'ФИО: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Класс: {self.grade}')
        print(f'Оценки: {self.scores}')
        print(f'Cредний балл: {self.averege_score()}')

    def averege_score(self):
        y = sum(self.scores)
        c = len(self.scores)
        return y / c

s = Student('Львов Андрей Валентинович', '20', '11', [4,5,2,2,3])
s.info()

