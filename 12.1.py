class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана: ", self.restaurant_name, "\nТип кухни: ", self.cuisine_type)

    def open_restaurant(self):
        print("\nРесторан открыт")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["пломбир", "ванильное", "фисташковое", "шоколадное"]

    def display_flavors(self):
        print("\nВкусы мороженого:")
        for flavor in self.flavors:
            print(flavor)


stand = IceCreamStand("Мороженица", "Кафе - Мороженое")
stand.describe_restaurant()
stand.display_flavors()
stand.open_restaurant()
