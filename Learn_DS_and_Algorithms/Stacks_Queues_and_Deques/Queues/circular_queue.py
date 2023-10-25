# Circular queue in Python

class CircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, item):
        if (self.tail + 1) % self.size == self.head:
            print('The queue is full')

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.head] = item

        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = item

    def dequeue(self):
        if self.head == -1:
            print('The queue is empty')

        elif self.tail == self.head:
            value = self.queue[self.head]
            self.tail = self.head = -1

            return value

        else:
            value = self.queue[self.head]
            self.head = (self.head + 1) % self.size

            return value

    def print_queue(self):
        if self.head == -1:
            print('The queue is empty')

        elif self.tail == self.head:
            print(self.queue[self.head])

        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i])


c_queue = CircularQueue(5)
c_queue.enqueue(1)
c_queue.enqueue(2)
c_queue.enqueue(3)
c_queue.enqueue(4)
c_queue.enqueue(5)
c_queue.print_queue()


