import math
def quadraticEquationPositive(a,b,c):
    if a != 0:
        pb = (b**2)-(4*a*c)
        if pb < 0:
            return None
        elif pb == 0:
            ans = (-1 * b) / 2 / a
            return ("중근", ans)
        else:
            ans1 = (-1 * b + ((b**2)-(4*a*c))**(0.5))/2/a
            ans2 = (-1 * b - ((b**2)-(4*a*c))**(0.5))/2/a
            return (ans1, ans2)
    else:
        return None

print(quadraticEquationPositive(1,-1,-2)) # (2.0, -1.0)
print(quadraticEquationPositive(3,3,3)) # None
print(quadraticEquationPositive(0,3,4)) # None
