def add (self, product):
    product_id = str(product.id)

    if product_id in self.cart:
        pass
    else:
        self.cart[product_id] = {'price': str(product.price)}

    self.session.modified = True