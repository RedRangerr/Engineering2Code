import math

#returns the angle between two lines with law of cosines
#x1->(x,y) point
#x2->(x,y) point
#x3=>(x,y) point
def angle_finder(x1, x2, x3, x4):
    pass

#p1->(x,y) point
#p2->(x,y) point
def distance(p1, p2):
    x = (p2[0] - p1[0]) 
    y = (p2[1] - p1[1]) 
    return math.sqrt(x*x + y*y)


#p1->(x,y) point
#p2->(x,y) point
#p1 and p2 are a vector
#p3->(x,y) point
#p4->(x,y) point
#p3 and p4 are also a vector
def dot_product(p1, p2, p3, p4):
    xdiff1 = p2[0] - p1[0]
    ydiff1 = p2[1] - p1[1]
    xdiff2 = p4[0] - p3[0]
    yDiff2 = p4[1] - p3[1]
    return xdiff1 * xdiff2 + ydiff1 * yDiff2

def angle(p1,p2,p3,p4):
    dot_prod = dot_product(p1, p2, p3, p4)
    d1 = distance(p1, p2)
    d2 = distance(p3,p4)
    if d1 * d2 == 0:
        return 0
    cosTheta = dot_prod/(d1*d2)
    return  math.degrees(math.acos(cosTheta))    

    
    