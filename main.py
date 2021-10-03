#10/3 Alpay Fibonacci Series

# 1,1,2,3,5,8,13,21,34,55..............

first = 1
second = 1

fibonacci = [first, second]

for i in range(25):

    first, second = second, first + second
    fibonacci.append(second)

print(fibonacci)



