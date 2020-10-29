n = p = int(input("Enter the number of students in the class: "))
sum = 0
while n:
    n -= 1
    m = float(input("Enter the marks: "))
    sum += m
    if n == 0:
        break
avg = sum / p
print(avg)
