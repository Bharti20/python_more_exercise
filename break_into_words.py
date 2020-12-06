words = "navgurukul is great"
counter = 0
List=[]
while counter <len(words):
    j=counter
    a=""
    while j<10:
        a=a+words[counter]
        counter=counter+1
        j=j+1
    List.append(a)
    counter=counter+1
print(List)
    