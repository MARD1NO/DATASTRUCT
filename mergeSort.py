def mergesort_Mardino(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergesort_Mardino(left)
        mergesort_Mardino(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

    return alist

# print(mergesort_Mardino([1, 9, 2, 7, 6]))

def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist) //2
        left = alist[:mid]
        right = alist[mid:]

        mergesort(left)
        mergesort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                k += 1
                i += 1
            else:
                alist[k] = right[j]
                k += 1
                j += 1

        while i < len(left):
            alist[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1

    return alist

print(mergesort([1, 9, 2, 7, 6]))