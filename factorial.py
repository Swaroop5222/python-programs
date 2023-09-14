num=int(input("Enter the number\n"))
fact=1
i=1
if(num==0 or num== 1):
    print("1\n")
else:
  while(i<=num):
    fact=fact*i
    i+=1

print(f"The factorial of {num} is {fact}")