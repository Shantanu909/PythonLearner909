#Task1 print a pattern 

for i in range(1,9,1):
    
    for j in range(1,9,1):
         print("#",end = "")
    print()

#Task2 sum of n number of odd and even unmbers 
sum_e = 0
sum_o = 0
for i in range(1,101,1):
    if(i%2==0):
        sum_e = sum_e + i
    else:
        sum_o = sum_o + i
        
print(sum_e)
print(sum_o)

#Task3 print 10,20,30...300

for i in range(10,301,10):
    print(i)

#Task4 print 105,98,91....7
i=105
while(i>0):
    print(i)
    i = i-7
    
#Task5 Wap to find if a number is  Pime number or not usign while loop
d = (int)(input("Please enter the number to be checked"))
i=0
count=0
for i in range(1,d,1):
    if(d%i==0):
        count = count+1
    else:
        count= count+0
if(count>0):
   print(d,"ïs composite")
else:
  print(d,"ïs prime")
    
#Task6 Number inversal of the number given by user
num = (int)(input("Please enter a number"))

i=num
for i in range (2,num,1):
    i = i%10
print(count)


