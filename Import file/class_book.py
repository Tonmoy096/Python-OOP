class Book:
    def __init__(self, name, author):
        self.name=name
        self.author=author
        self.price=250

    def update_price(self,price):
        self.price=price
    def get_price(self):
        return self.price
    
    def view(self):
        print("Book Name:",self.name,"\nAuthor:",self.author,"\nprice:",self.price)

