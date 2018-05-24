n=int(input('enter the no of elements'))
l=[]
for i in range(1,n+1):
  a=int(input('enter the elements'))
  l.append(a)
print (l)
for i in l:
    print (l.index(i))  
