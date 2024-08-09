#my_dict = {'tuple':'', 'list':'', 'dict': '', 'set': ''}
my_dict = {}
my_dict['tuple'] = (1,2,3,4,5)
my_dict['list'] = [1,2,3,4,5]
my_dict['dict'] = {1,2,3,4,5}
my_dict['set'] = {1,2,3,4,5}

new_tuple = my_dict['tuple']       #кортеж. Вывести на экран последний элемент

new_list = my_dict['list']        #лист. добавьте в конец списка еще один элемент и удалите второй элемент списка
new_list.append(66)
new_list.pop(2)

my_dict['dict'][('sdf')] = 343
new_dict = my_dict['dict']        #словари. добавьте элемент с ключом ('i am a tuple',) и любым значением
#new_dict[('i am a tuple',)] = (15,)          #словари. удалите какой-нибудь элемент
new_dict.remove(1)

print(new_tuple[-1])
print(new_list)
print(new_dict)
#print(my_dict)

#print(my_dict.keys())
#print(my_dict.values())
#(my_dict.items())