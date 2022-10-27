n=int(input())
b=str(n)
c=set(b)

if(len(b)==len(c)):
    print("Unique Number")
else:
    print("Not Unique Number")