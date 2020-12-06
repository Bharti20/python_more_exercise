list1 = [1, 5, 10, 12]
list2 = [1, 2, 10, 13, 16,16,20]
i=0
new_list=[]
if len(list1)>len(list2):
    
    while i<len(list1):
        j=0
        while j<=len(list2)-1:
            if list1[i] not in new_list:
                new_list.append(list1[i])
            elif list2[j] not in new_list:
                new_list.append(list2[j])
            j=j+1
        i=i+1
    print(new_list)
else:
    while i<len(list1):
        j=0
        while j<=len(list2)-1:
            if list1[i] not in new_list:
                new_list.append(list1[i])
            elif list2[j] not in new_list:
                new_list.append(list2[j])
            j=j+1
        i=i+1
    print(new_list)