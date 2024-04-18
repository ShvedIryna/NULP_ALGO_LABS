num = [15, 7, 22, 9, 36, 2, 42, 18]
n = len(num)
k = 3

def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[len(num) // 2]
    left = [x for x in num if x < pivot]
    middle = [x for x in num if x == pivot]
    right = [x for x in num if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def find_k_largest(num, k):
    if len(num) < k:
        return "Число k є більший за розмір заданого масиву"
    sorted_nums = quick_sort(num)
    k_largest = sorted_nums[-k]
    return k_largest

def find_k_position(num, k):
    position = num.index(k_largest)
    return position

sorted_num = quick_sort(num)
k_largest = sorted_num[-k]
position = num.index(k_largest)

print(f"{k_largest}")
print(f"{position}")
