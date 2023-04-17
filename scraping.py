import requests
from bs4 import BeautifulSoup
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="admin",
        database="ranked",

    ) as connection:
        
        URL = "https://www.wzranked.com/mw2/meta/guns"

        r = requests.get(URL)
        soup = BeautifulSoup(r.content, "html.parser")

        results_table = soup.find("tbody")

        val = []

        for row in results_table.find_all("tr"):
            
            rank = row.find("td", class_="text-custom-text-secondary").get_text()
            weapon = row.find("td", class_="text-custom-text-primary")
            link = weapon.find("a")
            name = link.find("div", class_="").get_text()
            url_weapon = link['href']

            val.append((name, url_weapon, rank))
        
        
        with connection.cursor() as cursor:
            insert_weapons_query = """
                    INSERT INTO weapons (name, link, rank_level) VALUES (%s, %s, %s)
                """
            cursor.executemany(insert_weapons_query, val)
            connection.commit()
            
            print(cursor.rowcount, "ROW(s) successfully added!")
            
except Error as e:
    print(e)


