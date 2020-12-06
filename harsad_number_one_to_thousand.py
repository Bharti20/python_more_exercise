def harsad_number(number):
    i=number
    sum=0
    while i>0:
        a=i%10
        sum=sum+a
        i=i//10
    if number%sum==0:
        print(number) 
      
def number():
    i=1
    while i<100:
        a=harsad_number(i)
        i=i+1
number()
