from queue import Queue


def main():
    queue = Queue()
    queue.enqueue('apple')
    queue.enqueue('banana')
    print(queue)
    queue.dequeue()
    print(queue)
    queue.save('queue.json')
    new_queue = Queue()
    new_queue.load('queue.json')
    print(new_queue)


if __name__ == "__main__":
    main()
