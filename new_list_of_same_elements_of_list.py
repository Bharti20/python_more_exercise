list1 = [1,2,3,4,5]
list2 = [2,1,3,4]
i=0
new_list=[]
if len(list1)>len(list2):
    
    while i<len(list1):
        j=0
        while j<=len(list2)-1:
            if list1[i]==list2[j]:
                new_list.append(list1[i])
            j=j+1
        i=i+1
    print(new_list)
else:
    while i<len(list1):
        j=0
        while j<=len(list2)-1:
            if list1[i]==list2[j]:
                new_list.append(list1[i])
            j=j+1
        i=i+1
    print(new_list)