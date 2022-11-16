import math

#returns the angle between two lines with law of cosines
#a->(x,y) point
#b->(x,y) point
#c->(x,y) point
#d->(x,y) point
def angle_finder(a, b, c):
    #calculate intersection point between line from A and line from C 
    ab_vec = (a[0]-b[0], a[1]-b[1])
    bc_vec = (c[0] - b[0], c[1]-b[1])
    dot_product = ab_vec[0] * bc_vec[0] + ab_vec[1] * bc_vec[1]
    try:
        costheta = dot_product/(distance(a,b)*distance(b,c))
        return math.degrees(math.acos(costheta))
    except:
        return 0
    
#returns the eucilidan distance between two points
def distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x*x +y*y)



    
    