from products import product_details

def test_product_details():
    expected_output = (
        "Product Id: 101\n"
        "Prodcut name: iPhone\n"
        "Quantity: 1\n"
        "Price: 155000\n"
    )
    assert product_details(101, "iPhone", 1, 155000) == expected_output
