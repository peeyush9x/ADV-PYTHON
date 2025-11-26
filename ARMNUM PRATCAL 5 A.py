def armnum(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num,"is armstrong number")
    else:
        print(num,"is not armstrong number")
def palnum(num):
    sum=0
    temp=num
    while num!=0:
        rem=num%10
        sum=rem+sum*10
        num=num//10
    if temp==num:
        print(temp,"is not a palindrome number")
    else:
        print(temp,"is a palindrome number")
num=int(input("enter a number"))
armnum(num)
palnum(num)
