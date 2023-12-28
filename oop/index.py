class Recipe():
    def __init__(self, name, ingredients,time) -> None:
        self.name = name
        self.ingredients = ingredients
        self.time = time

    def toString(self):
        print("I'm a " + self.name + " my ingredients" + \
              str(self.ingredients) + " time " + str(self.time))

pizza = Recipe("Margherita",["dough","cheese", "tomato sauce"], 30)
pasta = Recipe("Carbonara",["penne", "white sauce"], 40)

print(pizza.ingredients)
print(pizza.toString())