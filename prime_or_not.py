#ashwin
n=int(input())
if(n<=1000):
	for i in range(2,n):
		if(n%i==0):
			print(" not a prime number")
		else:
		print(" a prime number")
else:
	print("invalid")
