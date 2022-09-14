file=open("task16_input.txt",'r')
f=file.read()
# print(f)

fo=open("task16_write.txt",'w')
fo.write(f)
file.close()
