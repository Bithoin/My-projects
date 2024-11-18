# class FixedSizeStack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = []
#
#     def push(self, item):
#         if len(self.stack) >= self.size:
#             print("Стек повний")
#         else:
#             self.stack.append(item)
#             print(f"Додано: {item}")
#
#     def pop(self):
#         if self.is_empty():
#             print("Cтек порожній")
#             return None
#         return self.stack.pop()
#
#     def count(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def is_full(self):
#         return len(self.stack) == self.size
#
#     def clear(self):
#         self.stack.clear()
#         print("Стек порожній")
#
#     def peek(self):
#         if self.is_empty():
#             print("Стек порожній!")
#             return None
#         return self.stack[-1]
#
# stack = FixedSizeStack(3)
# stack.push("Line1")
# stack.push("Line2")
# stack.push("Line3")
# stack.push("Line4")
# print("Верхній елемент:", stack.peek())
# print("Видалено:", stack.pop())
# print("Стек пустий?", stack.is_empty())
# stack.clear()


class DynamicStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Додано: {item}")

    def pop(self):
        if self.is_empty():
            print("Cтек порожній")
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()
        print("Стек порожній!")

    def peek(self):
        if self.is_empty():
            print("Стек порожній!")
            return None
        return self.stack[-1]

stack = DynamicStack()
stack.push("Line1")
stack.push("Line2")
print("Верхній элемент:", stack.peek())
print("Видалено:", stack.pop())
print("Кіл-ть элементів:", stack.count())
stack.clear()
