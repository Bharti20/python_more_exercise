def List_function(same_list):
    i=0
    unique_list=[]
    while i<len(same_list):
        a=same_list[i]
        if a not in unique_list:
            unique_list.append(a)
        i=i+1
    return unique_list
print(List_function(["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]))