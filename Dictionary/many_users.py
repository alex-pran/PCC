

users = {
    'kate': {
        'first': 'ekaterina',
        'last': 'shishkina',
        'month': 'april'
    },

    'alex': {
        'first': 'alexandr',
        'last': 'pranitchii',
        'month': 'march'
    }
}

for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    dob = f"{user_info['month']}"
    print(f"\tFull name: {full_name}")
    print(f"\tMonth: {dob.title()}")
