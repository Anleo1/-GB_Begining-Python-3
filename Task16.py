num = int(input("Enter number: "))
arr = []
for i in range(0, num):
    k = int(input())
    arr.append(k)
found_num = int(input("Enter number, that need to be founded: "))
count = 0
for i in range(0, num):
    if (arr[i]==found_num):
        count+=1
print("Answer: ", count)