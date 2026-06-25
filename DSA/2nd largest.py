arr = [12, 35, 1, 10, 34, 1]

largest = float('-inf')
secondLargest = float('-inf')

for num in arr:
    if num > largest:
        secondLargest = largest
        largest = num
    elif num > secondLargest and num != largest:
        secondLargest = num

print("Second Largest:", secondLargest)