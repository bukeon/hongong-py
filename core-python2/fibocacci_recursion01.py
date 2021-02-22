def fibonacci(n: int):
#탈출조건
    if (n==1):
        return 1
    if (n==2):
        return 1 

    return fibonacci(n-1) + fibonacci(n-2)



#함수 호출
print(fibonacci(35))