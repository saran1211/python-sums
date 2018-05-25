n = int(input('enter the num'))
n1 = 0
n2 = 1
c = 0
print('fibonacci series upto',n)
while c < n:
  print(n1)
  nth=n1+n2
  n1=n2
  n2=nth
  c += 1
