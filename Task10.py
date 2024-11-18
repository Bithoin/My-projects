import tkinter as tk
from tkinter import ttk
import random
import time

class TimeSenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Перевірка відчуття часу")

        #Установка размеров окна и параметров центрирования
        self.width = 400
        self.height = 250
        self.setup_window(self.width, self.height)

        #Установка черного фона для всего окна
        self.root.configure(bg='#0c4001')

        #Настройка стилей для виджетов
        self.style = ttk.Style()
        self.style.theme_use('clam')  #Использование темы clam

        #Настройка стилей для кнопок и меток
        self.style.configure('TButton', background='#4CAF50', foreground='white', font=('Arial', 12), padding=10)
        self.style.configure('TLabel', font=('Arial', 12), foreground='white', background='#0c4001')

        #Метка для отображения сгенерированного времени
        self.interval_label = ttk.Label(root, text="")
        self.interval_label.pack(pady=10)

        #Кнопка для генерации времени
        self.generate_interval_button = ttk.Button(root, text="Згенерувати час", command=self.generate_interval, style='TButton')
        self.generate_interval_button.pack(pady=5)

        #Кнопка для начала отсчета времени
        self.start_button = ttk.Button(root, text="Старт", command=self.start_timer, style='TButton')
        self.start_button.pack(pady=5)

        #Кнопка для остановки отсчета времени
        self.stop_button = ttk.Button(root, text="Стоп", command=self.stop_timer, state=tk.DISABLED, style='TButton')
        self.stop_button.pack(pady=5)

        #Метка для отображения результата
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.generated_interval = None
        self.start_time = None

    def setup_window(self, width, height, x_offset=0, y_offset=0):
        #Получение размеров экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #Вычисление координат для центрирования окна
        x = (screen_width - width) // 2 + x_offset
        y = (screen_height - height) // 2 + y_offset

        #Установка геометрии окна
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def generate_interval(self):
        #Генерация случайного времени от 10 до 30 секунд
        self.generated_interval = random.randint(10, 30)
        #Обновление метки для отображения сгенерированного интервала
        self.interval_label.config(text=f"Згенерований час: {self.generated_interval} сек")

    def start_timer(self):
        #берем время
        self.start_time = time.time()
        # Отключение кнопки старта и включение кнопки остановки
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.start_time is not None:
            # Вычисление прошедшего времени
            elapsed_time = time.time() - self.start_time
            # Определение результата на основе прошедшего времени
            if elapsed_time > self.generated_interval:
                result_text = f"Час вже пройшов: {elapsed_time - self.generated_interval:.2f} сек"
                #result_text = f"Час вже пройшов)"
            elif elapsed_time < self.generated_interval:
                result_text = f"Залишилось часу: {self.generated_interval - elapsed_time:.2f} сек"
            else:
                result_text = "Ви відмінно відчуваєте час"
            #Обновление метки для отображения результата
            self.result_label.config(text=result_text)
            #Включение кнопки старта и отключение кнопки остановки
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            # Сброс времени старта
            self.start_time = None

root = tk.Tk()
app = TimeSenseApp(root)
root.mainloop()
