import json

from task_4.queue import Queue


class QueueCollection:
    def __init__(self):
        self.queues = []

    def add_queue(self, queue):
        if isinstance(queue, Queue):
            self.queues.append(queue)
        else:
            raise TypeError("Only Queue objects can be added")

    def remove_queue(self, index):
        if 0 <= index < len(self.queues):
            return self.queues.pop(index)
        raise IndexError("Index out of range")

    def get_queue(self, index):
        if 0 <= index < len(self.queues):
            return self.queues[index]
        raise IndexError("Index out of range")

    def __str__(self):
        return '\n'.join(f"Queue {idx}: {queue}" for idx, queue in enumerate(self.queues))

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump([queue.items for queue in self.queues], file)

    def load(self, filename):
        with open(filename, 'r') as file:
            queues_data = json.load(file)
            self.queues = [Queue() for _ in queues_data]
            for queue, items in zip(self.queues, queues_data):
                for item in items:
                    queue.enqueue(item)
