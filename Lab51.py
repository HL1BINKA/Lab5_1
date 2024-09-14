n = int(input("n = "))
sum=0
sum_of_minus=0
print(f"Enter {n} array elements:")
arr = [int(input()) for _ in range(n)]
print("Original array: ", arr)
for num in arr:
    if num<0:
        sum_of_minus+=num
    else:
        sum += num
print(f"Sum: {sum}")
print(f"Sum of minus: {sum_of_minus}")