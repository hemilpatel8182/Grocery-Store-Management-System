from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT product.product_id, product.product_name, product.uom_id, product.price_per_unit, uom.uom "
    "FROM product inner join uom on product.uom_id=uom.uom_id;")

    cursor.execute(query)

    response = []

    for (product_id, product_name, uom_id, price_per_unit, uom) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'name' : product_name,
                'id' : uom_id,
                'price_per_unit' : price_per_unit,
                'uom' : uom
            }
        )


    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into product "
    "(Product_Name, uom_id, price_per_unit)"
    "values (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("delete from product where product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 12
))