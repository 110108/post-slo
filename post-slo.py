#pavel yaskut
#4/4/2019
fn=input("Enter your first name: ")
ln=input("Enter your last name: ")
print("\nHello "+fn+" "+ln)
while True:
    db=input("\nPlease Enter Your Daily Budget: ")
    try:
        db=int(db)
        break
    except:
        pass
ds=0
em=0
cm=999999999999999999
for i in range(0,3,1):
    while True:
        mc=input("\nHow much do you spend on meal "+str(i+1)+": ")
        try:
            mc=int(mc)
            break
        except:
            pass
    if(em<mc):
        em=mc
    if(cm>mc):
        cm=mc
    db-=mc
    ds+=mc
    print("\nYou have $"+str(db)+" remaining in your budget")
print("You spent a total of $"+str(ds))
print("Your most expensive meal was $"+str(em))
print("Your cheapest meal was $"+str(cm))
print("Each meal cost an average of $"+str(ds/3))