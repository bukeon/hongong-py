n = int(input())


def factorial(n: int)-> int:

    output = 1

    for i in range(n,0,-1):
        output = output*i
    return output
    
print("n! = ",factorial(n))
