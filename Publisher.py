class Publisher:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        print(f'Название: {self.name}')
        print(f'Расположение: {self.location}')

    def publish(self, message):
        print(f'Издание в печати: {message}')

class BookPublisher(Publisher):

    def __init__(self, name, location, num):
        super().__init__(name, location)
        self.num = num
        
    def get_info(self):
        print(f'Название: {self.name}')
        print(f'Расположение: {self.location}')
        print(f'Количевство авторов: {self.num}')

class NewspaperPublisher(Publisher):

    def __init__(self, name, location, num1):
        super().__init__(name, location)
        self.num = num1

    def get_info(self):
        print(f'Название: {self.name}')
        print(f'Расположение: {self.location}')
        print(f'Количевство авторов: {self.num}')

publisher = Publisher("АБВГД Пресс", "Москва")
publisher.get_info()
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.get_info()
book_publisher.publish("Приключения Чебурашки")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.get_info()
newspaper_publisher.publish("Новая версия Midjourney будет платной")
