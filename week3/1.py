def second_smallest(numbers):
    unique_numbers = sorted(set(numbers))  # Remove duplicates and sort
    if len(unique_numbers) < 2:
        return "No second smallest number"
    return unique_numbers[1]  # Return the second smallest number
# Input handling
numbers = list(map(int, input().split()))
result = second_smallest(numbers)
print(result,end="")