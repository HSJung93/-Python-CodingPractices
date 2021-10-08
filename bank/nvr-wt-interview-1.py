

def stackQ(data):
  s1=[]
  s2=[]
  ret = []
  
  for i in data:
    s1.append(i)
    s2.append(s1.pop(0))
    
  # for j in s1:
  #   s2.append(j)
  for k in s2:
    ret.append(k)

  return ret

print(stackQ([1,2,3,4,5]))
