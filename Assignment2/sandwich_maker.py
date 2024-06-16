
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if ingredients['bread'] - self.machine_resources['bread'] <= 0 or ingredients['ham'] - self.machine_resources['ham'] <= 0 or ingredients['cheese'] - self.machine_resources['cheese'] <= 0:
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.machine_resources['bread'] -= order_ingredients[sandwich_size]['ingredients']['bread']
        self.machine_resources['ham'] -= order_ingredients[sandwich_size]['ingredients']['ham']
        self.machine_resources['cheese'] -= order_ingredients[sandwich_size]['ingredients']['cheese']
