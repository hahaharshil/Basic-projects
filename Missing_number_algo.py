a = input()
a=a.rstrip()
b=list(set(a))
l=[]
p=[]
c=0
for i in range(len(b)):
    if a.count(b[i])>1:
        c+=1
j=0
while j<=len(a):
    l.append(a[j:j+c+1])
    j=j+c+1
del l[-1]
k=int(l[0])
while k<=int(l[-1]):
    p.append(k)
    k=k+1
for u in range(len(p)):
    if str(p[u]) not in l:
        print(p[u])
        break
