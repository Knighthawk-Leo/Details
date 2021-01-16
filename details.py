f=open("result.txt","a")
x=1
f.write("NAME \t\t MARKS\n")
while (x>0):
    a=str(raw_input("enter name of candidate"))
    b=str(raw_input("enter marks obtained by student"))
    s=(a+"\t\t"+b+"\n")
    f.write(s)
    k=raw_input("do you want to add more details")
    if (k=="y"):
        x=x+1
    else:
        x=0
f.close()
