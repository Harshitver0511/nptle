def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

while True:
    try:
        n = int(input())
        print(sum_of_squares(n), end='')
    except EOFError:
        break
    except ValueError:
        break