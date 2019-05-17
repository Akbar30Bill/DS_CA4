input()
def minSwaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda it:it[1])
    vis = {k:False for k in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans
def inorder(arr, i):
    if i < len(arr):
        return inorder(arr, 2*i) + [arr[i]] + inorder(arr, 2*i+1)
    else:
        return []
arr = list(map(int, input().split()))
arr.insert(0,None)
arr = inorder(arr, 1)
print(minSwaps(arr))
