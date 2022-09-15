from ast import literal_eval


def convert_to_json(products):
    all_products = []

    for product in products:
        products = {}
        products['retailer_sku'] = product.retailer_sku
        products['brand'] = product.brand
        products['color'] = product.color
        products['price'] = product.price
        products['currency'] = product.currency
        products['gender'] = product.gender
        products['name'] = product.name
        products['url'] = product.url
        products['status'] = product.status

        products['image_url'] = literal_eval(product.image_urls)
        products['description'] = product.description
        products['care'] = product.care
        products['category'] = product.category

        products['skus'] = literal_eval(product.skus)
        all_products.append(products)

    return all_products


def imagestring_to_json(orders):
    all_orders = []

    for order in orders:
        orders = {}
        orders['id'] = order.id
        orders['name'] = order.name
        orders['quantity'] = order.quantity
        orders['price'] = order.price
        orders['product'] = order.product
        orders['date'] = order.date
        orders['status'] = order.status
        orders['phone'] = order.phone
        orders['address'] = order.address
        orders['image_url'] = literal_eval(order.image)

        all_orders.append(orders)

    return all_orders
