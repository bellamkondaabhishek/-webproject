from datetime import datetime
name = (input("enter a name : "))#.upper()
lists ='''
PANEER PIZZA🍕 ;119/-
CORN PIZZA 🍕:119/-
TANDOORI PIZZA 🍕:129/-
SPICY CHICKEN PIZZA 🍕:129/-
CHEESY OCEAN PIZZA 🍕:199/-
FRIEDS 2 PCS🍗 :129/-
FRIED WINGS 4 PCS 🍗:109/-
CHICKEN POPCORN 🍿 [SMALL 110GR]:119/-
CHICKEN POPCORN 🍗🍿[LARGE 220GR]:229/-
PANNER SANDWICH 🧀🍿:49/-
EGG SANDWICH 🌭 :49/-
CHICKEN SANDWICH 🌭:59/-
CLASSIC BURGER 🍔:99/-
PANNER BURGER 🍔:119/-
CLASSIC CHICKEN BURGER 🍔 :139/-
PANNER ROLL🥖 :79/-
CLASSIC CHICKEN ROLL 🥖 :89/-
SPICY CHICKEN ROLL 🥖:99/-
VEG RAMIN 🍜 :109/-
EGG RAMIN 🍜 :159/-
SPRITE 🥤 :20/-
THUMPS'UP 🥤:20/-
MOJITO 🥤:49/-
BLACK CURRENT 🥤:49/-
BLUE BERRY 🥤:59/-
WATER BOTTLE [SMALL]:10/-
WATER BOTTLE [BIG]:20/-
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rate of items()
items={'PANEER PIZZA':119,
'CORN PIZZA': 119,
'TANDOORI PIZZA': 129,
'SPICY CHICKEN PIZZA': 129,
'CHEESY OCEAN PIZZA': 199,
'FRIEDS 2 PCS': 129,
'FRIED WINGS 4 PCS':109,
'CHICKEN POPCORN [SMALL 110GR]': 119,
'CHICKEN POPCORN [LARGE 220GR]': 229,
'PANNER SANDWICH ':49,
'EGG SANDWICH':49,
'CHICKEN SANDWICH':59,
'CLASSIC BURGER':99,
'PANNER BURGER':119,
'CLASSIC CHICKEN BURGER':139,
'PANNER ROLL' :79,
'CLASSIC CHICKEN ROLL' :89,
'SPICY CHICKEN ROLL ':99,
'VEG RAMIN':109,
'EGG RAMIN':159,
'SPRITE':20,
'THUMPUP':20,
'MOJITO':49,
'BLACK CURRENT':49,
'BLUE BERRY':59,
'WATER BOTTLE [SMALL]':10,
'WATER BOTTLE [BIG]':20,
}
option = int(input("for list  of items press 1:"))
if option==1:
    print(lists)
for i in range (len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit :"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items :").upper()
        quantity=int(input("enter quantity :" ))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry your entered item is not avaliable ")
    else:
        print("you enterd wrong number ")
    inp=input("can i Bill The Items Yes or No : ")
    if input=='yes' or 'YES' :
        if input=='no' or 'NO':
            exit
            
        pass
        if finalamount!=0:
            print(29*"=","CRISPY CHEESY WORLD",50*"=")
            print(29*"=","RUDRAMPETA BY-PASS",50*"=")
            print("Name:",name,20*" ",30*" ","date:",datetime.now())
            print(100*" ")
            print("sno" ,10*" ",'items',18*" ",'quantity',32*" ",'price')            
            for i in range (len(pricelist)):
                print(i,10*" ",ilist[i],18*" ",qlist[i],32*" ",plist[i])
            print(100*"-")
            print(70*" ",'totalamount:','rs',totalprice)
           # print(15*" ","gst amount",26*" ",'rs',gst)
            print(100*"-")
            print(70*" ",'finalamount:','Rs',totalprice)
            print(100*"-")
            print(30*" "," 🍽 🤭THANKS FOR VISITING ❤")
            print(33*" "," 🍴 🍽   VISIT AGAIN 🍽🍴 ")
            print(100*"-")
    
                