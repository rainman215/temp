import queue
q = queue.deque()
q.append(123)
q.append(456)
q.appendleft(780)
print(q.pop())
print(q.popleft())