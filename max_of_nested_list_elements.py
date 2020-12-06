def marks_list(marks):
    index=0
    while index<len(marks):
        j=0
        a=0
        while j<len(marks[index]):
            if marks[index][j]> a:
                a=marks[index][j]
            j=j+1
        print(a)
        index=index+1
marks_list([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]])
