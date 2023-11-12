#Task1 Data structures introduction
t = ([12, 1.02,'SHANTANU'],["Yellloo",True ])
x = t[1][1]
print(x)

s1 = {342,445454,50,False}
s1.add("sdl")
print()

#Task 2:- Demonstrating The Use Of Tuples
t1 = ("New",24353355433,"Yes",0.00023)
t2 = ("World",14.255554,65,"Order")

print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])

print(t1[0:4])
print(len(t1))
print(t1 + t2)
print(len(t1 + t2))
t3 = ('NewWorldOrder',1.62,100+0.9j,20)
t4 = ('New','World','Order',88+1j,160)
t5 = t3[1:3] + t4[2:4]
#Task 3:- Demonstrating The Use Of List

l1 = ['Kiddo' , 5.23 , 12+36j , 69]
l2 = [99 , 'Is' , False , 68+45j]
print(l1[0])
l1[0] = False
print(l1 + l2)
print(type(list(t1)))

#Task 4:- Implementing The List Functions

l5 = ["Guardians"]
l5.append("the")
print(l5)
l5.insert(1,"of")
print(l5)
l4 = ["Galaxy"]
l5.extend(l4)
