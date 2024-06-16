class Cashier:
    def __init__(self):
        pass

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
