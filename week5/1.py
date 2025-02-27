l = input().split()
obj = {}

for s in l:
    key = s.lower()
    obj[key] = obj.get(key, 0) + 1

for key, value in obj.items():
    print(f"{key}: {value}")
