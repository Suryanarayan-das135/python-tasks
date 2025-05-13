# factorial of a no

n=int(input("Enter a no: "))

def fact(n):
    if(n<2):
        return 1
    else:
        return n*(fact(n-1))
    
res=fact(n)
print("Factorial of",n,"is :",res)    
