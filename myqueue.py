import json
from exceptions import QueueOutOfRangeException


class Queue:
    def __init__(self):
        self._queue = []
        self._front = -1
        self._rear = 0

    # getter and setters
    @property
    def queue(self):
        return self._queue

    @queue.setter
    def queue(self, new_queue):
        self._queue = new_queue

    @property
    def front(self):
        return self._front

    @front.setter
    def front(self, new_front):
        self._front = new_front

    @property
    def rear(self):
        return self._rear

    @rear.setter
    def rear(self, new_rear):
        self._rear = new_rear

    # Instance methods
    def is_empty(self):
        if not len(self.queue):
            return True
        return False

    def enqueue(self, new_value):  # inque
        self.queue.append(new_value)

    def dequeue(self):
        if self.is_empty() == False:
            print(f"{self.queue[0]} popped")
            self.queue.dequeue(0)
        else:
            print("Queue is Empty Nothing to dequeue")
            print("None")  # return None

    def show_queue(self):
        if self.is_empty() == False:
            print(self.queue)
        else:
            print("Queue is Empty Nothing to show")

    def show_front(self):
        if self.is_empty() == False:
            return self.queue[self.front]

    def show_rear(self):
        if self.is_empty() == False:
            return self.queue[self.rear]


class UpgradedQueue(Queue):
    all_queus = {}
    file_path = "queues.json"

    def __init__(self, name, size):
        super().__init__()
        self._name = name
        self._size = size
        self._queue = [None] * size
        self.__class__.all_queus[name] = self.queue

    # def __str__(self):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size

    def enqueue(self, new_value):
        if None in self.queue:
            none_index = self.queue.index(None)
            self.queue[none_index] = new_value
        else:
            raise QueueOutOfRangeException()

    @classmethod
    def get_queue(cls, queue_name):
        return UpgradedQueue.all_queus[queue_name]

    @classmethod
    def save_queues(cls):
        with open(UpgradedQueue.file_path, "w") as file:
            json.dump(UpgradedQueue.all_queus, file)

    @classmethod
    def load_queues(cls):
        with open(UpgradedQueue.file_path, "r") as file:
            loaded_data = json.load(file)
            return loaded_data

    # def __repr__(self):

    def dequeue(self):
        if all(item is None for item in self.queue):
            print("Queue is Empty Nothing to dequeue")
            print("None popped")
        else:
            self.queue[0] = None
            for i in range(len(self.queue)):
                if i == len(self.queue)-1:
                    # print(f"{self.queue[i]} popped")
                    self.queue[i] = None
                else:
                    # print(f"{self.queue[i]} popped")
                    self.queue[i] = self.queue[i + 1]
