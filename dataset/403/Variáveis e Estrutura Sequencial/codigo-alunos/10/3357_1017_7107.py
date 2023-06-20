from math import *

lt1 = radians(float(input()))
lg1 = radians(float(input()))

lt2 = radians(float(input()))
lg2 = radians(float(input()))

d = 6371.01 * (   acos( (sin(lt1) * sin(lt2) ) + ( cos(lt1) * cos(lt2) ) * cos(lg1 - lg2)  )  )

print(round(d, 2))
																					 
																					 
