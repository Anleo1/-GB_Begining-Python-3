num = int(input("Enter number: "))
arr = []
for i in range(0, num):
    k = int(input())
    arr.append(k)
X = int(input("Enter number, that need to be founded: "))
max_cl = max(arr)
result = 0
for i in range(0, num):
    if (abs(arr[i] - X) < max_cl):
        max_cl = abs(arr[i] - X)
        result = arr[i]
print("Answer: ", result)