def remove_even_duplicates(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or num % 2 != 0:
            seen.add(num)
            result.append(num)
    return result

# Input handling
numbers = list(map(int, input().split()))
filtered_numbers = remove_even_duplicates(numbers)
print(" ".join(map(str, filtered_numbers)),end="")
