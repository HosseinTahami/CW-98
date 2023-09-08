# Use the Observer Design Pattern for items and Strategy Design Pattern for discount method


class ShoppingCart:
    def init(self):
        self.items = []
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def calculate_discount(self):
        if self.total_price > 100:
            return self.total_price * 0.1
        else:
            return 0

    def checkout(self):
        final_price = self.total_price - self.calculate_discount()

        print(f"Total price: {self.total_price}")

        print(
            f'Discount applied: (self calculate _discount ()]") print(f°Final price after discount: (final_price]")'
        )
        print("final price", final_price)
