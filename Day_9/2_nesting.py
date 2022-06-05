# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgard"],
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12,
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
        "total_visited": 5,
    },
}

# Nesting a distionary inside a list
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
