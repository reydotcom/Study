# Priority Queue in Python

class PriorityQueue:
    def __init__(self):
        self.arr = []

    def heapify(self, size, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < size and self.arr[i] < self.arr[l]:
            largest = l

        if r < size and self.arr[i] < self.arr[r]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(size, largest)

    def add(self, item):
        if self.arr == 0:
            self.arr.append(item)
        else:
            self.arr.append(item)
            size = len(self.arr)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)

    def remove(self, item):
        size = len(self.arr)
        i = 0

        for i in range(0, size):
            if item == self.arr[i]:
                break

        self.arr[i], self.arr[size - 1] = self.arr[size - 1], self.arr[i]

        self.arr.pop(size - 1)

        for i in range((size // 2) - 1, -1, -1):
            self.heapify(len(self.arr), i)

    def display_q(self):
        print(self.arr)


q = PriorityQueue()
q.add(1)
q.add(2)
q.add(7)
q.add(5)
q.display_q()
q.remove(2)
q.display_q()
