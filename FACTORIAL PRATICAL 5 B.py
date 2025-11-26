def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
num=int(input("enter a number:"))
print("the factorial of",num,"is",fact(num))
    
 
