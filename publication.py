class Publicaton:
    a = 'a'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print('Название:', self.title)
        print(f'Автор: {self.author}')
        print(f'year: {self.year}')

class Book(Publicaton):

    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f'ISBN: {self.isbn}')

class Magazin(Publicaton):

    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        super().display()
        print(f'Номер выпуска: {self.issue_number}')

# p = Publicaton('sdfsdfsdf', 'dsfsdfsdfs', '1995')
# p.display()
# d = Book('Чебурашка', 'Народная', 1995, 12312312)
# d.display()
m = Magazin('dfsfdsfd', 'sfdsdfssdf', 1975, 5)
m.display()