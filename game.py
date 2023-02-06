from game_data import MENU,resources


def meth1():
    print("please insert coins : ")
    quater=int(input("how many quaters? : "))
    dimes=int(input("how many dimes? : "))
    nickle=int(input("how many nickle? :"))
    pennies=int(input("how many pennies? : "))
    amount=quater*.25+dimes*.1+nickle*.05+pennies*.01
    return amount


def meth2(str):
    for key in resources:
        d=resources[key]
        resources[key]=resources[key]-MENU[str]["ingredients"][key]
        if(resources[key]<0):
            resources[key]=d
            print(f"sorry not enough {key}")
            return False
    
    return True




cash=0
while True:
    what=input("what would you like ? (espresso/latte/cappuccino) : ")
    if(what=='report'):
        for items in resources:
            print(f"{items}: {resources[items]}")
        print(f"cash :{cash}")
    elif(what=='latte'):
        if meth2(what):
            amount=meth1()
            if(amount>=MENU[what]["cost"]):
                d=MENU[what]["cost"]
                cash=cash+d
                print(f"here is ${amount-d} in change")
                print("here is your latte enjoy")
            else:
                print("sorry thats not nough money : money refunded")
                break
    elif(what=='espresso'):
        if meth2(what):
            amount=meth1()
            if(amount>=MENU[what]["cost"]):
                d=MENU[what]["cost"]
                cash=cash+d
                print(f"here is ${amount-d} in change")
                print("here is your espresso enjoy")
            else:
                print("sorry thats not enough money : money refunded ")
                break
    elif(what=='cappuccino'):
        if meth2(what):
            amount=meth1()
            if(amount>=MENU[what]["cost"]):
                d=MENU[what]["cost"]
                cash=cash+d
                print(f"here is ${amount-d} in change")
                print("here is your cappuccino enjoy")
            else:
                print("sorry thats not enough money : money refunded ")
                break
