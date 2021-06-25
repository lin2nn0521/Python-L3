b=list()
a=input()
c=0

for i in range(len(a)):
        if a[i]==("("):
            b.append("(")
            c+=1
        elif a[i]==(")"):
            c-=1
            if ("(") in b:
                b.pop()
        else:break
if len(b)==0 and c==0:
    print("yes")
else:
    print("no")    