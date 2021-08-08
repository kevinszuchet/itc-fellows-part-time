def print_divisible_by_or_contains_7(n):
    for num in range(0, n + 1):
        ten = (num // 10)
        # Examples:
        #   - 73 is true because the ten is 7
        #   - 97 also is true because the unit is 7
        if not (num % 7) or num > 9 and (ten == 7 or (num - ten * 10) == 7):
            print(num)


print_divisible_by_or_contains_7(100)
