from enum import Enum

class Products(Enum):
    BURGER = 'burger'
    FRIES = 'fries'
    COLA = 'cola'

class Product:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'{self.name}'



class Cart:
    def __init__(self, user_id: int, products: list[Product] = list()):
        self.user_id = user_id
        self.products = products

    def __repr__(self):
        return f'{self.user_id}, {self.products}'

    def add_product(self, new_product: Product):
        self.products.append(new_product)

class Menu:
    def __init__(self, products: list[Product]):
        self.products = products

    def __repr__(self):
        return f'{self.products}'



carts: dict[int, Cart] = {}


#def get_menu() -> Menu:
    #return menu

def get_user_cart(user_id: int) -> Cart:
    return carts.get(user_id, None)

def create_new_cart(user_id: int) -> Cart:
    cart = Cart(user_id)
    carts[user_id] = cart
    return cart

def add_to_cart(cart: Cart, product: Product) -> Cart:
    cart.add_product(product)
    return cart

def make_order(user: str, callbacks :list[callable]):
    cart = get_user_cart(user)
    #save_cart_to_db(cart)

    for callback in callbacks:
        callback(cart)
        print("Заказ сделан")

    # del[cart]


