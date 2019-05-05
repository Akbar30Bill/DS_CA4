import heapq
def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)
lsblk = 0
n,time = list(map(int,input().split()))
lst = list(map(int,input().split()))
heapq._heapify_max(lst)
for i in range(time):
    tmp = heapq._heappop_max(lst)
    _heappush_max(lst, int(tmp/2))
    lsblk += tmp
print(lsblk)
