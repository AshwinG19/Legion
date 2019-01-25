#ashwin
n,q=map(int,input().split())
print("Prime numbers between",n,"and",q,"are:")
for num in range(n,q + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
