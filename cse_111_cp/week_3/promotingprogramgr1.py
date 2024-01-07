# balanda  , manya , kwadeba , malombo , christiane , bulundwe , bulambo
# grade 12 sc
# ascitech 
# promoting program 
# mr. jack 
x=int(input("how many items are you going to purchase ?"))
y=int(input("how much are you going to pay ?"))
if x>15 :
    z=y-(y*20/100)
    print("the total with the discount is",z,"$")
elif 10<x<14 :
    k=y-(y*15/100)
    print("the total with the discount is",k,"$")
elif 6<x<9 :
    l=y-(y*8/100)
    print("the total with the discount is",l,"$")
else :
    print("You don't have any discount")