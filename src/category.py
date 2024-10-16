from src.product import Product
from src.exeptions import ZeroQuantityProduct

class Category:
    name: str
    description: str
    list_product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__list_product = products
        Category.category_count += 1
        Category.product_count += len(products)

 #   def __str__(self):
#      return f'{self.name}, колличество продуктов: {self.product_count} шт.'

    def __str__(self):
        total_quantity = 0
        for item in self.__list_product:
            total_quantity += item.quantity
        return f"{self.name}, колличество продуктов: {total_quantity} шт."


    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct('Нельзя добавить товар с нулевым количеством')
            except ZeroQuantityProduct as e:
                print(str(e))
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ''
        for product in self.__list_product:
            product_str += f'\n{str(product)}'
        return product_str

    @property
    def products_in_list(self):
        return self.__list_product

    def middle_price(self):
        try:
            return sum([product.price for product in self.products_in_list]) / len(self.products_in_list)
        except ZeroDivisionError:
            return 0
