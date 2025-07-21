def factorial(n):
    if n<2 :
        return 1
    else :
        return n*factorial(n-1)

a=int(input('Enter a nmber: '))
c=factorial(a)
print('The factorial of', a, 'is', c)
