number_of_student=int(input("enter the number"))
one_student_expence=int(input("enter the expence"))
monthly_budget=50000
total_manthly_expence=number_of_student*one_student_expence
if total_manthly_expence<=monthly_budget:
    print("hum budget ke ander hai")
else:
    print("hum budget ke bahar hai")