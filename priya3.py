l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print("sample list1:",l)
for i in range(len(l)):#5->0-4
    for j in range((len(l)-i-1)): #5-0-1=4#0-3
        if l[j][1]>l[j+1][1]:#l[0][1]>l[1][1]
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp

print("Expected result:",l)