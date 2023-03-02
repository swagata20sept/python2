# recursive vs iterative approach
def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
    pass
number=int(input("enter the number: "))
print(factorial_iterative(number))
def factorial_recursive(n):
    if n==1:
      return 1
    else:
        return n*factorial_recursive(n-1)
    