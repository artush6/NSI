def max_diviser(lst):
    if len(lst) == 1:
        return lst[0]  # base case

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    max_left = max_diviser(left)
    max_right = max_diviser(right)

    return max(max_left, max_right)
