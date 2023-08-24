from myqueue import Queue, UpgradedQueue

# Test Queue
# test1 = Queue()
# test1.enqueue(5)  # [5]
# test1.enqueue(6)  # [5, 6]
# print(test1.show_queue())  # [5, 6]
# test1.dequeue()  # 5 popped => [6]
# print(test1.show_queue())  # [6]
# test1.dequeue()  # []
# test1.dequeue()  # nothing to dequeue
# test1.enqueue(5)  # [5]
# test1.dequeue()  # [5]
# print(test1.show_front())  # None
# print(test1.show_rear())  # None


# Test UpgradedQueue

# test2 = UpgradedQueue("test2", 5)
# print(test2)
# test2.show_queue()
# test2.enqueue(1)
# test2.show_queue()
# test2.enqueue(2)
# test2.show_queue()
# test2.dequeue()
# test2.enqueue(3)
# test2.show_queue()
# test2.enqueue(4)
# test2.show_queue()
# test2.enqueue(5)

# test2.enqueue(5)
# test2.enqueue(6) # output exception
# test2.show_queue()
# test2.dequeue()
# test2.show_queue()


# print("###########testing test3##############")
# test3 = UpgradedQueue("test3", 6)
# test3.dequeue()
# test3.enqueue(1)
# test3.enqueue(2)
# test3.enqueue(3)
# test3.enqueue(4)
# test3.enqueue(5)
# test3.enqueue(6)
# test3.show_queue()
# # test3.enqueue(6) # exciption
# test3.dequeue()
# test3.show_queue()
# test3.dequeue()
# test3.show_queue()
# test3.dequeue()
# test3.show_queue()
# test3.dequeue()
# test3.show_queue()
# test3.dequeue()
# test3.show_queue()
# test3.dequeue()
# test3.show_queue()
# test3.dequeue() # nothing popped

# print(UpgradedQueue.get_queue("test2"))
# print(UpgradedQueue.get_queue("test3"))

# # Saving
# UpgradedQueue.save_queues()

# # Loading
# print(UpgradedQueue.load_queues()["test2"])
# print(UpgradedQueue.load_queues()["test3"])
