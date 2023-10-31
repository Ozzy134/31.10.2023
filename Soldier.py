class Soldier:

    def __init__(self, name, rank, num):
        self.name = name
        self.__rank = rank
        self.__num = num

    def get_rank(self):
        return self.__rank

    def get_num(self):
        return self.__num

    def promote(self):
        self.__rank = "ефрейтор"
        print(f'{self.name} повышен в звании, теперь он {self.__rank}')

    def demote(self):
        self.__rank = "рядовой"
        print(f'{self.name} понижен в звании, теперь он {self.__rank}')

soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
print('Создан новый игровой персонаж типа Solider с атрибутами:')
print(f'name: {soldier1.name}, soldier_rank: {soldier1.get_rank}, SSN: {soldier1.get_num}')
print(f'Персонаж {soldier1.name} имеет звание {soldier1.get_rank()}')
soldier1.promote()
soldier1.demote()


