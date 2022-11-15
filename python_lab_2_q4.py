a=input("Enter a string to count its charatcters: ")
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
    



