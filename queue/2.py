import queue
q = queue.PriorityQueue()
q.put((3,'aaaaa'))
q.put((3,'bbbbb'))
q.put((1,'ccccc'))
q.put((3,'ddddd'))
print(q.get())
print(q.get())