student_detail={
    "name":"karina",
    "age":20,
    "rollno":2021,
    "hobie":"study",
    "favperson":"ankush",
    "favbook":"os"
}

#Accessing value
print("fav person is",student_detail["favperson"])
print("age is ",student_detail["age"])

#desplaying all keys
# for i in student_detail:
    # print(i)

#add new key value pair in dictonary
student_detail['contact']=7973742809
print(student_detail)

#update dictionary
student_detail["age"]=19
print(student_detail)

#remove key value pair from dictionary
student_detail.pop("favbook")
print(student_detail)

#length of dictionary
print("length of dictionary is",len(student_detail))

#copy a dictionay
karina_detail=student_detail.copy()
print("karina's detail",karina_detail)

#delete dictonary
student_detail.clear()
print(student_detail)