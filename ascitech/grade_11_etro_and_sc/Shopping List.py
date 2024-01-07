
f=open("history.py","r")
qna=input("Would you like to buy the same thing as last time, or would you like to erase your purchase history (Y/N and E to erase)\n")
if qna.lower() == "y" or qna.lower() == "yes":
	ans2=input("Do you have a discount?(Y/N)\n")
	if ans2.lower() == "y" or ans2.lower() == "yes":
		amount=int(input("Please enter the price of the unit:\n$"))
		disc=int(input("enter the value of the discount: \n%"))
		amount=(amount-(amount*(disc/100)))
		print(f.read())
		print(f"With your new discount the total is ${amount}\nReminder:This is only for your latest purchase.")
	else:
	
		print (f.read())
elif qna.lower() == "e":
	f=open("Purchases.py", "w")
	print(f.write(""))
	print("Your history was cleared")

else:
	qte =[]
	product = []
	prices = []
	total = 0
	disc = 0
	while True:
		item = input("Enter the item you want to buy.(Enter 'q' to quit)\n")
		if item.lower()=='q':
			break
		else:
			num = int(input("How many do you want to buy?\n"))
			price = float(input(f"enter the price of the {item}: $"))
			price = price*num

		qte.append(num)
		product.append(item)
		prices.append(price)

		
	print(" -----  YOUR CART  ----- ")
	for item in product:
		print(item)
	for price in prices:
		total = total+price
	print(f"Your total is ${total}")
	ans=input("do you have a discount? (Y/N)\n")
	if ans.lower()=="yes" or ans.lower()=="y":
		value=int(input("enter the value of the discount: \n%"))
		total=total-(total*(value/100))
		print(f"Your final price is ${total}")
	else:
		print(f"Your final price is ${total}")
		
		
		
	expenses=str(total)
	
	f = open("history.py", "a")
	f.write(f"Your previous total was ${expenses}\n")
	f.write(f"\nThe previous item(s) you bought are/is {product}\n")
	
	f.close()
	
	




		
	