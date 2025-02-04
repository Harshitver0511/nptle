def process_list(numbers):
    reversed_numbers = numbers[::-1]
    new_list = [numbers[i] + reversed_numbers[i] if i % 2 == 0 else numbers[i] for i in range(len(numbers))]
    return new_list

# Input handling
numbers = list(map(int, input().split()))
result = process_list(numbers)
print(" ".join(map(str, result)),end="")
