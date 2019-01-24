#ashwin
N,Q=map(int,input().split())
if(N<=100000):
    for i in range(N,Q+1):
    if(i%2!=0):
        print(i)
else:
    print("invalid")
