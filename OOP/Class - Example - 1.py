"""Class:       template for creating objects.
                All objects created using same class will
                have the same characteristics.

Objects:        An instance of a class
Instantiate:    Create an instance of a class
Method:         a function defined in a class
Attribute:      a variable bound to an instance of a class
"""

# ------------------------------------------------------------------------------
#    Class Definition
# ------------------------------------------------------------------------------
class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# ------------------------------------------------------------------------------
#    Main Code
# ------------------------------------------------------------------------------
Kenwood = Kettle("Kenwood", 8.99)
print(Kenwood.make)
print(Kenwood.price)
print('-'*80)

Hamilton = Kettle("Hamilton", 14.55)
print(Hamilton.make)
print(Hamilton.price)
print('-'*80)

# Another way to print
print("Models: {} = {}, {} = {}".format(Kenwood.make, Kenwood.price, Hamilton.make, Hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(Kenwood, Hamilton))
print('-'*80)

print(Hamilton.on)
Hamilton.switch_on()
print(Hamilton.on)