from collections import namedtuple
from Crypto.Util.number import inverse

#The CH curve is  E: Y^2 = X^3 + 497X + 1768
#Define our curve params here
a = 497
b = 1768
p = 9739

#The structure that we used to refer to the points in the script
#because P.x + Q.x always sounds better than P[0] + Q[0] ;)
Point = namedtuple("Point", "x y")

#Pretty printing for point
def printPoint(P):
    print(f"x = {P.x}")
    print(f"y = {P.y}")

#Checks if point is on the curve 
def checkPoint(P):
   LHS  = ((P.y) ** 2) % p 
   RHS = ((P.x) ** 3 + a * (P.x) + b) % p

   return LHS == RHS

#Check if a point X == Point Y
def pointEquals(P, Q):
     return True if P.x == Q.x and P.y == Q.y else False

# Adds two points on the Elliptic curve to produce a third point on the same
# curve. Calculates P + Q == P', where P' is the third point that we want.
# Algorithm taken from "An Introduction to Mathematical Cryptography" by Silverman et.al
def add(P, Q):
    # P = O ==> P + Q = Q
    if sum(P) == 0:
        return Q

    # Q = O ==> P + Q == P
    elif sum(Q) == 0:
        return P

    x1, y1 = P[0], P[1]
    x2, y2 = Q[0], Q[1]

    # The point is a reflection of P and hence,
    # P + (-P) = 0 
    if x1 == x2 and y1 == -y2:
        return (0,0)

    #Otherwise...
    if pointEquals(P, Q):
        lamb = (3 * (x1**2) + a) * inverse(2*y1,p)
    else:
        lamb = (y2 - y1) * inverse(x2-x1, p)

    x3 = (pow(lamb, 2) - x1 - x2) % p
    y3 = (lamb*(x1-x3) - y1) % p

    # P'=(x3, y3)
    return Point(x3,y3)

def main():

    # Insert the test cases here. The script works if we pass the assertions. 
    # Will let this stay here :)
    X = Point(5274,2841)
    Y = Point(8669, 740)
    assert(add(X,Y) == (1024,4440))
    assert(add(X,X) == (7284, 2107))

main()
