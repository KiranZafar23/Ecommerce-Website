from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = list(cart.keys())

    if str(product['retailer_sku']) in ' '.join(keys):
        return True

    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = list(cart.keys())

    if str(product['retailer_sku']) in ' '.join(keys):
        return cart[str(product['retailer_sku'])]

    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return int(product['price']) * int(cart_quantity(product, cart))


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0

    for product in products:
        sum += price_total(product, cart)

    return sum

