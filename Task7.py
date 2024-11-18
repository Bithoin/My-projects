class List:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9]

    def add_item(self, item):
        if item in self.items:
            print("Таке число вже є в списку")
        else:
            self.items.append(item)
            print(f"Число {item} було додано до списку.")

    def del_item(self, item):
        if item in self.items:
            self.items = [x for x in self.items if x != item]
            print(f"Усі вхождения числа {item} було видалено зі списку.")
        else:
            print("Такого числа немає в списку")

    def show_list(self):
        print("Список:", self.items)

    def show_list_reverse(self):
        print("Список у зворотньому порядку:", self.items[::-1])

    def check_item_list(self, item):
        if item in self.items:
            print("Таке число є у списку")
        else:
            print("Такого числа нема у списку")

    def replace_item_list(self, item, itemreplace, replace_all=False):
        if item not in self.items:
            print("Такого числа немає у списку")
            return

        if replace_all:
            self.items = [itemreplace if x == item else x for x in self.items]
            print(f"Усі вхождения числа {item} було замінено на {itemreplace}.")
        else:
            self.items[self.items.index(item)] = itemreplace
            print(f"Число {item} було замінено на {itemreplace}.")


lst = List()

while True:
    print("\nВиберіть дію:")
    print("1. Додати число до списку")
    print("2. Видалити всі входження числа з списку")
    print("3. Показати список")
    print("4. Показати список в оберненому порядку")
    print("5. Перевірити чи в списку є задане число")
    print("6. Замінити число в списку")
    print("7. Вийти")

    try:
        choice = int(input("Введіть номер дії: "))
    except ValueError:
        print("Будь ласка, введіть число від 1 до 7 ")
        continue

    if choice == 1:
        number_to_add = int(input("Введіть число для додавання: "))
        lst.add_item(number_to_add)
    elif choice == 2:
        number_to_remove = int(input("Введіть число для видалення: "))
        lst.del_item(number_to_remove)
    elif choice == 3:
        lst.show_list()
    elif choice == 4:
        lst.show_list_reverse()
    elif choice == 5:
        number_to_check = int(input("Введіть число для перевірки: "))
        lst.check_item_list(number_to_check)
    elif choice == 6:
        number_to_replace = int(input("Введіть число, яке хочете замінити: "))
        new_number = int(input("Введіть нове число: "))
        replace_all = input("Замінити всі входження? (так/ні): ").strip().lower() == 'так'
        lst.replace_item_list(number_to_replace, new_number, replace_all)
    elif choice == 7:
        print("Вихід...\n")
        break
    else:
        print("Будь ласка, оберіть правильний номер дії.")
