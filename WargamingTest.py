import wargaming

wows = wargaming.WoWS('3672a1d96819ef8bfe0ac902ad887a00', region='asia', language='en')

all_ships = []
i = 1
while i < 4:
    page = wows.encyclopedia.ships(fields=[
        "name", "nation", "type", "tier", "is_premium"], page_no=i)
    if bool(page):
        all_ships += page.values()
        i = i+1
    else:
        break

print(all_ships)

for ship in all_ships:
    print("name: %s, nation: %s, type: %s, tier: %d" % (ship["name"], ship["nation"], ship["type"], ship["tier"]))
