class Desert:
    def __init__(self, flavor):
        self.flavor = flavor


class IceCream(Desert):
    def __init__(self, flavor):
        super().__init__(self, flavor)

    def __str__(self):
        return "My favortie flavor is " + self.flavor


obj = IceCream("Pistachio")
print(obj)