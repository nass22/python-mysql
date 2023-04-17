from mysql.connector import connect, Error

try:
  with connect(
      host="localhost",
      user="username",
      password="password",
  ) as connection:
      create_db_query = "CREATE DATABASE ranked"
      
      with connection.cursor() as cursor:
          cursor.execute(create_db_query)
          
          print("DB successfully created!")
except Error as e:
  print(e)


