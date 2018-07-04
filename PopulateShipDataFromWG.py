import datetime
import mysql.connector
import wargaming

print("fetching data from wargaming", end='')
# Connection to WarGaming API
wows = wargaming.WoWS('3672a1d96819ef8bfe0ac902ad887a00', region='asia', language='en')

all_ships = []
i = 1
for i in range(1, 4):
    page = wows.encyclopedia.ships(fields=[
        "name",
        "nation",
        "type",
        "tier",
        "is_premium",
        "default_profile.armour.total",
        "default_profile.weaponry.aircraft",
        "default_profile.weaponry.anti_aircraft",
        "default_profile.weaponry.artillery",
        "default_profile.weaponry.torpedoes",
        "default_profile.mobility.total",
        "default_profile.concealment.total",
        "price_credit",
        "price_gold"
    ], page_no=i)
    all_ships += page.values()
    print('.', end='')

print("complete")
# Connection to MySQL
cnx = mysql.connector.connect(user='michael', password='_tacocat_',
                              host='instancem.cf4rtyoqhdsw.us-east-1.rds.amazonaws.com',
                              database='warships')
cursor = cnx.cursor()

print("clearing database...")
cursor.execute("truncate ships")

query = ("insert into ships (nation, name, class, tier, survivability, artillery, "
         "aa, torpedo, aircraft, maneuverability, concealment) "
         "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

for ship in all_ships:
    if "[" not in ship["name"] and "]" not in ship["name"]:
        default_profile = ship["default_profile"]
        data_ships = (
                    ship["nation"],
                    ship["name"],
                    ship["type"],
                    ship["tier"],
                    default_profile["armour"]["total"],
                    default_profile["weaponry"]["artillery"],
                    default_profile["weaponry"]["anti_aircraft"],
                    default_profile["weaponry"]["torpedoes"],
                    default_profile["weaponry"]["aircraft"],
                    default_profile["mobility"]["total"],
                    default_profile["concealment"]["total"]
                    )
        cursor.execute(query, data_ships)
        print("[SUCCESS] tier %s %s :[ %s ] inserted into dock without lube. - %s" %
              (ship["tier"], ship["type"], ship["name"],
               datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

cnx.commit()

cursor.close()
cnx.close()
