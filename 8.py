def add_dicts(dict1 :dict,dict2 :dict)->dict:
    for i in dict2.keys():
        if i in dict1.keys():
            dict1[i]+=dict2[i]
        else:
            dict1[i] = dict2[i]
    return dict1
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
print(add_dicts(dict1,dict2))