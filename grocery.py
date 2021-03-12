while True:
    budget = float(input("Enter your budget : "))
    available=budget
    break
d ={"name":[], "quantity":[], "price":[]} 

l= list(d.values()) 

name = l[0] 

quantity= l[1] 

price = l[2] 

while True:
     ch = int(input("1.ADD\n2.EXIT\nEnter your choice : ")) 
     
     if ch == 1 and available>0:
         pn = input("Enter product name : ")  
         q = int(input("Enter quantity : "))
         p = float(input("Enter price of the product : "))               
       
         if p>available:
                            
             print("canot by product")  
             continue
             
         else:
             if pn in name:
                 
                ind = na.index(pn) 
                price.remove(price[ind])   
                quantity.insert(ind, q)      
                price.insert(ind, p)    
                available = budget-sum(price)    
                print("\namount left", available) 

             else:
                name.append(pn)
                quantity.append(q)
                price.append(p)
                available= budget-sum(price)
                print("\namount left", available) 
     elif available<= 0:
         print("no amount left")  
            
     else:
         break 
print("\nAmount left : Rs.", available)  

if available in price:  
     
    print("\nyou an buy", na[price.index(available)])   
  
print("\n\n\nGROCERY LIST") 

for i in range(len(name)):
    print(name[i],quantity[i],price[i])
    
