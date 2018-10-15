import math

def quadratic(a,b,c):
 if not isinstance(a&b&c,(int,float)):
  raise TypeError('bad operand type')
 if (b*b-4*a*c)>0:
  x=(math.sqrt(b*b-4*a*c)-b)/(2*a)
  y=-(math.sqrt(b*b-4*a*c)+b)/(2*a)
  return x,y
 elif (b*b-4*a*c)==0:
  x=(math.sqrt(b*b-4*a*c)-b)/(2*a)
  return x
 else:
  print(u'Error!')