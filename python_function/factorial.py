# exmple of default arguments
def factorial(number=0):
    fac = 1
    for x in range(1,number+1):
        fac *= x
    return fac



number = int(input("Enter Number : "))
print("Factorial of ",number, " is ",factorial(number))