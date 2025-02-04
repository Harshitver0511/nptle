while True:
    try:
       
        numbers = list(map(int, input().split()))
      
        mean = round(sum(numbers) / len(numbers))
        print(mean, end='')
    except EOFError:
        break
    except:
        break