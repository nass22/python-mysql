from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="username",
        password="password",
        database="ranked",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM weapons")
            results = cursor.fetchall()

            for x in results:
                print(x)
except Error as e:
    print(e)