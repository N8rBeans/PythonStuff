import heapq

min_heap = []

heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 20)

print(min_heap)

smallest = heapq.heappop(min_heap)
print(smallest)

print(min_heap)

arr = [15, 34, 7, 2, 5, 8]
heapq.heapify(arr)
print(arr)