from myqueue import Queue, UpgradedQueue

# Test Queue
# test1 = Queue()
# test1.insert(5)  # [5]
# test1.insert(6)  # [5, 6]
# print(test1.show_queue())  # [5, 6]
# test1.pop()  # 5 popped => [6]
# print(test1.show_queue())  # [6]
# test1.pop()  # []
# test1.pop()  # nothing to pop
# test1.insert(5)  # [5]
# test1.pop()  # [5]
# print(test1.show_front())  # None
# print(test1.show_rear())  # None


# Test UpgradedQueue

# test2 = UpgradedQueue("test2", 5)
# print(test2)
# test2.show_queue()
# test2.insert(1)
# test2.show_queue()
# test2.insert(2)
# test2.show_queue()
# test2.pop()
# test2.insert(3)
# test2.show_queue()
# test2.insert(4)
# test2.show_queue()
# test2.insert(5)

# test2.insert(5)
# test2.insert(6) # output exception
# test2.show_queue()
# test2.pop()
# test2.show_queue()


# print("###########testing test3##############")
# test3 = UpgradedQueue("test3", 6)
# test3.pop()
# test3.insert(1)
# test3.insert(2)
# test3.insert(3)
# test3.insert(4)
# test3.insert(5)
# test3.insert(6)
# test3.show_queue()
# # test3.insert(6) # exciption
# test3.pop()
# test3.show_queue()
# test3.pop()
# test3.show_queue()
# test3.pop()
# test3.show_queue()
# test3.pop()
# test3.show_queue()
# test3.pop()
# test3.show_queue()
# test3.pop()
# test3.show_queue()
# test3.pop() # nothing popped

# print(UpgradedQueue.get_queue("test2"))
# print(UpgradedQueue.get_queue("test3"))

# # Saving
# UpgradedQueue.save_queues()

# # Loading
# print(UpgradedQueue.load_queues()["test2"])
# print(UpgradedQueue.load_queues()["test3"])
