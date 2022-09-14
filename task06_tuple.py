# Write a program to demonstrate working with tuples in python.

days=('sunday','monday','tuesday','wednesday','thrusday','friday','saturday')
#tuple unpacking -->we need same amout of variables as tuples have 
day1,day2,day3,day4,day5,day6,day7=(days) 
print("day one is",day1)
#tuple slicing
print(days[:2])
#tuple with one element
names=('karina',)
print(type(names))
#tuples without parenthesis
nums='one','two','three'
print("type of nums is",type(nums))

#min,max and sum method in tuples
grades=(2,5.6,7.5,4,8)
print("minimum gade is",min(grades))
print("maximum grade is",max(grades))
print("total grades are",sum(grades))

#loop in tuple
for i in grades:
    if i>7:
        break
    print(i)