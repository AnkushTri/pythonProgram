#Write a program to create, concatenate and print a string and accessing sub-string from a given string.



first_name="Ankush"
last_name="Kumar"

#concatenation strings
full_name=first_name+" "+last_name

#print after concatenation strings
print(full_name)

#Accesing sub string from strings
college_name="ct group of institutions"
print(college_name[0:4])
print(college_name[0:5:2])
print(college_name[0::2])
print(college_name[:5:-1])

'''
#some more method in strings
name = "anKUsh kuMaR"
#string slicing
print(name[0:5:2]) #first for starting ,second for till then and third for how much step
print(name[0::3])
print(name[::-1]) #reverse the string

#uppercase,lowercase and title case
print(name.upper())
print(name.lower())
print(name.title())
#count method
print(name.count("a"))

#find method
print(college_name.find("group"))

#replace method
print(college_name.replace(" ","_"))

#len method --find the length of string
print(len(college_name))

#this is an error,string is immutable so we can't change string using index value but we can replace string 
# name[1]="r"
# print(name)

#strip method ---remove unusable space
bro="  ankit"
print(bro.strip())

'''


