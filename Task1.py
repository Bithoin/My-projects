class Auto:
    def __init__(self, carmodel: str, releaseyear: int, enginevolume: float, carcolor: str, carprice: float):
        self.__carModel = carmodel
        self.__releaseYear = releaseyear
        self.__engineVolume = enginevolume
        self.__carColor = carcolor
        self.__carPrice = carprice
    def output(self):
        return f"""Модель автомобіля: {self.__carModel}
Рік випуску автомобіля: {self.__releaseYear}
Об'єм двигуна: {self.__engineVolume}
Колір автомобіля: {self.__carColor}
Ціна автомобіля: {self.__carPrice} $
"""
    @classmethod
    def create_auto(cls):
        fields = ["Модель автомобіля", "Рік випуску автомобіля", "Об'єм двигуна", "Колір автомобіля", "Ціна автомобіля"]
        car_data = []
        for field in fields:
            while True:
                value = input(f"Введіть {field}: ")
                if field == "Рік випуску автомобіля":
                    try:
                        value = int(value)
                        break
                    except ValueError:
                        print("Будь ласка, введіть коректний рік (число).")
                elif field in ["Об'єм двигуна", "Ціна автомобіля"]:
                    try:
                        value = float(value)
                        break
                    except ValueError:
                        print(f"Будь ласка, введіть коректний {field.lower()} (число).")
                else:
                    break
            car_data.append(value)
        return cls(car_data[0], car_data[1], car_data[2], car_data[3], car_data[4])

h1 = Auto.create_auto()
print(h1.output())

class Book:
    def __init__(self, title: str, year: int, publisher: str, genre: str, author: str, price: float):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def output(self):
        return f"""Назва книги: {self.__title}
Рік видання: {self.__year}
Видавець: {self.__publisher}
Жанр: {self.__genre}
Автор: {self.__author}
Ціна: {self.__price} грн
"""
    @classmethod
    def create_book(cls):
        fields = ["Назва книги", "Рік видання", "Видавець", "Жанр", "Автор", "Ціна"]
        book_data = []
        for field in fields:
            while True:
                value = input(f"Введіть {field}: ")
                if field == "Рік видання":
                    try:
                        value = int(value)
                        break
                    except ValueError:
                        print("Будь ласка, введіть коректний рік (число).")
                elif field == "Ціна":
                    try:
                        value = float(value)
                        break
                    except ValueError:
                        print("Будь ласка, введіть коректну ціну (число).")
                else:
                    break
            book_data.append(value)
        return cls(book_data[0], book_data[1], book_data[2], book_data[3], book_data[4], book_data[5])

book = Book.create_book()
print(book.output())

class Stadium:
    def __init__(self, name: str, opening_date: str, country: str, city: str, capacity: int):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def output(self):
        return f"""Назва стадіону: {self.__name}
Дата відкриття: {self.__opening_date}
Країна: {self.__country}
Місто: {self.__city}
Вмісткість: {self.__capacity} місць
"""
    @classmethod
    def create_stadium(cls):
        fields = ["Назва стадіону", "Дата відкриття", "Країна", "Місто", "Вмісткість"]
        stadium_data = []
        for field in fields:
            while True:
                value = input(f"Введіть {field}: ")
                if field == "Вмісткість":
                    try:
                        value = int(value)
                        break
                    except ValueError:
                        print("Будь ласка, введіть коректну вмісткість (число).")
                else:
                    break
            stadium_data.append(value)
        return cls(stadium_data[0], stadium_data[1], stadium_data[2], stadium_data[3], stadium_data[4])
    
stadium = Stadium.create_stadium()
print(stadium.output())