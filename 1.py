def sort_first(lst):
    tmp = lst[-1]
    lst.pop()
    for i in range(len(lst)-1,-1,-1):
        if tmp < lst[i]:
            lst.insert(tmp,i)
            return

n,time = list(map(int,input().split()))
lsblk = 0
lst = list(map(int,input().split()))
lst.sort()
# print(lst)
# for i in range(len(lst)):
#     lst[i] = [lst[i],i]
# print(lst)
# lst.sort(key=lambda x:x[0])
# lst.sort()
# print(lst)
for i in range(time):
    # print(lst)
    lsblk += lst[-1]
    lst[-1] = int(lst[-1]/2)
    sort_first(lst)
print(lsblk)
