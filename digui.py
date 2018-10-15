def trim(s): 
 if s[0]==" ":
  return trim(s[1:])
 if s[-1]==" ":
  return trim(s[:-1])
 return s