stri =input("enter string")
i=1
new =""
j=0
size = len(stri)
for j in range(len(stri)):
    if(j==len(stri)-1):
        if i==1:
            new = new +stri[j]
            new=new+str(i)
            break
        else:
            new=new+str(i)
            break
    if i==1:
        new =new+stri[j]
    if(stri[j]==stri[j+1]):
        i=i+1
    
    else:
        new =new+str(i)
        i=1

print(new)
