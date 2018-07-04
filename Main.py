import mysql.connector

cnx = mysql.connector.connect(user='michael', password='_tacocat_',
                              host='instancem.cf4rtyoqhdsw.us-east-1.rds.amazonaws.com',
                              database='warships')
cursor = cnx.cursor()

ships_processed = [
    {
        "nation": "BOGUS",
        "name": "BOGUS",
        "class": "CA",
        "tier": "5",
        "survivability": "99",
        "artillery": "9",
        "aa": "96",
        "torpedo": "32",
        "aircraft": "3",
        "maneuverability": "11",
        "concealment": "34"
    },
]
#query template
query = ("insert into ships (nation, name, class, tier, survivability, artillery, aa, torpedo, aircraft, maneuverability, concealment) "
         "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

#loop through processed ships and insert them into mysql
for ship in ships_processed:
    data_ships = (
                ship["nation"],
                ship["name"],
                ship["class"],
                ship["tier"],
                ship["survivability"],
                ship["artillery"],
                ship["aa"],
                ship["torpedo"],
                ship["aircraft"],
                ship["maneuverability"],
                ship["concealment"])
    cursor.execute(query, data_ships)

cnx.commit()
cursor.close()
cnx.close()
