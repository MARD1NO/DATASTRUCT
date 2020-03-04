"""
基数排序
"""
import time
def radix_sort(s):
    i = 0 # 记录当前正在排哪一位
    max_num = max(s) # 最大值
    j = len(str(max_num)) # 记录最大位数
    while i < j:
        bucket_list = [[] for _ in range(10)]
        for x in s:
            bucket_list[int(x/10**i)%10].append(x)

        # print(bucket_list)
        s.clear() # 清空数组
        for x in bucket_list:
            for y in x:
                s.append(y) # 将桶排序过的数组再放回去

        i += 1

    return s

def radix_sort_Mardino(s):
    i = 0
    max_num = max(s)
    j = len(str(max_num))
    while i < j:
        bucket_list = [[] for _ in range(10)]
        for x in s:
            bucket_list[int(x/10**i)%10].append(x)

        s.clear()
        for x in bucket_list:
            for y in x:
                s.append(y)

        i += 1

    return s


if __name__ == '__main__':
    a = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
    b = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
    start = time.time()
    a = radix_sort_Mardino(a)
    print(a)