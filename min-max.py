def find_min_max(lst):
    if not lst:
        return None, None

    min_val = lst[0]
    max_val = lst[0]

    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val


numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]

min_val, max_val = find_min_max(numbers)
print("Minimum value:", min_val)
print("Maximum value:", max_val)