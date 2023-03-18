def revese(x):
    if x<0:
        x=-1*x
        return -1*int(str(x)[::-1]) if -1*int(str(x)[::-1]) in range(-2**31,2**31) else 0
    elif x>0 and x%10!=0:
        return int(str(x)[::-1]) if int(str(x)[::-1]) in range(-2**31,2**31) else 0
    else:
        while x%10!=0:
            x=x//10
        return int(str(x)[::-1]) if int(str(x)[::-1]) in range(-2**31,2**31) else 0

print(revese(-1563847412))

