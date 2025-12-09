def product_details(product_id, name, quantity, price):
    result = (
        f"Product Id: {product_id}\n"
        f"Prodcut name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}\n"
    )
    return result
if __name__ = "__main__":
    print(product_details(101, "iPhone", 1, 155000))