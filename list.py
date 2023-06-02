
# *args and *kwargs
# def addition(*args):
#     total = 0
#     for numbers in args:
#         total += numbers
#     print(f'Sum ={total}')

# addition(1,2,3,4,20)
# order x,y,*args,**kwargs
# def myFunction(x,*args,**kwargs):
#     print(x)
#     print(args)
#     for keys,values in kwargs.items():
#         print(f'{keys} = {values}')

# myFunction('Ghana','University of Gh', name='Nat',age='20')
#OOP
class BakingPan:
    unit_price = 5
    def __init__(self,flour,sugar,special_ingredient) -> None:
        self.flour = flour # bread2.flour = 'soft'
        self.sugar = sugar
        self.special_ingredient = special_ingredient

    def bread_name(self):
        return f'{self.special_ingredient} bread'
    def total_price(self,quantity):
        total = quantity* self.unit_price
        return f'Total Price of {quantity} {self.bread_name()} = Ghc {total}'

# flour, sugar, special indredient assigning attribute and parameters

bread1= BakingPan('soft',20,'Wheat')
bread2= BakingPan('hard',10,'Coconut')

print(bread1.total_price(10))
print(bread2.total_price(30))






