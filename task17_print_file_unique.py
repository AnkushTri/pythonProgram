fname=input("enter file name:")
file=open(fname)

words=[]
for line in file:
    words+=line.split()
    words.sort()

# print(words)
li=list()
for word in words:
    if word in li:
        continue
    else:
        li.append(word)
        print(word,end=" ")

# print(li,end="")
