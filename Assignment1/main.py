### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if ingredients['bread'] - resources['bread'] <= 0 or ingredients['ham'] - resources['ham'] <= 0 or ingredients['cheese'] - resources['cheese'] <= 0:
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        self.dollars = int(input("how many large dollars?: "))
        self.halfDollars = float(input("how many half dollars?: "))
        self.quarters = float(input("how many quarters?: "))
        self.nickels = float(input("how many nickels?: "))
        self.coins =  self.dollars + (self.halfDollars/2) + (self.quarters/4) + (self.nickels/20)
        return self.coins
    
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if self.coins < cost:
            return False
        else:
            return True
        
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources['bread'] -= order_ingredients[sandwich_size]['ingredients']['bread']
        self.machine_resources['ham'] -= order_ingredients[sandwich_size]['ingredients']['ham']
        self.machine_resources['cheese'] -= order_ingredients[sandwich_size]['ingredients']['cheese']

### Make an instance of SandwichMachine class and write the rest of the codes ###
        
SM = SandwichMachine(resources)


while True:

    size = input(("What would you like? (small/ medium/ large/ off/ report):"))

    if size in ['large', 'medium', 'small']:
        if SM.check_resources(recipes[size]['ingredients']):
            coins = SM.process_coins()
            if SM.transaction_result(coins, recipes[size]['cost']):
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
  
