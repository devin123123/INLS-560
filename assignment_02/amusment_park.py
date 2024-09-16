# This lesson focuses on the idea that order is important when using elif. 
age = 101

if age < 4: 
    print("Admission is $0")

elif age < 18: 
    print("Admission is $25")

elif age > 60:
    print("Admission is $35")
#This is not going to work here. Put it before age > 60
# elif age > 100: 
#    print("Admission is $0 and you get a free beer")
else:
    print("Admission is $40")

    