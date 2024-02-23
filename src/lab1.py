num = [15, 7, 22, 9, 36, 2, 42, 18]
n = len(num)
k = 3

def compare_and_swap(num):
    for i in range(n-1):
        for pos in range(0, n-1):
            prev_pos = pos + 1
            if (num[pos] > num[prev_pos]):
                num[pos], num[prev_pos] = num[prev_pos], num[pos]
    return num


def find_k_largest(num, k):
    if len(num) < k:
        return "Число k є більший за розмір заданого масиву"
    sorted_nums = compare_and_swap(num)
    k_largest = sorted_num[-k]
    return k_largest

def find_k_position(num, k):
    position = num.index(k_largest)
    return position

sorted_num = compare_and_swap(num)
k_largest = num[-k]
position = num[::-1].index(k_largest)

print(f"{k_largest}")
print(f"{position}")
