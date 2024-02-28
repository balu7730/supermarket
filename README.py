import base64
from datetime import datetime

name=input("enter your name:")
lists='''
RICE 20/KG
SUGAR 40/KG
KIROSINE 60/KG
GOLD 1000/KG'''
price=0
totalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]
finalamount=0
gst=0
items={"rice":20,"sugar":40,"kerosine":60,"gold":1000}
option=int(input("enter 1 for list of items"))
if option==1:
    print(lists)
for i in range(len(lists)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    elif inp1==1:
        item=input("enter item")
        quantity=int(input("quantity"))
        if item.lower() in items.keys():
            price=items[item]*quantity
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("entered item is not available")
else:
    print("you enterd wring number")

inp3=input("can i bill yes or no")
if inp3=="yes":
    pass
    if finalamount!=0:
        print(25*"=","kiran supermarket",25*"=")
        print(28*" ","wanaparthy")
        print("name:",name,30*" ","date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ","quantity",3*" ",'price')
        for i in range(len(pricelist)):
            print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(50* " ","thanks for visiting")
            print(75*"-")
   
