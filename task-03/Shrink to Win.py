n = int(input())
count=0
k = n
while(k>0):
    count=count+1
    k=k//10
i = 1
sum=0
count1 = 0
if len(str(n)) ==1:
    print(0)
    exit()
for i in range(count):
    while(n>0):
        sum=sum+n%10
        n=n//10
    count1 = count1 + 1;
    if len(str(sum)) != 1:
        n = sum
        sum = 0
    else:
        break;
print(count1)
