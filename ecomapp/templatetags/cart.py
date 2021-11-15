from django import template


register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    val = cart.values()
    # print(keys)
    for id in keys:
        # print('ffff',id,product.id)
        # print('gggg',type(id),type(product.id))
        if int(id) == product.id:
            return True
    print('kkkk',product,keys,cart,val)
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    # val = cart.values()
    # print(keys)
    for id in keys:
        # print('ffff',id,product.id)
        # print('gggg',type(id),type(product.id))
        if int(id) == product.id:
            return cart.get(id)
    # print(product,keys,cart,val)
    return 0


@register.filter(name='price_total')
def price_total(product,cart):
    return product.prod_price * cart_quantity(product , cart)






@register.filter(name='grand_total')
def grand_total(product,cart):
    sum = 0
    for i in product:
        sum += price_total(i,cart)
    return sum