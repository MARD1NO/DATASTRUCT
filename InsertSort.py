"""
插入排序
"""
def insertSort(numlist):
    n = len(numlist)
    for i in range(1, n):
        print("%d轮"%i, numlist)
        value = numlist[i]

        for j in range(i-1, -1, -1):
            if numlist[j] > value:
                numlist[j+1] = numlist[j] # 搬移数据
            else:
                break

        # 经过那个循环后已经-1了，所以这里我们要加1加回去
        numlist[j+1] = value

    return numlist

print(insertSort([1, 10, 2, 9, 4]))