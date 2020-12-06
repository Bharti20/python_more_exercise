def harsad_number(number):
    i=number
    sum=0
    while i>0:
        a=i%10
        sum=sum+a
        i=i//10
    if number%sum==0:
        return True 
    else:
        return False
print(harsad_number(42))