#Write a program to create, append, and remove lists in python.
#create list of number type
number=[1,5,7.5,11]

# a list of string type
words=['os','python','dbms','flat']

#a list of mixed type
mixed=['mathe',1,"datastructure",2]


#append method
subjects=["Flat","Software Engineering","Math","Computer Network"]
# print(subjects)
subjects.append("Python")
subjects.append("DBMS")
print("after appending ",subjects)

#remove method
subjects.remove("Math")
print("after romoving math from sujects:\n", subjects)

#append a list into new empty list
new_subject = []
print("Initial element in new subject",new_subject)
for suject in subjects:
    new_subject.append(suject)
print("after appending subjects into new subject list:\n",new_subject)






#some more list method
new_list=['ram','ankush','srishti','karina','ram']
#insert method is used to insert a element in list at specific index
# new_list.insert(2, "ERP")

#exend method--is used to merge to list
# new_list.extend(subjects)

#pop method is used to delete last element of a list
# new_list.pop()

#sort method is used sort a list by alaphaet
new_list.sort()

#reverse method is used to reverse the element of  list
new_list.reverse()

#count the a element of list
# print(new_list.count("ram"))


# print(new_list)
'''

'''
