# import time
# def Task(func):
#     def wrapper():
#         start = time.perf_counter()
#         list_numbers = func()
#         end = time.perf_counter()
#         # list_numbers = func()
#         execution_time = end - start
#         return f'Час виконнаня програми = {execution_time:.8f} мілісекунд\n{list_numbers}'
#     return wrapper
# @Task
# def numbers():
#     list_numbers = []
#     is_prime = [True] * (target1 + 1)
#     is_prime[0] = is_prime[1] = False
#
#     for num in range(target, target1 + 1):
#         if is_prime[num]:
#             list_numbers.append(num)
#             for multiple in range(num * num, target1 + 1, num):
#                 is_prime[multiple] = False
#     return list_numbers
# while True:
#     target = int(input('Введіть першу межу діапазону: '))
#     target1 = int(input('Введіть другу межу діапазону: '))
#     if target >= target1:
#         raise ValueError("Введіть допустимі межі діапазону")
#     else:
#         break
# print(numbers())

class BaseReport:
    def create(self):
        raise NotImplementedError("Цей метод повинен бути переозначений.")

class FinancialReport1(BaseReport):
    def create(self):
        return "Фінансовий звіт 1."

class FinancialReport2(BaseReport):
    def create(self):
        return "Фінансовий звіт 2."

class FinancialReport3(BaseReport):
    def create(self):
        return "Фінансовий звіт 3."

def report_decorator(report_class):
    class Wrapper(report_class):
        def create(self):
            report = super().create()
            return f"Оброблений: {report}"

    return Wrapper

@report_decorator
class ProcessedReport1(FinancialReport1):
    pass

@report_decorator
class ProcessedReport2(FinancialReport2):
    pass

@report_decorator
class ProcessedReport3(FinancialReport3):
    pass

def main():
    reports = [
        ProcessedReport1(),
        ProcessedReport2(),
        ProcessedReport3()
    ]
    for report in reports:
        print(report.create())

main()
