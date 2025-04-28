recipes = []

with open('recipes.txt', 'r', encoding='utf8') as file: # открываем файл с рецептами на чтение.
    for product_list in file:
        dish_name = product_list.strip()
        dish = {"name": dish_name, "ingredients": []}
        ingredients_count = file.readline()
        for ing in range(int(ingredients_count)):
            ingredients = file.readline()
            name, quantity, measure = ingredients.strip().split(' | ')
            dish ['ingredients'].append({'name': name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        recipes.append(dish)

def get_shop_list_by_dishes(list_dish, people):
    '''
    Функция, которая на вход принимает список блюд из cook_book и
    количество персон для кого мы будем готовить.
    '''
    purchases = {}
    for dish in list_dish:
        for dish_book in recipes:
            if dish_book['name'] == dish:
                for ing in dish_book['ingredients']:
                    if ing['name'] not in purchases.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity'])
                        purchases[ing['name']] = {'measure': measure, 'quantity': quantity}
                    
                    elif ing['name'] in purchases.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity']) + int((purchases[ing['name']])['quantity'])
                        purchases[ing['name']] = {'measure': measure, 'quantity': quantity}
    return purchases

print(get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 3))
