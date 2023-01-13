def filework(name):
    with open(name, 'rt', encoding='utf-8') as file:
        cook_book_ = {}

        for line in file:
            name_cook = line.strip()
            ingredient_count = int(file.readline())
            ingr_list = []
            for _ in range(ingredient_count):
                ingr = file.readline().strip().split(' | ')
                name, qu, mea = ingr
                ingr_list += [{'ingredient_name': name, 'quantity': int(qu), 'measure': mea}]
            cook_book_[name_cook] = ingr_list
            file.readline()
    return cook_book_


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            list_item = dict(ingredient)
            list_item['quantity'] *= person_count
            if list_item['ingredient_name'] in shop_list:
                shop_list[list_item['ingredient_name']]['quantity'] = list_item['quantity']
            else:
                shop_list[list_item['ingredient_name']] = list_item
                del(shop_list[list_item['ingredient_name']]['ingredient_name'])
    return shop_list


cook_book = filework('recipes.txt')
print(cook_book)
print()

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
        