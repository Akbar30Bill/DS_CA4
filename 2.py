class room:
    def __init__(this, on):
        this.on = on
        # this.parrent = None
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
for i in range(tedad):
    lst.append(room(on_lst[i]))
for i in range(0, tedad-1):
    lst[parrent_lst[i]].childs.append(lst[i+1])
for i in lst:
    print (i.on)
    for j in i.childs:
        print(j.on)
while True:
    cmd = input().split()
    if cmd[0] == "report":print(lst[int(cmd[1])].report())
    else:lst[int(cmd[1])].toggle()
