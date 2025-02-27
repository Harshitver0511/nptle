def grantha_sudharaka(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Swap if current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(" ".join(map(str, arr)))  # Print order after each pass
        if not swapped:
            break  # Stop if no swaps occurred in this pass

# Taking input as space-separated integers
arr = list(map(int, input().split()))
grantha_sudharaka(arr)
