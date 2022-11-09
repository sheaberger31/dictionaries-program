#-----------------
#Summative dictionary program
#shea berger
#-------------------


#---lists---#
cart = {}


#-----------functions------------------#

def fill_cart():
    drink = 1
    while drink == 1:
        print('type done when you are finished')
        choice = input('pick what you want in your cart ')
        if choice == 'done':        
            drink = 2
        
        
        else:
            price = int(input('How much does it cost '))
            cart[choice] = price
            print(cart)

def display():
    total = sum(cart.values())
    print("your total is")
    print(total)
    
def dbc():
    check = input("Was that all for you today?")
    if "y" in check.lower():
        print("Have a good day")
        
    else:
        option = input("are you addig items or removing items?")
        if "a" in option.lower():
            fill_cart()
            print(cart)
            total = sum(cart.values())
            print(total)
        else:
            print(cart)
            remove = input('which item are you removing from your cart')
            del cart[remove]
            print(cart)
            total = sum(cart.values())
            print(total)
            
        
    

    
    
    


fill_cart()
display()
dbc()