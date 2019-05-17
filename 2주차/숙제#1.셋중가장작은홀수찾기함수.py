def smallerOdd(x,y):
    if(x%2==0 and y%2==0) : None
    elif(x%2==0 and y%2!=0) : return y
    elif(x%2!=0 and y%2==0) : return x
    else :
        if x>y : return y
        else : return x
def smallestOdd(x,y,z):
    if(smallerOdd(x,y)!=None and smallerOdd(y,z)!=None) :
        return smallerOdd(smallerOdd(x,y),smallerOdd(y,z))
    elif(smallerOdd(x,y)==None and smallerOdd(y,z)!=None) :
        return smallerOdd(y,z)
    elif(smallerOdd(x,y)!=None and smallerOdd(y,z)==None) :
        return smallerOdd(x,y)
    else : return None
print(smallestOdd(3,2,2)) 
print(smallestOdd(3,5,7)) 
print(smallestOdd(3,5,1)) 
print(smallestOdd(8,3,4))
print(smallestOdd(8,3,5))
print(smallestOdd(8,5,3))
print(smallestOdd(2,8,3)) 
print(smallestOdd(2,8,4)) 
