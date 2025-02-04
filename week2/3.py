while True:
    try:
        
        numbers = list(map(int, input().split()))
       
        count = {}
        for num in numbers:
            count[num] = count.get(num, 0) + 1
       
        mode = max(count, key=count.get)
        print(mode, end='')
    except EOFError:
        break
    except:
        break