maths=float(input("Enter Marks of Maths:"))
eng=float(input("Enter marks of English:"))
scince=float(input("Enter marks of Scince:"))
merit=(maths+eng+scince)/3
if merit>=90:
    print("A grade")
elif merit>=80 and merit<=89:
    print("B grade")
elif merit>=70 and merit<=79:
    print("C grade")
elif merit>=60 and merit<=69:
    print("D grade")
elif merit>=50 and merit<=59:
    print("E grade")
else:
    print("F grade")    
