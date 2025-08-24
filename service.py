
class Product:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'{self.name}'



class Cart:
    def __init__(self, user: any, products: list[Product] = list()):
        self.user = user
        self.products = products

    def __repr__(self):
        return f'{self.user}, {self.products}'

    def add_product(self, new_product: Product):
        self.products.append(new_product)


class Menu:
    def __init__(self, products: list[Product]):
        self.products = products

    def __repr__(self):
        return f'{self.products}'


menu = Menu([
    Product('Бургер'),
    Product('Пицца'),
    Product('Кола'),
]
)

carts: dict[int, Cart] = {}


def get_menu() -> Menu:
    return menu

def get_user_cart(user: int) -> Cart:
    return carts.get(user, None)

def create_new_cart(user: int) -> Cart:
    cart = Cart(user)
    carts[user] = cart
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


