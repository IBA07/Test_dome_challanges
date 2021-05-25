'''
Implement the function find_roots to find the roots of the quadriatic equation:
aX^2+bx+c.
The function should return a tuple containing roots in any order. If the equation has only one solution, the function should return that solution as both elements of the tuple. The equation will always have at least one solution.
The roots of the quadriatic equation can be ound with the following formula:
x1,2=(-b+-sqrt(b^2-4ac))/2a
For example, find_roots(2,10,8) should return (-1, -4) or (-4,-1) as the roots of the equation 2x^2+10x+8=0 are -1 and -4.
'''

def find_roots(a, b, c):
    
    import math
    delta = b**2-4*a*c
    x1 = (-1*b+math.sqrt(delta))/(2*a)
    x2 = (-1*b-math.sqrt(delta))/(2*a)
    return x1,x2

print(find_roots(2, 10, 8));