print("le van an")
print("235752021610044")
a= float(input("enter a (a<>0):"))
b= float(input("nhap b: "))
c = float(input("enter c: "))
delta=b*b-4*a*c;
if delta==0:
    print("pt means x1=x2=",-b/(2*a))
if delta>0:
    print("equation has two solutions x1=", (-b+delta**0.5/(2*a), "ca x2=", (-b-delta**0.5/(2*a))))
if delta<0:
    print("unreasonable equation")
