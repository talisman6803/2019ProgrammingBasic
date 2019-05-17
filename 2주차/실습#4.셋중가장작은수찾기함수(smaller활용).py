def smaller(x,y):
    if x>y : return y
    else : return x
def smallest(x,y,z):
    return smaller(smaller(x,y),smaller(y,z))
print(smallest(3,5,9))
print(smallest(5,3,9))
print(smallest(5,9,3))
print(smallest(3,9,5))
print(smallest(9,3,5))
print(smallest(9,5,3))
print(smallest(3,3,5))
print(smallest(5,3,3))
print(smallest(3,5,3))
print(smallest(3,3,3))
