def rem_dup(dict_list:list):
    deleter = []
    for i in range(len(dict_list)):
        for j in range(len(dict_list)):
            if i==j:
                continue
            if dict_list[i]==dict_list[j] and (i not in deleter) and (j not in deleter):
                deleter.append(j)
    deleter.sort(reverse = True)
    for i in deleter:
        dict_list.pop(i)
    return dict_list
dict_list = [{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
output = rem_dup(dict_list)
print(output)