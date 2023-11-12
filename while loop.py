#While looping

print("Welcome to the code for while loop implementation")
i=0
while i<100:
    i = i+1
    print("**")
    
j=0
while j<10:
    if(j%2==0):
        print(j,"is even")
    else:
        print(j,"is odd")
    j = j+1
    
k=0
while k<69:
    k=k+1
    if(k/2==4):
        continue
    elif(k%2==0):
        print("even")
        if(k==50):
            print("Stop")
            break    