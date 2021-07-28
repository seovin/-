alist=[]
def d(n):
    if n<10:
        a = 2*n
    if 9<n<100: 
        a = n+n%10+n//10
    if 99<n<1000: 
        a = n+n//100+(n//10)%10+n%10
    if 999<n<10000: 
        a = n+ n//1000 + (n//100)%10 + (n//10)%10 +n%10
    alist.append(a)

for i in range(1,10000):
    d(i)    
for i in range(1,10000):
        if i not in alist:
            print(i)