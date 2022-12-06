li=[]
for i in range(1,26):
    li.append(i)
print(li)
li=[i for i in li if(i%2==0)]
print(li)