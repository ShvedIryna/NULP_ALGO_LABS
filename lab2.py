piles = [3, 6, 7, 11]
h = 8


def min_speed_of_eating_bananas(piles, h):
    left, right = 1, max(piles)

    while left < right:
        middle = (left + right) // 2
        hours = sum((pile + middle - 1) // middle for pile in piles)

        if hours > h:
            left = middle + 1
        else:
            right = middle

    return left


res = min_speed_of_eating_bananas(piles, h)
print(res)
