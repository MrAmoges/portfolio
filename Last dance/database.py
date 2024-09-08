import psycopg2
from psycopg2 import sql

db_name = 'Evos'
user = 'postgres'
host = 'localhost'
port = 5432
password = '9004'

def get_connection():

    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            host=host,
            port=port,
            password=password
        )
        return conn
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

def check_user(telegram_id):
    conn = get_connection()
    if conn is None:
        return False

    try:
        cur = conn.cursor()

        query = sql.SQL("SELECT * FROM Users WHERE telegram_id = %s;")
        cur.execute(query, (telegram_id,))
        
        user = cur.fetchone()
        conn.close()

        return user is not None 
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return False

def add_user(telegram_id, phone_number):
    conn = get_connection()
    if conn is None:
        return False

    try:
        cur = conn.cursor()

        query = sql.SQL("INSERT INTO Users (telegram_id, phone_number) VALUES (%s, %s);")
        cur.execute(query, (telegram_id, phone_number))
        
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")
        return False


def add_product(product_name,product_desc,product_photo,product_price):
    db_name = 'Evos'
    user = 'postgres'
    host = 'localhost'
    port = 5432
    password = '9004'

    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(f"""INSERT INTO products (products_name, description, photo, product_price) 
                   VALUES ('{product_name}','{product_price}','{product_desc}','{product_photo}');""") 
    connect.commit()  
    connect.close()  

    print("Товар успешно добавлен.")

def delete_product(product_name):
    db_name = 'Evos'
    user = 'postgres'
    host = 'localhost'
    port = 5432
    password = '9004'

    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute("DELETE FROM products WHERE product_name = %s;", (product_name,))
    connect.commit()  
    connect.close()    
    print("Товар успешно удалён.")  
    
def update_product(id, product_name, product_price):
    conn = get_connection()
    if conn is None:
        return False

    try:
        cur = conn.cursor()
        query = sql.SQL("""
            UPDATE products 
            SET products_name = %s, product_price = %s 
            WHERE id = %s;
        """)
        cur.execute(query, (product_name, product_price, id))
        conn.commit()
        conn.close()
        print("Product successfully updated.")
    except Exception as e:
        print(f"Error updating product: {e}")
        return False    
    

def add_basket(user_id, product_name, product_amount, total_price, location):
    conn = get_connection()
    if conn is None:
        return False

    try:
        cur = conn.cursor()
        query = """
        INSERT INTO basket (telegram_id, product_name, product_amount, total_price, location) 
        VALUES (%s, %s, %s, %s, %s);
        """
        values = (user_id, product_name, product_amount, total_price, location)
        cur.execute(query, values)
        conn.commit()
        return True
    except Exception as e:
        print(f"Ошибка при добавлении товара в корзину: {e}")
        return False
    finally:
        cur.close()
        conn.close()

def delete_basket(telegram_id):
    db_name = 'Evos'
    user = 'postgres'
    host = 'localhost'
    port = 5432
    password = '9004'
    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute("DELETE FROM basket WHERE telegram_id = %s;",(telegram_id,))
    
    connect.commit()  
    connect.close()    

def add_orders(product,phone_number,location,total_price):
    db_name = 'Evos'
    user = 'postgres'
    host = 'localhost'
    port = 5432
    password = '9004'


    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(f"""INSERT INTO orders (product, phone_number, location, total_price) 
                   VALUES ('{product}','{phone_number}','{location}','{total_price}');""") 
    connect.commit()  
    connect.close()  

    print("Заказ успешно добавлен.")

def delete_orders(id):
    db_name = 'Evos'
    user = 'postgres'
    host = 'localhost'
    port = 5432
    password = '9004'

    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(f"DELETE FROM orders WHERE ('{id}'); ")
    connect.commit()  
    connect.close()    
    print("Заказ успешно удалён.")  

def update_orders(id,product,phone_number,location,total_price):
    db_name = 'Evos'
    user = 'postgres'
    host = 'localhost'
    port = 5432
    password = '9004'

    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(f"""UPDATE orders SET {product},{phone_number},{location},{total_price} WHERE {id};""") 
    connect.commit()  
    connect.close() 
    print("Заказ успешно изменен.")