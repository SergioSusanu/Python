# caf or decaf, small, medium, large, toppings: milk, soy milk, almond milk
base_coffee = {1:{'type':'regular', 'price':1.99},
               2:{'type':'decaf', 'price':2.30}}
size = {1:{'size':'medium','price':1},
        2:{'size':'medium','price':2}}

def calc_subtotal(items):
    sum = 0
    for x in items:
        sum+=x["price"]
    return sum

def get_inputs():
    print("Coffee offerings today:")
    print(base_coffee)
    base_c = base_coffee[int(input("Select coffee type:"))]

    print("Coffee size:")
    print(size)
    base_s = size[int(input("Select coffee size:"))]
    return base_c, base_s

print(calc_subtotal(get_inputs()))
