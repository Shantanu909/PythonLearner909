#Task 1:- Assigning the same value to a different variable at a time
#Python Code:
x = y = z = 199
print(x,y,z)
#Output:

#Task 2:- Assigning the different value to a different variable at a time
#Python Code:
S,h,a = 5,6,7
print(S,h,a)
#Output:
#Task 3:- Adding two numbers
#Python Code:
U = 10
V = 20
print(U+V)
#Output:

#Task 4:- Concating two strings
#Python Code:
P = "Bonjour"
Q = "Amigos"
print(P + " " + Q)
#Output:

#Task 5:- Printing the string in different ways using indexing
#Python Code:
P = "Bonjour"
Q = "Amigos"
R = P + " " + Q
print(R[:5])
print(R[::-1])
#Output:

#Task 5:- implemet different operators on strings.
#Python Code:
t = "Rock star"
print(t[2:5])
print(t[:5])
print(t[2:])
print(t[::-1])
print(t[-1::])
print(t[::1])
print(t[1::])
print(t[::2])
print(t[-5:-2])
print('R' in t)
print('s' in t)
print(t*2)
w = "Rock star"
q = "Rock Star"
print(w == q)
print('A' in w)
print('s' not in q)
#Output:


#Task 6:- implemet different operators on strings.
#Python Code:
name = "Rock"
age = 20
marks = 10.2
str1 = 'Hey %s' % (name)
str2 = 'My Age Is %d' % (age)
str3 = 'Bonjour , My Name Is %s , My Age Is %d , And My Mark Is %f' %(name,age,marks)
print(str1)
print(str2)
print(str3)
#Output:

#Task 7:- implementing string methods
#Python Code:
x = "Rock star"
Count = x.count('k')
Title = x.title()
Lower = x.lower()
Upper = x.upper()
print(Count)
print(Title)
print(Lower)
print(Upper)
#Output:
