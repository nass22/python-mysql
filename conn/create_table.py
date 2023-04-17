from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin",
        database="ranked",
    ) as connection:
        create_table_weapons_query = """
            CREATE TABLE weapons(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            link VARCHAR(255),
            rank_level INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """

        with connection.cursor() as cursor:
            cursor.execute(create_table_weapons_query)
            connection.commit()
            
            print("TABLE successfully created!")
except Error as e:
    print(e)





