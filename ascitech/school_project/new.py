
monster = [0,0,0]
for i in monster :
    monster[i]=int(input("Enter a number: "))

def add(x,y,z):
    c=x+y
    d=x+c
    return d
s=add(monster[0],monster[1],monster[2])
print(s)