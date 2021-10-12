# Создать словарь х-тик продукта с ключами "title" (str), "price"(float), "ingredients" (list)
# 1. Добавить еще одну пару ключ-значение "descriptions": какой-то текст
pr = {"title": "potato", "price": 20.5, "ingredients": [1, 2, 3]}
print(pr)
pr["descriptions"] = 'red'
print(pr)
print( '-------------------------- next exercise 2 ')
# 2. Увеличить цену на 100
pr["price"] = pr["price"]+100
print(pr)
print('-------------------------- next exercise 3 ')
# 3. Добавить в список инградиентов еще один инградиент.
pr["ingredients"].append(2)
pr["ingredients"].append(5)
print(pr)
print( '-------------------------- next exercise 4 ')
# 4. Вывести на экран кол-во инградиентов.
print(len(pr["ingredients"]))
print( '-------------------------- next exercise 5 ')
# 5. Удалить из словаря значение с ключем 'descriptions'
pr.pop('descriptions')
print(pr)
