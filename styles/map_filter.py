menu = ['americano', 'cappucino', 'latte']

def add_sugar(coffee):
    return coffee + ' with sugar'

def print_array(arr):
    for x in arr:
        print(x)

print_array(menu)
sweet_coffees = map(add_sugar, menu)
print_array(sweet_coffees)

def stars_with_c(coffee):
    return coffee[0] == 'c'

c_coffee = filter(stars_with_c, menu)
print_array(c_coffee)
