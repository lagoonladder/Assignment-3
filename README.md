# Assignment-3
This is an assignment.

## Task 1
This is basically a factorial calculator. It asks the users to enter a number and gives the output as factorial of that number.

 def factorial(n):
    if n<2 :
        return 1
    else :
        return n*factorial(n-1)

a=int(input('Enter a nmber: '))
c=factorial(a)
print('The factorial of', a, 'is', c)



### Task 2
Thisallows users to calculate square root, logarithm and the sine of the given number. It asks users to enter a number and gives the value of its square root, logarithm  and sine as the output.

a=int(input('Enter a number: '))
import math
print('Square root: ', math.sqrt(a))
print('Logarith: ', math.log(a,2.71828 ))
print('Sine: ', math.sin(a))
