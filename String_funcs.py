
X = "Shantanusinh Parmar"

Y = len(X)
print(Y)
i = Y+1
j = Y-i
k = j-1
l = k-1
m = l-1
print(X[j])
print(X[k])
print(X[l])
print(X[m])

print(X[10],X[11],X[12],X[13],X[14])


""" remaining progs
"""

##find function
Str1 = "Joe roganpodcast"
i = Str1.find("rogan")
print(i)

##replace
Str2 = Str1.replace("roganpodcast", "rogan podcast")
print(Str2)


##Rfind
Str2 = "ABCD ABCD ABCD ABCD"
"""to get the index value of  arepeated digit"""
i = Str2.rfind("A")
print(i)

"""Task: S = Shantanusinh Parmar, count the number of As
replace a with x"""
S = "Shantanusinh Parmar"
i = S.count("a")
a = S[3::]
b = S[0:3]
Strq = a.replace("a","b",1)
c = b+Strq
print(c)
S = S.replace("a","b")

"""Some standard functions"""

##Capitalsize first word
Str1 = "conan"
Str1 = Str1.capitalize()
print(Str1)

##Casefold, used to de-capitalize strings
Str2 = "Higgs Boson"
print(Str2.casefold())

##center. use to fill up empty spaces
Str3 = "925 753"
print("Please find the OTP at your phn number ",Str3.center(20,"X"))

##expand tabs, replaces atbs with spaces
Str4 = "Particle   physics      "
print(Str4.expandtabs())

##index, gives lowest index number where a substring starts
Str5 = "Sheldon Lee Cooper"
print(Str5.index("don"))

##rindex, gives lowest index number from rear where a substring starts
Str6 = "Sheldon Lee Cooper"
print(Str6.rindex("e"))

##isalnum,  gives boolean value of whether there are only alpha numeric values in a string
Str6 = "#$%@^!*(&#(@&*$((#*"
print(Str6.isalnum())

##isalpha, gives boolean value if a string is only alphabetic
Str7 = "Manhattan Project5"
print(Str7.isalpha())

##isascii, gices a boolean value if a string is only ASCII
Str8 = "a b c d E F G H I J K L M N O P Q R S T U V W X Y Z"
print(Str8.isascii())


##isdecimal, gives boolean value if a string has only decimal numbers
Str9 = "50222362F"
print(Str9.isdecimal())

##isdigit, gives boolean value if a string is only digits
Str10 = "01234566789"
print(Str10.isdigit())

##isidentifier, gives boolean value if a string is a reseved keyword
Str11 = "print"
print(Str11.isidentifier())


##islower, gives boolean value if a string is only lowerc cased
Str12 = "Yo hablas espanol"
print(Str12.islower())

##isnumeric, gives boolean value if a string is only numeric
Str13 = "00001110010101010001111"
print(Str13.isnumeric())

##isprintable, gives boolean value if a string is only numeric
Str14 = "Ma Halo Hawaii, $$#%#563}||{: Σ ?w$"
print(Str14.isprintable())

##isspace, gives boolean value if a string is only whitespace
Str15 = "WHITESPACEINCLUDE SPACEAND    TABAND\
ENTER"
print(Str15.isspace())

##istitle, gives boolean value if a string has first letter capital
Str16 = "Chris Hemmsworth"
print(Str16.istitle())

##format,insert elements
Str17 = "Hello {}friends this {} a code for formatting"
print(Str17.format("amigos ","is"))

##zfill,insert s before string
Str18 = "Ayo man What ae yo doin"
print(Str18.zfill(30))

##isupper, chec fro uppercase char
Str19 = "RAGNAROK"
print(Str19.isupper())


