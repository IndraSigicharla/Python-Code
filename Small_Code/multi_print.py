n = 0
product = 1
while n > -1 :
    n += 1
    product *= n
    print(n, end=" ")
    if n == 10:
        break
print("The product is:", product)
