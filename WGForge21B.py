from math import (sqrt,acos)
r, h = map(float, input().split()) 

x1, y1, z1 = map(float, input().split()) 
x2, y2, z2 = map(float, input().split()) 

PI = acos(-1)

if z1  == 0.0 and z2 == 0:
   length = sqrt((x1-x2)**2+(y1-y2)**2 ) 


#for num_A, index_A in enumerate(point_A):
    #index_A[2] == 0                          
    #for num_B, index_B in enumerate(point_B):
        #index_B[2] == 0
        #length = sqrt((index_A[0]-index_B[0])**2+(index_A[1]-index_B[1])**2 )  


#print(x1, y1, z1)
#print(x2, y2, z2)
print(length)

