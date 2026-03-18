def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True
print(is_sorted([1, 2, 3, 4,5,6,7,8,9]))
print(is_sorted([1, 3, 2, 4,5,8,7,9,6]))