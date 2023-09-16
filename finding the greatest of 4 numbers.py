a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
d=int(input("Enter the number: "))

if(a>b):
   large1 = a
else:
   large1 = b

   if(c>d):
      large2 = c
   else:
      large2 = d

      if(large1>large2):
         large=large1
      else:
         large=large2
         
         print("the greatest number is:",large)