P=float(input("Enter Prize(Amount of Money):"))
R=float(input("Enter Rate Of Intrest:"))
T=float(input("Enter Time(In Year):"))
N=float(input("Enter Net Price:"))
Si=P*R*T/100
Ci=P*(1+R/100*N)**(N*T)
print("Simple Intrest",Si)
print("Coumpound Intrest",Ci)
