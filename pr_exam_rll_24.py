#Q1.

"""Counting the number of words."""
print("Please enter a sentence.")
sent = input()
n = sent.count(" ")
print("Number of words:")
print(n+1)


"""Counting the number of Capital leters."""
r = len(sent)

count=0
for i in range (0,r,1):
    temp_str =sent[i].isupper()
    if(temp_str==True):
        count = count+1
    else:
        count = count+0

print("Number of Capital letters:")
print(count)


"""Counting the number of small letters."""
count1=0
for i in range (0,r,1):
    temp_str =sent[i].islower()
    if(temp_str==True):
        count1 = count1+1
    else:
        count1 = count1+0
print("Number of small letters:")
print(count1)
        
"""Counting the number of special symbols."""
count2=0
count3=0

for i in range (0,r,1):
    temp_str =sent[i].isspace()
    if(temp_str==True):
        count2 = count2+1
    else:
        count2 = count2+0

for i in range (0,r,1):
    temp_str =sent[i].isalpha()
    if(temp_str==True):
        count3 = count3+0
    else:
        count3 = count3+1

count2 = count3-count2
        
print("Number of special symbols:")
print(count2)




#Q2.
print("Please enter a sentence.")
sent1 = input()

tem = sent1.split()
tn = len(tem)
counter1=0
tem2 = sent1.split()
tem3 = tem2
tem4 = sent1.split()
for i  in range(0,tn,1):
    sp_count=0
    for j in range(i+1,tn-1,1):
        if(tem2[i]==tem2[j]):
            sp_count = sp_count+1
    tem3[i]=sp_count
    for k in range(i,tn-1,1):
        if(tem2[i]==tem2[k]):
            tem2[k]==0
        
fin_count=0
for i in range(0,tn,1):
    if(tem3[i]>0):
        
        fin_count = fin_count+1
print("No. of Words:")
print(fin_count)

for i in range(0,tn,1):
    if(tem3[i]>0):
        print(tem4[i])
        


#q3        
print("Please enter a list of numbers separated by spaces:")
sent1 = input()
sent2 = sent1.split()

# Convert the input values to integers
sent2 = [int(x) for x in sent2]

sent3 = []
seen = set()

# Iterate through the list to remove duplicates while preserving order
for num in sent2:
    if num not in seen:
        seen.add(num)
        sent3.append(num)

print(sent3)
