from vending_machine import TeaFactory, CoffeeFactory, HotDrinkMachine


def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':
    # entry = input("What kind of drink would you like?")
    # drink = make_drink(entry)
    # drink.consume()

    # Using Hot Drink
    hdm = HotDrinkMachine()
    hdm.make_drink()

