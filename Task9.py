import re
class Password:
    def __init__(self):
        self.__password = "01234567" # - приватний атребут делаетсья через __

    @property #Декоратор  використовується для створення властивостей об'єктів, які можна читати, але не можна змінювати напряму
    def password(self):
        return self.__password #властивість, яка дозволяє отримати поточний пароль (тільки для читання)
#позволяет вам получать доступ к приватной переменной __password  как к атрибуту объекта
    def set_password(self, current_password, new_password): #метод зміни паролю
        if current_password == self.__password:
            if self.is_valid_password(new_password):   #метод is_valid_password приймає аргумент new_password котрий із себе представляє новий пароль
                self.__password = new_password
                print("Пароль успішно змінено.")
            else:
                print("Новий пароль не відповідає вимогам.")
        else:
            print("Неправильний поточний пароль. Неможливо змінити пароль.")

    def is_valid_password(self, password):
        if len(password) < 8:
            return False
        if re.search(r"[+=;:\"'\\/\| ]", password):
            return False
        if re.match(r"^[A-Za-z0-9!@#$%^&*()-_+=<>?]{8,}$", password): # символ ^- строка должна начинаться с одного из символов, указанных в скобках
            return True                                                       # символ $ - строка длжн. заканчиваться с одного из симв →      ↑
        return False

class Login:
    def __init__(self):
        self.__login = "user"

    @property
    def login(self):
        return self.__login

    def set_login(self, current_password, password_instance, new_login): #метод зміни логіну, перевіряє, чи поточний пароль співпадає з введеним
        if current_password == password_instance.password:
            if self.is_valid_login(new_login):
                self.__login = new_login
                print("Логін успішно змінено.")
            else:
                print("Новий логін не відповідає вимогам.")
        else:
            print("Неправильний поточний пароль. Неможливо змінити логін.")

    def is_valid_login(self, login):     # - метод для перевірки нового логіну на відповідність вимогам
        if len(login) == 0 or len(login) > 20:
            return False
        if re.match(r"^[A-Za-z0-9_]{1,20}$", login):
            return True
        return False

class UserForm:
    def __init__(self):
        self.pswd = Password()     # при визове атрибута pswd визиваетсья класс password там
        self.lgn = Login()         # виполняються действия и результат записиваетсья в этот обект аналогично и с атрибутом lgn
    def view_credentials(self):         #Метод для відображення поточного логіна і пароля
        print(f"Поточний логін: {self.lgn.login}")    # вивод логина
        print(f"Поточний пароль: {self.pswd.password}")

    def change_login(self):  #проверка пользователя знает ли он пароль
        current_password = input("Введіть поточний пароль: ")    #ввод пароля в переменную current_password
        new_login = input("Введіть новий логін: ")  # ввод логина в переменную new_login
        self.lgn.set_login(current_password, self.pswd, new_login) #обращается к атрибуту lgn который является экземпляром класса Login.
                                                                    #lgn.set_login -обращения к методу set.login и передаються представленние аргументи
    def change_password(self):  #смена логина и пароля
        current_password = input("Введіть поточний пароль: ")
        new_password = input("Введіть новий пароль: ")
        self.pswd.set_password(current_password, new_password) # обращаеться к атрибуту pswd обращения к методу set_password в классе Password все анал логину

def main():
    a = UserForm()

    while True:   #це бескінечний цикл якщо завжди буде true тобто якщо ми зажди будемо сллідкувати умовам то завжди буде true і ми зможемо бескін взаємодіювати з прогр
        print("\n1. Переглянути поточні логін і пароль")
        print("2. Змінити логін")
        print("3. Змінити пароль")
        print("\n4. Вийти")
        choice = input("Виберіть дію: ")

        if choice == "1": #Якщо користувач обирає "1", викликається метод view_credentials() об'єкту user_form, що відображає поточний логін та пароль
            a.view_credentials()
        elif choice == "2":   #аналогічно так і працює інші вибори
            a.change_login()
        elif choice == "3":
            a.change_password()
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

main()