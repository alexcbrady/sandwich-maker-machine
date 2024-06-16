import data
from sandwich_maker import SandwichMaker
from cashier import Cashier




# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
SM = SandwichMaker(resources)
cashier_instance = Cashier()



def main():
    ###  write the rest of the codes ###

    while True:

        size = input(("What would you like? (small/ medium/ large/ off/ report):"))

        if size in ['large', 'medium', 'small']:
            if SM.check_resources(recipes[size]['ingredients']):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, recipes[size]['cost']):
                    print(f"Here is ${coins - recipes[size]['cost']} in change.")
                    print(f"{size} sandwich is ready. Bon appetit!")
                    SM.make_sandwich(size, recipes)
                else:
                    print("Sorry that's not enough money. Money refunded.")

        
        elif size == 'off':
            break
        
        elif size == 'report':
            print(f"Bread : {SM.machine_resources['bread']} slice(s)")
            print(f'Ham: {SM.machine_resources["ham"]} slices(s)')
            print(f'Cheese : {SM.machine_resources["cheese"]} pound(s)')


if __name__=="__main__":
    main()
