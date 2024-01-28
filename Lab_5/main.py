from collection import QueueCollection
from task_4.queue import Queue


# Пример использования
def main():
    queue1 = Queue()
    queue1.enqueue("Item 1")
    queue1.enqueue("Item 2")

    queue2 = Queue()
    queue2.enqueue("Item 3")

    collection = QueueCollection()
    collection.add_queue(queue1)
    collection.add_queue(queue2)
    print(collection)

    collection.save("queues.json")

    new_collection = QueueCollection()
    new_collection.load("queues.json")
    print(new_collection)


if __name__ == "__main__":
    main()
