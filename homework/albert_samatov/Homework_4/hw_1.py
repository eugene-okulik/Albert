my_dict = {}
my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = [1, 2, 3, 4, 5]
my_dict['dict'] = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
my_dict['set'] = {1, 2, 3, 4, 5}

new_tuple = my_dict['tuple']  # кортеж. Вывести на экран последний элемент, print(new_tuple[-1])

new_list = my_dict['list']  # лист. добавьте в конец списка еще один элемент и удалите второй элемент списка
new_list.append(66)
new_list.pop(1)

new_dict = my_dict['dict']
new_dict.update({'i am a tuple': '720'})  # словари. добавьте элемент с ключом ('i am a tuple',) и любым значением
new_dict.pop(1)  # словари. удалите какой-нибудь элемент

new_set = my_dict['set']
new_set.add(42)
new_set.remove(1)

print(new_tuple[-1])
print(new_list)
print(new_dict)
print(new_set)

print('\n', my_dict)
