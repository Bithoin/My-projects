class Device:
    def __init__(self, price: float, serial_number: str, quantity: int):
        self._price = price
        self._serial_number = serial_number
        self._quantity = quantity

    def get_info(self):
        return f'''
Ціна: {self._price} грн
Серійний номер: {self._serial_number}
Кількість на складі: {self._quantity}
'''

    @classmethod
    def create_device(cls):
        while True:
            try:
                price = float(input("Введіть ціну девайсу (грн): "))
                serial_number = input("Введіть серійний номер: ")
                quantity = int(input("Введіть кількість: "))
                break
            except ValueError:
                print("Будь ласка, введіть правильні значення.")
        return cls(price, serial_number, quantity)


class CoffeeMachine(Device):
    def __init__(self, price: float, serial_number: str, quantity: int, power: str):
        super().__init__(price, serial_number, quantity)
        self._power = power

    @classmethod
    def create_device(cls):
        # Спочатку запитуємо дані базового класу
        device_info = Device.create_device()
        power = input("Введіть потужність кавомашини (Вт): ")
        return cls(device_info._price, device_info._serial_number, device_info._quantity, power)

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}Об\'єм кавомашини: {self._power}\n'


class MeatGrinder(Device):
    def __init__(self, price: float, serial_number: str, quantity: int, blade_types: str):
        super().__init__(price, serial_number, quantity)
        self._blade_types = blade_types

    @classmethod
    def create_device(cls):
        device_info = Device.create_device()
        blade_types = input("Введіть типи лез: ")
        return cls(device_info._price, device_info._serial_number, device_info._quantity, blade_types)

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}Тип лез: {self._blade_types}\n'


class Blender(Device):
    def __init__(self, price: float, serial_number: str, quantity: int, noise_level: str):
        super().__init__(price, serial_number, quantity)
        self._noise_level = noise_level

    @classmethod
    def create_device(cls):
        device_info = Device.create_device()
        noise_level = input("Введіть рівень шуму блендера (дБ): ")
        return cls(device_info._price, device_info._serial_number, device_info._quantity, noise_level)

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}Рівень шуму блендера: {self._noise_level}\n'


class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_coffee_machine(self):
        coffee_machine = CoffeeMachine.create_device()
        self.devices.append(coffee_machine)

    def add_blender(self):
        blender = Blender.create_device()
        self.devices.append(blender)

    def add_meat_grinder(self):
        meat_grinder = MeatGrinder.create_device()
        self.devices.append(meat_grinder)

    def show_devices(self):
        print("\nІнформація про всі пристрої:")
        for device in self.devices:
            print(device.get_info())

    def run(self):
        while True:
            print("\nВиберіть тип пристрою для додавання:")
            print("1. Кавомашина")
            print("2. Блендер")
            print("3. М'ясорубка")
            print("4. Вихід")

            choice = input("Ваш вибір: ")

            if choice == '1':
                self.add_coffee_machine()
            elif choice == '2':
                self.add_blender()
            elif choice == '3':
                self.add_meat_grinder()
            elif choice == '4':
                print("Вихід...")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")

            self.show_devices()

manager = DeviceManager()
manager.run()


class Ship:
    def __init__(self, name: str, length: float, width: float, displacement: float):
        self._name = name
        self._length = length
        self._width = width
        self._displacement = displacement

    def get_info(self):
        return f'''
Назва: {self._name}
Довжина: {self._length} м
Ширина: {self._width} м
Водотоннажність: {self._displacement} т
'''

    @classmethod
    def create_ship(cls):
        name = input("Введіть назву корабля: ")
        while True:
            try:
                length = float(input("Введіть довжину корабля (м): "))
                width = float(input("Введіть ширину корабля (м): "))
                displacement = float(input("Введіть водотоннажність (т): "))
                break
            except ValueError:
                print("Будь ласка, введіть правильні значення.")
        return cls(name, length, width, displacement)


class Frigate(Ship):
    def __init__(self, name: str, length: float, width: float, displacement: float, armament: str):
        super().__init__(name, length, width, displacement)
        self._armament = armament

    @classmethod
    def create_ship(cls):
        ship_info = Ship.create_ship()
        armament = input("Введіть озброєння фрегата: ")
        return cls(ship_info._name, ship_info._length, ship_info._width, ship_info._displacement, armament)

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}Озброєння: {self._armament}\n'


class Destroyer(Ship):
    def __init__(self, name: str, length: float, width: float, displacement: float, missile_system: str):
        super().__init__(name, length, width, displacement)
        self._missile_system = missile_system

    @classmethod
    def create_ship(cls):
        ship_info = Ship.create_ship()
        missile_system = input("Введіть систему ракетного озброєння есмінця: ")
        return cls(ship_info._name, ship_info._length, ship_info._width, ship_info._displacement, missile_system)

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}Система ракетного озброєння: {self._missile_system}\n'


class Cruiser(Ship):
    def __init__(self, name: str, length: float, width: float, displacement: float, role: str):
        super().__init__(name, length, width, displacement)
        self._role = role

    @classmethod
    def create_ship(cls):
        ship_info = Ship.create_ship()
        role = input("Введіть роль крейсера: ")
        return cls(ship_info._name, ship_info._length, ship_info._width, ship_info._displacement, role)

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}Роль: {self._role}\n'


class ShipManager:
    def __init__(self):
        self.ships = []

    def add_frigate(self):
        frigate = Frigate.create_ship()
        self.ships.append(frigate)

    def add_destroyer(self):
        destroyer = Destroyer.create_ship()
        self.ships.append(destroyer)

    def add_cruiser(self):
        cruiser = Cruiser.create_ship()
        self.ships.append(cruiser)

    def show_ships(self):
        print("\nІнформація про всі кораблі:")
        for ship in self.ships:
            print(ship.get_info())

    def run(self):
        while True:
            print("\nВиберіть тип корабля для додавання:")
            print("1. Фрегат")
            print("2. Есмінець")
            print("3. Крейсер")
            print("4. Вихід")

            choice = input("Ваш вибір: ")

            if choice == '1':
                self.add_frigate()
            elif choice == '2':
                self.add_destroyer()
            elif choice == '3':
                self.add_cruiser()
            elif choice == '4':
                print("Вихід...\n")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")

            self.show_ships()

manager = ShipManager()
manager.run()

class Money:
    def __init__(self, dollars=0, cents=0):
        self.set_values(dollars, cents)

    def set_values(self, dollars, cents):
        total_cents = dollars * 100 + cents
        self._dollars = total_cents // 100
        self._cents = total_cents % 100

    def get_dollars(self):
        return self._dollars

    def get_cents(self):
        return self._cents

    def __str__(self):
        return f"{self._dollars}.$ {self._cents:02d}¢"

    def add(self, other):
        if isinstance(other, Money):
            self.set_values(self._dollars + other.get_dollars(), self._cents + other.get_cents())

    def subtract(self, other):
        if isinstance(other, Money):
            total_cents = (self._dollars * 100 + self._cents) - (other.get_dollars() * 100 + other.get_cents())
            if total_cents < 0:
                raise ValueError("Недостатньо грошеq для виконання операції.")
            self.set_values(total_cents // 100, total_cents % 100)

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def set_price(self, price):
        self._price = price

    def discount(self, amount):
        self._price.subtract(amount)

    def get_info(self):
        return f"Продукт: {self._name}, Ціна: {self._price}"

class Store:
    @staticmethod
    def run():
        m1 = Money(10, 50)
        print(m1)

        m2 = Money(5, 75)
        print(m2)

        m1.add(m2)
        print(f"Сума після додавання: {m1}")

        bread = Product("Хліб", Money(3, 99))
        print(bread.get_info())

        discount = Money(1, 49)
        bread.discount(discount)
        print(bread.get_info())

Store.run()
