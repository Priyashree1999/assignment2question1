l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print("sample list1:",l)
for i in range(len(l))
    for j in range((len(l)-i-1)): 
        if l[j][1]>l[j+1][1]:#l[0][1]>l[1][1]
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp

print("Expected result:",l)
