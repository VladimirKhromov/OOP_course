class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)



lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']



shop_items = {}

for st in lst_in:
    name, weight, price = st.split(":")[0], st.split()[-2], st.split()[-1]
    items = ShopItem(name, weight, price)
    if items in shop_items:
        shop_items[items][1] += 1
    else:
        shop_items[items] = [items, 1]


print(shop_items)
