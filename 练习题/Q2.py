#给定一个整数数组，你的解决方案应该找到其中最小的整数。
def mimimum(arr):
    if not arr:
        return None  # 如果数组为空，返回None
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value