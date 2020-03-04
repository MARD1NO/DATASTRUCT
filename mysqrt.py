"""
平方根运算
"""
def sqrt_binary(num):
    if num > 1:
        low = 1
        high = num
    else:
        low = num
        high = 1
    mid = float(low) + float((high - low) / 2)
    while abs(mid ** 2 - num) > 0.000001:
        if mid ** 2 < num:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2

    return round(mid, 6)

print(sqrt_binary(0.25))