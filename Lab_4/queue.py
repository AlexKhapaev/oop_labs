import json  # Импортируем модуль json для работы с JSON-файлами


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Очередь пустая")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    @classmethod
    def from_string(cls, str_value):
        queue = cls()
        for item in str_value.split(','):
            queue.enqueue(item.strip())
        return queue

    # Метод для сохранения данных очереди в JSON-файл
    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.items, file)

    # Метод для загрузки данных очереди из JSON-файла
    def load(self, filename):
        with open(filename, 'r') as file:
            self.items = json.load(file)
