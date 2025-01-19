MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "milk":150,
            "water":200,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "milk":100,
            "water":250,
            "coffee":24,
        },
        "cost":3.0,
    }
}
profit=0
resources={
    "water":300,
    "milk":200,
    "coffee":100,
}

def is_resorces_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total=int(input("How many quarters?: "))*0.25
    total+=int(input("How many dimes?: "))*0.1
    total+=int(input("How many nickles?: "))*0.05
    total+=int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successfull(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is your change ${change}")
        
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry thats not enough money. Money is refunded. ")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"enyoy your coffee {drink_name}. Enjoy!")
is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=='off':
        is_on=False
    elif choice=='report':
        print("Water:100ml")
        print("Milk:50ml")
        print("coffee:76g")
        print("Money:$0")
    else:
        drink=MENU[choice] 
        if is_resorces_enough(drink['ingredients']):
            payment=process_coins()
            if is_transaction_successfull(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])

       






    
 

