# def sort_first(lst):
#     tmp = lst[-1]
#     lst.pop()
#     for i in range(len(lst)-1,-1,-1):
#         if tmp < lst[i]:
#             lst.insert(tmp,i)
#             return
# n,time = list(map(int,input().split()))
# lsblk = 0
# lst = list(map(int,input().split()))
# lst.sort()
# for i in range(time):
#     # print(lst)
#     lsblk += lst[-1]
#     lst[-1] = int(lst[-1]/2)
#     sort_first(lst)
# print(lsblk)
#-----------------------------------------------------------

class node:
    def __init__(this, parrent, data):
        this.data = data
        this.parrent = parrent
    def insert(this, value_to_insert):
        try:
            if value_to_insert > this.data:
                this.rightChild.insert(value_to_insert)
            else:
                this.leftChild.insert(value_to_insert)
        except:
            if value_to_insert > this.data:
                this.rightChild = node(this, value_to_insert)
            else:
                this.leftChild  = node(this, value_to_insert)
