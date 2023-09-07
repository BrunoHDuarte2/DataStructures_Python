def recursion(x):
    x+=1
    print("Loop número:", x)
    if x==5:
        return    
    recursion(x)

def soma(x):
    if x==0:
        return 0
    return x+soma(x-1)

##Exericios de recursão
#fatorial
def fatorial(x):
    if x==0:
        return 1
    else: 
        return x*fatorial(x-1)
        # 
# Expoente
def exp(a, b):
    if a==0:
        return 0
    if b==0:
        return 1
    return a*exp(a, b-1)
print(exp(2,0))
