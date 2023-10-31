import random

class MusicAlbum:

    def __init__(self, title, artist, relais_year, genere, tracklist):
        self.title = title
        self.artist = artist
        self.relais_year = relais_year
        self.genere = genere
        self.tracklist = tracklist

    def info(self):
        print('Название', self.title)
        print('Исполнитель', self.artist)
        print('Год', self.relais_year)
        print('Жанр', self.genere)
        print('Треки', self.tracklist)

    def play_random_track(self):
        return random.choice(self.tracklist)

ma = MusicAlbum('Berezovskiy', 'AK-47', '2009', 'Русский реп', ['Ak Ak', 'Витя и Максим', 'Але, это Пакситан', 'Братц', 'Пол второго feat Mad Bustaz', 'А вот так-то', 'Патриотическая', 'Ни чё не продаете', 'Школа feat Белый Рэп', 'Кругом тонирован', 'Максим на связи', 'Пландыши', 'У щет мен', 'Слышь, малыш', 'Эй, не пизди!', 'Ы да Ы'])
ma.info()
print('Сейчас играет:', ma.play_random_track())