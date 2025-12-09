from products import product_details

def test_product_details():
    expected_output = (
        "Product Id: 101"
        "Prodcut name: iPhone"
        "Quantity: 1"
        "Price: 155000"
    )

assert product_details(101, "iPhone" ,1 , 155000) == expected_output