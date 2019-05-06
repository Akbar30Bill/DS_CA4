class room:
    def __init__(this, on):
        this.on = on
        this.childs = []
    def report(this):
        rtvl = this.on;
        for child in this.childs:
            rtvl += child.report()
        return rtvl
    def toggle(this):
        this.on = abs(this.on-1)
        for child in this.childs:
            child.toggle()
tedad = int(input())
parrent_lst = list(map(int, input().split()))
lst = []
on_lst = list(map(int, input().split()))
for i in on_lst:
    lst.append(room(i))
for i in range(0, tedad-1):
    lst[parrent_lst[i]-1].childs.append(lst[i+1])
for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == "report":print(lst[int(cmd[1])-1].report())
    else:lst[int(cmd[1])-1].toggle()
