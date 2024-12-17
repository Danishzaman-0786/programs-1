arr=[2,3,3]
a=0
d={}
duplicate=0
for i in arr:
  a=a+i
  if i in d:
    d[i]=d[i]+1
  else:
    d[i]=1
for i in d:
  if d[i]>1:
    duplicate=i

n=len(arr)
m=((n+1)*(n))//2 
print(duplicate,m-a+duplicate)
