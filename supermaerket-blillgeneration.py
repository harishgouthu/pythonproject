from datetime import datetime

name = input('Enter your name: ')

list = '''
Rice      Rs  50/kg
Colgate   Rs  40/100g
oil       Rs  130/kg
Boost     Rs  120/1/2kg
Wheet     Rs  50/kg
Salt      Rs  20/kg
Magi      Rs  20/1
Soaps     Rs  25/1
Surfexcel Rs  110/ltr

'''
price = 0
pricelist = []
totalprice = 0
finalamount = 0
ilist = []
qlist = []
plist = []

items = {'Rice':50,'Colgate':40,'oil':130,'Boost':120,'Wheet':50,'Salt':20,'Magi':20,'Soaps':25,'Surfexcel':110} 


option = int(input('press 1 for the list of items: '))
if option == 1:
    print(list)

for i in range(len(items)):
    inp = int(input('press 1 for buy or prss 2 for exit: ')) 
    if inp == 2:
        break
    if inp == 1:
        item = input('Enter your items: ')
        quantity = int(input('Enter your quantity: '))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalamount = gst+totalprice
        else:
            print('you entered item is currently not available')
    else:
        print('you have entered wrong number')
    inp1 = input('select yes or no for bill the items: ')
    if inp1 == 'yes':
        pass
        if  finalamount != 0:
            print(30*'=','hareesh super market',30*'=')
            print(30*' ','kakinada')
            print('Name:',name,30*' ','Date:',datetime.now())
            print(60*'-')
            print('sn0',12*' ','items',10*' ','quantity',6*' ','price')
            for i in range(len(pricelist)):
                print(i,9*' ',5*' ',ilist[i],12*' ',qlist[i],13*' ',plist[i])
            print(60*'-')
            print(35*' ','Totalamount:','Rs',totalprice)
            print('GSTamount:',38*' ','Rs',gst)
            print(60*'-')
            print(34*' ','Final amount:','Rs',finalamount)
            print(60*'-')
            print(36*' ','Thanks for visiting')
            print(60*'-')            
                


