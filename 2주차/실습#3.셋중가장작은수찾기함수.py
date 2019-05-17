def smaller(x,y,z):
    if x>y:
        t=x
        x=y
        y=t
    if y>x:
        t=y
        y=z
        z=t
    if x>y:
        t=x
        x=y
        y=t
    return x
print(smaller(3,5,9))
print(smaller(5,3,9))
print(smaller(5,9,3))
print(smaller(3,9,5))
print(smaller(9,3,5))
print(smaller(9,5,3))
print(smaller(3,3,5))
print(smaller(5,3,3))
print(smaller(3,5,3))
print(smaller(3,3,3))
