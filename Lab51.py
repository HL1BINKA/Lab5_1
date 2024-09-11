n = int(input("n = "))
sum=0
print(f"Enter {n} array elements:")
arr = [int(input()) for _ in range(n)]
print("Original array: ", arr)
for num in arr:
    if num % 3 == 0:
        sum += num
print(f"Sum: {sum}")