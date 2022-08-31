import math

def quad_calc(a,b,c):
   disc = b*b - 4*a*c
   if (disc < 0):
       print("No real solution")
       return None
    
   sqr_root_disc =  math.sqrt(disc)
   solution_1 = (-1*b+sqr_root_disc)/(2*a)
   solution_2 = (-1*b-sqr_root_disc)/(2*a)
   return (solution_1, solution_2)



print(quad_calc(1,4,2))



















