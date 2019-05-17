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



# class node:
#     def __init__(this, parrent, data):
#         this.data = data
#         this.parrent = parrent
#         this.rightChild = None
#         this.leftChild = None
#     def insert(this, value_to_insert):
#         try:
#             if value_to_insert > this.data:
#                 this.rightChild.insert(value_to_insert)
#             else:
#                 this.leftChild.insert(value_to_insert)
#         except:
#             if value_to_insert > this.data:
#                 # print(f'inserted rightChild {value_to_insert} the parrent is {this.data}')
#                 this.rightChild = node(this, value_to_insert)
#             else:
#                 # print(f'inserted left child {value_to_insert} the parrent is {this.data}')
#                 this.leftChild  = node(this, value_to_insert)
#     def find(this, value_to_find):
#         if value_to_find > this.data:
#             try:return this.rightChild.find(value_to_find)
#             except:pass
#         elif value_to_find < this.data:
#             try:return this.leftChild.find(value_to_find)
#             except:pass
#         else:
#             return this
#     def popMax(this):
#         if not this.rightChild == None:
#             return this.rightChild.popMax()
#         elif not this.leftChild == None:
#             # if not this.parrent.rightChild == None:
#             this.parrent.rightChild = this.leftChild
#             this.leftChild.parrent  = this.parrent
#             return this.data
#         else:
#             this.parrent.rightChild = None
#             return this.data
#
# n,time = list(map(int,input().split()))
# lst = list(map(int,input().split()))
# Dummy = node(None, None)
# root = node(Dummy, 0)
# val = 0
# for i in range(0, len(lst)):
#     root.insert(lst[i])
# for i in range(time):
#     mxvl = root.popMax()
#     # print(mxvl)
#     val += mxvl
#     root.insert(int(mxvl/2))
# print(val)
