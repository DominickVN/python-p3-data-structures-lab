spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_symbols = '🌶' * heat_level

        output = f"{name} ({cuisine}) | Heat Level: {heat_symbols}"
        print(output)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return "Please enter a proper Cuisine."

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            name = food['name']
            cuisine = food['cuisine']
            heat_level = '🌶' * food['heat_level']

            output = f"{name} ({cuisine}) | Heat Level: {heat_level}"
            print(output)

def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_foods = len(spicy_foods)

    for food in spicy_foods:
        total_heat += food['heat_level']

    average = total_heat / num_foods
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    modified_list = list(spicy_foods)
    modified_list.append(new_food)
    return modified_list

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

result = create_spicy_food(spicy_foods, new_food)
print(result)
