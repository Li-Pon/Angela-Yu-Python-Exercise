travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
        "total_visited": 5,
    },
]
#-------------------------
def add_new_country(country, times, cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["cities_visited"] = cities
    new_dict["total_visited"] = times
    travel_log.append(new_dict)
#-------------------------
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
