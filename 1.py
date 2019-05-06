# def sort_first(lst):
#     # print(lst)
#     tmp = lst.pop()
#     tmp_lst = []
#     # for i in range(len(lst)-1,-1,-1):
#         # if tmp <= lst[i]:
#         #     print(lst, end=' turned into ')
#         #     lst.insert(i-1,tmp)
#         #     print(lst)
#         #     print(i)
#         #     return
#     while lst[-1] > tmp:
#         tmp_lst.append(lst.pop())
#     lst.append(tmp)
#     while not len(tmp_lst) == 0:
#         lst.append(tmp_lst.pop())
# n,time = list(map(int,input().split()))
# lsblk = 0
# lst = list(map(int,input().split()))
# lst.sort()
# for i in range(time):
#     try:
#         lsblk += lst[-1]
#         lst[-1] = int(lst[-1]/2)
#         sort_first(lst)
#     except:pass
# print(lsblk)
#-----------------------------------------------------------

class node:
    def __init__(this, parrent, data):
        this.data = data
        this.parrent = parrent
        this.rightChild = None
        this.leftChild = None
    def insert(this, value_to_insert):
        try:
            if value_to_insert > this.data:
                this.rightChild.insert(value_to_insert)
            else:
                this.leftChild.insert(value_to_insert)
        except:
            if value_to_insert > this.data:
                # print(f'inserted rightChild {value_to_insert} the parrent is {this.data}')
                this.rightChild = node(this, value_to_insert)
            else:
                # print(f'inserted left child {value_to_insert} the parrent is {this.data}')
                this.leftChild  = node(this, value_to_insert)
    def find(this, value_to_find):
        if value_to_find > this.data:
            try:return this.rightChild.find(value_to_find)
            except:pass
        elif value_to_find < this.data:
            try:return this.leftChild.find(value_to_find)
            except:pass
        else:
            return this
    def popMax(this):
        if not this.rightChild == None:
            return this.rightChild.popMax()
        elif not this.leftChild == None:

            this.parrent.rightChild = this.leftChild
            this.leftChild.parrent  = this.parrent
            return this.data
        else:
            this.parrent.rightChild = None
            return this.data

n,time = list(map(int,input().split()))
lst = list(map(int,input().split()))
Dummy = node(None, None)
root = node(Dummy, 0)
val = 0
for i in range(0, len(lst)):
    root.insert(lst[i])
for i in range(time):
    mxvl = root.popMax()
    # print(mxvl)
    val += mxvl
    root.insert(int(mxvl/2))
print(val)


# ---------------------------------------------------------------------
# class node:
#     def __init__(this, data):#, next, prev):
#         this.data = data
#         this.next = None
#         this.prev = None
#     def insert(this, data, last):
#         if this.data > data:
#             new_node = node(data)#, this, this.prev)
#             this.prev.next = new_node
#             this.prev = new_node
#         else:
#             this.next.insert(data)
#     def popMax(this, last):
#         backup = this
#         this.prev.next = None
#         return this.data
#
#
# n,time = list(map(int,input().split()))
# lst = list(map(int,input().split()))
# lsblk = 0
# lst.sort()
# for i in range(len(lst)):
#     lst[i] = node(lst[i])
# for i in range(1, len(lst)-1):
#     lst[i].prev = lst[i-1]
#     lst[i].next = lst[i+1]
# lst[0].next = lst[1]
# lst[-1].next=lst[-1]
# for i in time:
#     kkk = last.popMax(last)
#     lsblk += kkk
#     last.insert(kkk/2)
#---------------------------------------------------------------------
