def countSort(array, n):
    """
    计数排序
    :param array: 数组
    :param n: 数组大小
    :return:
    """
    print(array)
    bucket_size = max(array) + 1
    bucket = [0]*bucket_size

    for i in array:
        bucket[i] += 1

    print(bucket)

    for i in range(1, bucket_size):
        bucket[i] += bucket[i-1]

    print(bucket)

    sorted_array = [0] * len(array)

    for i in range(len(array)-1, -1, -1):
        index = bucket[array[i]] - 1
        sorted_array[index] = array[i]
        bucket[array[i]] -= 1

    return sorted_array

# a = countSort([2, 5, 3, 0, 2, 3, 0, 3], 6)
# print(a)

