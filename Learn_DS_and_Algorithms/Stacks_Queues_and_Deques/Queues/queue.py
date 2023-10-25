# Queue in Python

# Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

# Basic Operations of Queue
# Enqueue: Add an element to the end of the queue
# Dequeue: Remove an element from the front of the queue
# IsEmpty: Check if the queue is empty
# IsFull: Check id the queue is full
# Peek: Get the value of the front of the queue without removing it


class MyQueue:
    def __init__(self):
        self.queue = []   # Creating a queue

    def enqueue(self, item):
        self.queue.append(item)   # Adding item to a queue

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop(0)   # Displaying the first item and then dropping it
        else:
            return None   # If a queue is empty, return 'None'

    def is_empty(self):
        return True if len(self.queue) == 0 else False   # Checking if the queue is empty

    def peek(self):
        return self.queue[0]


queue = MyQueue()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')

print(queue.is_empty())
print(queue.peek())

queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue.is_empty())
