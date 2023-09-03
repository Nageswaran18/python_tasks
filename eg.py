the_dic_value= {
    'name':'naga',
    'age':20,
    'phone_number':8277887
    }, 
    

# for x in the_dic:
#     print(x['name'])




name_list = ["swee","naga"]
value_list = list()
for name in name_list:
    name_dict = dict()
    name_dict['name'] = name
    value_list.append(name_dict)
print(value_list)



name_new_list = ['swee','naga','siva']
empty_list = []
for name_new in name_new_list:
    the_dict = dict()
    the_dict['name'] = name_new
    empty_list.append(the_dict)
print('new values:'f'{empty_list}')









