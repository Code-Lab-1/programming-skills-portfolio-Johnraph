favorite_places = {
    'Liam': ['beach', 'everest', 'mt canlaon'],
    'Olivia': ['Palawan', 'Baguio'],
    'Lucas': ['Batangas', 'Tagaytay', 'Ilocos']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")