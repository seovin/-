def hannum(n):
    if 0<n<100:
        alist.append(n)
    if 99<n<1000: #456
        if (n//100)+(n%10) == ((n//10)%10)*2:
              alist.append(n)
    
alist = []
count = int(input())
value = 0
for i in range(1,count+1):
    hannum(i)
for i in range(1,count+1):
    if i in alist:
        value = value + 1
print(value)