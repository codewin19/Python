#variable arguments
def userSum(*arg):
    print(arg)
    s = 0
    for x in arg:
        s +=x
    return s

print(userSum(1))
print(userSum(2,4))
print(userSum(3,5,6,7,8,9))