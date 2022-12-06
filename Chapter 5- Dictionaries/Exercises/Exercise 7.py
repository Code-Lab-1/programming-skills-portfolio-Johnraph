favorite_numbers = {
    'maya': [13, 17],
    'addison': [31, 27, 65],
    'Aurora': [3, 22],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")