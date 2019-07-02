import heapq

# priority queue
pqueue = []
heapq.heappush(pqueue , (1 , 'A'))
heapq.heappush(pqueue , (7 , 'B'))
heapq.heappush(pqueue , (3 , 'C'))
heapq.heappush(pqueue , (6 , 'D'))
heapq.heappush(pqueue , (2 , 'E'))

 # not necessarily sorted
print(pqueue)


print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))

