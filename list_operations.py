#Lab 5

#Task 1 List inside Tuple and Tuple inside List

tuple1 = ([1,2,3],[12,34,56])
print(tuple1)

list1 = [(0,2,5),(51,91,60),(0,0,0)]
print(list1)

#Task 2 Making maximum and Minimum of Tuple 
tuple1 = (1,34,24,5454,0,34,9)
max1 = 0
for i in range(0,7,1):
    if(tuple1[i]>max1):
        max1 = tuple1[i]
print(max1)
min1 = 999999999999999999999
for i in range(0,7,1):
    if(tuple1[i]<min1):
        min1 = tuple1[i]
print(min1)

#Task 3: Finding the highest frequency in Tuple
tuple1 = (1,34,24,5454,0,34,9)
c = []
c.append(tuple1.count(tuple1[0]))
c.append(tuple1.count(tuple1[1]))
c.append(tuple1.count(tuple1[2]))
c.append(tuple1.count(tuple1[3]))
c.append(tuple1.count(tuple1[4]))
c.append(tuple1.count(tuple1[5]))
c.append(tuple1.count(tuple1[6]))
max1 = 0
maxi = 0
for i in range(0,7,1):
    if(c[i]>max1):
        max1 = c[i]
        maxi =i
print(tuple1[maxi])
#Task 4:- Demonstrate The Usage Of Dictionary

student_scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 72,
    "David": 90
}

# Accessing values using keys
print(student_scores["Alice"])

student_scores["Eva"] = 78

# Modifying a value
student_scores["Bob"] = 92

if "David" in student_scores:
    print("David's score:", student_scores["David"])
else:
    print("David's score not found")


#Task 5:- Demonstrate The Usage Of Sets

fruits = {"apple", "banana", "orange", "apple", "pear"}
fruits.add("grape")
fruits.remove("banana")
if "orange" in fruits:
    print("We have an orange!")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
union_set = set1.union(set2)         
intersection_set = set1.intersection(set2)  
difference_set = set1.difference(set2)     
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

#Task 6:- Joining The Characters Of Tuples

tuple1 = ('H', 'e', 'l', 'l', 'o')
tuple2 = ('W', 'o', 'r', 'l', 'd')
joined_string1 = ''.join(tuple1)
joined_string2 = ''.join(tuple2)
print("Joined string 1:", joined_string1)
print("Joined string 2:", joined_string2)  
